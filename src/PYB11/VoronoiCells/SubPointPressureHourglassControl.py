#-------------------------------------------------------------------------------
# SubPointPressureHourglassControl
#-------------------------------------------------------------------------------
from PYB11Generator import *
from Physics import *
from PhysicsAbstractMethods import *
from RestartMethods import *

@PYB11template("Dimension")
@PYB11dynamic_attr
class SubPointPressureHourglassControl(Physics):

    PYB11typedefs = """
    using Scalar = typename %(Dimension)s::Scalar;
    using Vector = typename %(Dimension)s::Vector;
    using Tensor = typename %(Dimension)s::Tensor;
    using SymTensor = typename %(Dimension)s::SymTensor;
    using FacetedVolume = typename %(Dimension)s::FacetedVolume;
    using TimeStepType = typename Physics<%(Dimension)s>::TimeStepType;
"""
    
    def pyinit(self,
               fHG = "Scalar"):
        "SubPointPressureHourglassControl constructor"
        return

    @PYB11virtual
    @PYB11const
    def requireVoronoiCells(self):
        "Some physics algorithms require the Voronoi cells per point be computed."
        return "bool"

    #...........................................................................
    # Properties
    fHG = PYB11property("Scalar", "fHG", "fHG", doc="The fractional multiplier on the hourglass force")           

#-------------------------------------------------------------------------------
# Inject methods
#-------------------------------------------------------------------------------
PYB11inject(PhysicsAbstractMethods, SubPointPressureHourglassControl)