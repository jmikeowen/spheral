#-------------------------------------------------------------------------------
# SPHHydroBase
#-------------------------------------------------------------------------------
from PYB11Generator import *
from DEMBase import *

@PYB11template("Dimension")
@PYB11module("SpheralDEM")
class LinearSpringDEM(DEMBase):

    PYB11typedefs = """
  typedef typename %(Dimension)s::Scalar Scalar;
  typedef typename %(Dimension)s::Vector Vector;
  typedef typename DEMDimension<%(Dimension)s>::AngularVector RotationType;
  typedef typename %(Dimension)s::Tensor Tensor;
  typedef typename %(Dimension)s::SymTensor SymTensor;
  typedef typename DEMBase<%(Dimension)s>::TimeStepType TimeStepType;
"""
    
    def pyinit(dataBase = "const DataBase<%(Dimension)s>&",
               normalSpringConstant = "const Scalar",
               restitutionCoefficient = "const Scalar",
               stepsPerCollision = "const Scalar",
               xmin = "const Vector&",
               xmax = "const Vector&"):
        "DEMBase constructor"

    @PYB11virtual
    @PYB11const
    def dt(dataBase = "const DataBase<%(Dimension)s>&", 
           state = "const State<%(Dimension)s>&",
           derivs = "const StateDerivatives<%(Dimension)s>&",
           currentTime = "const Scalar"):
        "Vote on a time step."
        return "TimeStepType"

    @PYB11virtual
    @PYB11const
    def evaluateDerivatives(time = "const Scalar",
                            dt = "const Scalar",
                            dataBase = "const DataBase<%(Dimension)s>&",
                            state = "const State<%(Dimension)s>&",
                            derivs = "StateDerivatives<%(Dimension)s>&"):
        "calculate the derivatives for Linear Spring DEM."
        return "void"

    normalSpringConstant = PYB11property("Scalar", "normalSpringConstant", "normalSpringConstant", doc="linear spring constant")
    restitutionCoefficient = PYB11property("Scalar", "restitutionCoefficient", "restitutionCoefficient", doc="linear restitution coefficient")
    beta = PYB11property("Scalar", "beta", "beta", doc="a damping parameter")
    timeStep = PYB11property("Scalar", "timeStep", "timeStep", doc="constant time-step for this model")
  