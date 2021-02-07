.. _io.siesta:

Siesta
======

.. currentmodule:: sisl.io.siesta

.. autosummary::
   :toctree: api-generated/

   fdfSileSiesta - input file
   outSileSiesta - output file
   xvSileSiesta - xyz and vxyz file
   bandsSileSiesta - band structure information
   eigSileSiesta - EIG file
   pdosSileSiesta - PDOS file
   gridSileSiesta - Grid charge information (binary)
   gridncSileSiesta - NetCDF grid output files (netcdf)
   onlysSileSiesta - Overlap matrix information
   dmSileSiesta - density matrix information
   hsxSileSiesta - Hamiltonian and overlap matrix information
   wfsxSileSiesta - wavefunctions
   ncSileSiesta - NetCDF output file
   ionxmlSileSiesta - Basis-information from the ion.xml files
   ionncSileSiesta - Basis-information from the ion.nc files
   orbindxSileSiesta - Basis set information (no geometry information)
   faSileSiesta - Forces on atoms
   fcSileSiesta - Force constant matrix
   kpSileSiesta - k-points from simulation
   rkpSileSiesta - k-points to simulation


TranSiesta
==========

.. autosummary::
   :toctree: api-generated/

   tshsSileSiesta - TranSiesta Hamiltonian
   tsdeSileSiesta - TranSiesta (energy) density matrix
   tsgfSileSiesta - TranSiesta surface Green function files
   tsvncSileSiesta - TranSiesta specific Hartree potential file


TBtrans
=======

.. currentmodule:: sisl.io.tbtrans

.. autosummary::
   :toctree: api-generated/

   tbtncSileTBtrans
   deltancSileTBtrans
   tbtgfSileTBtrans - TBtrans surface Green function files
   tbtsencSileTBtrans
   tbtavncSileTBtrans
   tbtprojncSileTBtrans

`TBtrans`_ is per default a ballistic electron transport utility. It may also
be compiled in a ballistic phonon transport mode, named ``PHtrans``.

.. autosummary::
   :toctree: api-generated/

   phtncSilePHtrans
   phtsencSilePHtrans
   phtavncSilePHtrans
   phtprojncSilePHtrans