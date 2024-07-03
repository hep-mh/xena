# math
from math import log10

# input
from acropolis.input import InputInterface
# models
from acropolis.models import AbstractModel
# params
from acropolis.params import universal
# pprint
from acropolis.pprint import print_error


class NeutrinoCascadeModel(AbstractModel):
    
    def __init__(self, io_directory):
        if not universal:
            print_error(
                "NeutrinoCascadeModel requires 'universal = True'.",
                "xena.models.NeutrinoCascadeModel"
            )
        
        self._sII = InputInterface( io_directory, type="dir" )

        # Check if all required parameters are present
        if not all(element in self._sII.param_keys() for element in ["mphi", "tau", "eta"]):
            print_error(
                f"Not all required parameters are present in {io_directory}/param_file.dat.",
                "xena.models.NeutrinoCascadeModel"
            )

        # -->
        self._sMphi = self._sII.parameter("mphi")
        self._sTau  = self._sII.parameter("tau")

        # Call the super constructor
        super(NeutrinoCascadeModel, self).__init__(self._sMphi/2., self._sII)
    
    # ABSTRACT METHODS ##################################################################

    def _temperature_range(self):
        # Calculate the approximate decay temperature
        Td = self._sII.temperature( self._sTau )
        # Calculate Tmin and Tmax from Td
        Td_ofm = log10(Td)

        Tmin = 10.**(Td_ofm - 2.00)
        Tmax = 10.**(Td_ofm + 1.10)

        return (Tmin, Tmax)


    def _source_photon_0(self, T):
        return self._sII.cosmo_column(6, T)


    def _source_electron_0(self, T):
        return 0.


class EmDecayModel(AbstractModel):
    
    def __init__(self, io_directory):
        pass