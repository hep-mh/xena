# Xena - The Disintegration Princess

![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square)

A wrapper code around ``ACROPOLIS`` (https://github.com/hep-mh/acropolis/) to calculate photo- and hadrodisintegration constraints for more specific BSM scenarios that are not part of the core ``ACROPOLIS`` package

| Input              | Output             |
| ------------------ | ------------------ |
| param_file.dat     | bbundance_file.dat |
| cosmo_file.dat     |                    |
| abundance_file.dat | 

# How to run

First install ``v2``(currently in alpha) of ``ACROPOLIS`` (preferably in a virtual environment) via
```
pip3 install git+https://github.com/hep-mh/acropolis.git@v2
```
Afterwards run
```
./bin/xena <model_class> <io_directory>
```
Here, both command-line arguments are mandatory. The argument ``<model_class>`` is the name of the model to use (currently only ``NeutrinoCascadeModel`` and ``EmDecayModel`` are supported), and the argument ``<io_directory>`` is the directory where to find ``cosmo_file.dat``, ``param_file.dat`` and ``abundance_file.dat``

An example output of running ``./bin/xena NeutrinoCascadeModel io/test`` would be
```
Xena v1.0 (using ACROPOLIS v2.0.0 [dev])

INFO   : Using the model 'NeutrinoCascadeModel'.
INFO   : Using 'universal = True' as required by the model.
INFO   : Using the directory 'io/test' to read and write data.
INFO   : Using parameters from 'io/test/param_file.dat'.
INFO   : Using cosmological data from 'io/test/cosmo_file.dat'.
INFO   : Using initial abundances from 'io/test/abundance_file.dat'.
INFO   : Running photo- and hadrodisintegration...Done!
INFO   : The final abundances are:

     |     mean     |    high Γ    |    low Γ     |    high ξ    |    low ξ    
-------------------------------------------------------------------------------
   n | 0.000000e+00 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00  [decayed]
   p | 7.559015e-01 | 7.559705e-01 | 7.558327e-01 | 7.559047e-01 | 7.558983e-01
  H2 | 2.253442e-05 | 2.213301e-05 | 2.294575e-05 | 2.327524e-05 | 2.179358e-05
  H3 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00  [decayed]
 He3 | 1.352834e-05 | 1.358545e-05 | 1.347749e-05 | 1.461604e-05 | 1.244062e-05
 He4 | 6.100487e-02 | 6.098777e-02 | 6.102189e-02 | 6.100321e-02 | 6.100654e-02
 Li6 | 3.077093e-14 | 5.069457e-14 | 2.249760e-14 | 3.077093e-14 | 3.077093e-14
 Li7 | 3.932416e-10 | 4.187589e-10 | 3.698327e-10 | 3.932416e-10 | 3.932416e-10
 Be7 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00  [decayed]

INFO   : The final abundances have been written to 'io/test/bbundance_file.dat'.
```

## The abundance-file
``Xena`` expects an abundance-file with name ``abundance_file.dat`` in ``<io_directory>`` with the same structure as ``ACROPOLIS``


## The param-file
``Xena`` expects a param-file with name ``param_file.dat`` in ``<io_directory>`` with at least one line that reads ``eta=<eta>``, e.g. ``eta=6.137e-10``

When using either ``CascadeNeutrinoModel`` or ``EmDecayModel``, ``Xena`` further expects entries for ``mphi`` [in MeV] and ``tau`` [in s], as well as for ``Bree`` and ``Braa`` in the latter case.

## The cosmo-file
``Xena`` expects a cosmo-file with name ``cosmo_file.dat`` in ``<io_directory>`` with the column structure
* ``t`` in s
* ``T`` in MeV
* ``dTdt`` in MeV²
* ``Tnu`` in MeV
* ``H`` in MeV
* ``nb_etaf`` in MeV³

When using the model ``NeutrinoCascadeModel``, ``Xena`` aditionally expects six more column with
* ``Sem`` in MeV⁴
* ``Shd`` in MeV⁴
* ``dndt_sc`` in MeV⁴
* ``Khd_sc`` in MeV
* ``dndt_sh`` in MeV⁴
* ``Khd_sh`` in MeV

When using the model ``EmDecayModel``, ``Xena``additionally expects a seventh column with
* ``nphi`` in MeV³
