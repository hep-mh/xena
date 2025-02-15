# Xena - The Photodisintegration Princess

A wrapper code around ``ACROPOLIS`` (https://github.com/hep-mh/acropolis/) to calculate photodisintegration constraints for more specific BSM scenarios that are not part of the core ``ACROPOLIS`` package

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
INFO   : Running photodisintegration...Done!
INFO   : The final abundances are:

     |     mean     |     high     |     low     
-------------------------------------------------
   n | 0.000000e+00 | 0.000000e+00 | 0.000000e+00  [decayed]
   p | 7.529170e-01 | 7.528786e-01 | 7.529565e-01
  H2 | 1.892391e-05 | 1.852884e-05 | 1.932896e-05
  H3 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00  [decayed]
 He3 | 7.774584e-06 | 7.831135e-06 | 7.724084e-06
 He4 | 6.175413e-02 | 6.176388e-02 | 6.174408e-02
 Li6 | 8.227352e-15 | 2.793651e-14 | 1.294786e-15
 Li7 | 3.524633e-10 | 3.154068e-10 | 3.380052e-10
 Be7 | 0.000000e+00 | 0.000000e+00 | 0.000000e+00  [decayed]

INFO   : The final abundances have been written to 'io/test/bbundance_file.dat'.
```

## The abundance-file
``Xena`` expects an abundance-file with name ``abundance_file.dat`` in ``<io_directory>`` with the same structure as ``ACROPOLIS``


## The param-file
``Xena`` expects a param-file with name ``param_file.dat`` in ``<io_directory>`` with at least one line that reads ``eta=<eta>``, e.g. ``eta=6.137e-10``

When using either ``CascadeNeutrinoModel`` or ``EmDecayModel``, ``Xena`` further expects entries for ``mphi`` [in MeV] and ``tau`` [in s], as well as for ``bree`` and ``braa`` in the latter case.

## The cosmo-file
``Xena`` expects a cosmo-file with name ``cosmo_file.dat`` in ``<io_directory>`` with the column structure
* ``t`` in s
* ``T`` in MeV
* ``dTdt`` in MeV²
* ``Tnu`` in MeV
* ``H`` in MeV
* ``nb_etaf`` in MeV³

When using the model ``NeutrinoCascadeModel``, ``Xena`` aditionally expects a seventh column with
* ``Sem`` in MeV⁴
* ``Shd`` in MeV⁴
* ``dndt_sc`` in MeV⁴
* ``Khd_sc`` in MeV
* ``dndt_sh`` in MeV⁴
* ``Khd_sh`` in MeV

When using the model ``EmDecayModel``, ``Xena``additionally expects a seventh column with
* ``nphi`` in MeV³
