from __future__ import print_function, division

import numpy as np

# Import sile objects
from ..sile import add_sile, Sile_fh_open
from .sile import *
from sisl.unit.siesta import unit_convert


__all__ = ['fcSileSiesta']


class fcSileSiesta(SileSiesta):
    """ Force constants Siesta file object """

    @Sile_fh_open
    def read_force(self, displacement=None, na=None):
        """ Reads all displacement forces by multiplying with the displacement value

        Since the force constant file does not contain the non-displaced configuration
        this will only return forces on the displaced configurations minus the forces from
        the non-displaced configuration.

        This may be used in conjunction with phonopy by noticing that Siesta FC-runs does
        the displacements in reverse order (-x/+x vs. +x/-x). In this case one should reorder
        the elements like this:

        >>> fc = np.roll(fc, 1, axis=2) # doctest: +SKIP

        Parameters
        ----------
        displacement : float, optional
           the used displacement in the calculation, since Siesta 4.1-b4 this value
           is written in the FC file and hence not required.
           If prior Siesta versions are used and this is not supplied the 0.04 Bohr displacement
           will be assumed.
        na : int, optional
           number of atoms (for returning correct number of atoms), since Siesta 4.1-b4 this value
           is written in the FC file and hence not required.
           If prior Siesta versions are used then the file is expected to only contain 1-atom displacement.

        Returns
        -------
        forces : numpy.ndarray with 5 dimensions containing all the forces. The 2nd dimensions contains
                 contains the directions, and 3rd dimensions contains -/+ displacements.
        """
        if displacement is None:
            line = self.readline().split()
            self.fh.seek(0)
            try:
                displacement = float(line[-1])
            except:
                displacement = 0.04 * unit_convert('Bohr', 'Ang')

        # Since the displacements changes sign (starting with a negative sign)
        # we can convert using this scheme
        displacement = np.repeat(displacement, 6).ravel()
        displacement[1::2] *= -1
        return self.read_force_constant(na) * displacement.reshape(1, 3, 2, 1, 1)

    @Sile_fh_open
    def read_force_constant(self, na=None):
        """ Reads the force-constant stored in the FC file

        Parameters
        ----------
        na : int, optional
           number of atoms in the unit-cell, if not specified it will guess on only
           one atom displacement.

        Returns
        -------
        force constants : numpy.ndarray with 5 dimensions containing all the forces. The 2nd dimensions contains
                 contains the directions, and 3rd dimensions contains -/+ displacements.
        """
        # Force constants matrix
        line = self.readline().split()
        if na is None:
            try:
                na = int(line[-2])
            except:
                na = None

        fc = list()
        while True:
            line = self.readline()
            if line == '':
                # empty line or nothing
                break
            fc.append(list(map(float, line.split())))

        # Units are already eV / Ang ** 2
        fc = np.array(fc)

        # Slice to correct size
        if na is None:
            na = fc.size // 6 // 3

        # Correct shape of matrix
        fc.shape = (-1, 3, 2, na, 3)

        return fc

add_sile('FC', fcSileSiesta, case=False, gzip=True)
add_sile('FCC', fcSileSiesta, case=False, gzip=True)
