# Xena

A wrapper code that utilizes ``ACROPOLIS`` (https://github.com/hep-mh/acropolis/) to handle the process of photodisintegration for more specific BSM scenarios that are not part of the core ``ACROPOLIS`` package

# How to run

First install the xena branch of ``ACROPOLIS`` in a virtual environment via
```
pip3 install git+https://github.com/hep-mh/acropolis.git@xena
```
Afterwards activate the virtual environment and run
```
./bin/xena <model_class> <io_directory>
```
Here, both command-line arguments are mandatory. The argument ``<model_class>`` is the name of the model to use (currently only ``CascadeNeutrinoModel`` is supported), and the argument ``<io_directory>`` is the directory where to find ``cosmo_file.dat``, ``param_file.dat`` and ``abundance_file.dat``

An example output of running ``./bin/xena NeutrinoCascadeModel io/test`` would be
```
Xena v1.0 (using ACROPOLIS v1.2.3)

INFO   : Using the model 'NeutrinoCascadeModel'.
INFO   : Using the directory 'io/test' to read and write data.
INFO   : Using cosmological data from 'io/test/cosmo_file.dat'.
INFO   : Using parameters from 'io/test/param_file.dat'.
INFO   : Using initial abundances from 'io/test/abundance_file.dat'.
INFO   : Running photodisintegration...Done!
INFO   : The final abundances are:

     |    mean     |    high     |    low     
----------------------------------------------
   n | 0.00000e+00 | 0.00000e+00 | 0.00000e+00  [decayed]
   p | 7.52917e-01 | 7.52879e-01 | 7.52957e-01
  H2 | 1.89239e-05 | 1.85288e-05 | 1.93290e-05
  H3 | 0.00000e+00 | 0.00000e+00 | 0.00000e+00  [decayed]
 He3 | 7.77458e-06 | 7.83113e-06 | 7.72408e-06
 He4 | 6.17541e-02 | 6.17639e-02 | 6.17441e-02
 Li6 | 8.22735e-15 | 2.79365e-14 | 1.29479e-15
 Li7 | 3.52463e-10 | 3.15407e-10 | 3.38005e-10
 Be7 | 0.00000e+00 | 0.00000e+00 | 0.00000e+00  [decayed]

INFO   : The final abundances have been written to 'io/test/bbundance_file.dat'.
```

## The abundance-file
``Xena`` expects an abundance-file with name ``abundance_file.dat`` in ``<io_directory>`` with the same structure as ``ACROPOLIS``


## The param-file
``Xena`` expects a param-file with name ``param_file.dat`` in ``<io_directory>`` with at least one line that reads eta=<eta>, e.g. eta=6.137e-10

When using either ``CascadeNeutrinoModel`` or ``EmDecayModel``, ``Xena`` further expects entries for ``mphi`` [in MeV] and ``tau`` [in s]

## The cosmo-file
``Xena`` expects a cosmo-file with name ``cosmo_file.dat`` in ``<io_directory>`` with the column structure
* t in s
* T in MeV
* dTdt in MeV²
* Tnu in MeV
* H in MeV
* nb/etaf in MeV³

When using the model ``NeutrinoCascadeModel``, ``Xena`` aditionally expects a seventh column with
* S in MeV⁴

When using the model ``EmDecayModel``, ``Xena``additionally expects a seventh column with
* nphi in MeV³