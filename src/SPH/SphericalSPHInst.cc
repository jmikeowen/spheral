//------------------------------------------------------------------------------
// A collection of intantiations for SphericalSPH 
//------------------------------------------------------------------------------
#include "Kernel/SphericalKernel.hh"
#include "Geometry/Dimension.hh"

#include "computeSPHSumMassDensity.cc"
#include "correctSPHSumMassDensity.cc"
#include "SPHHydroBase.hh"
#include "SPHEvaluateDerivativesImpl.cc"

namespace Spheral {

template void computeSPHSumMassDensity(const ConnectivityMap<Dim<1>>&, 
                                       const SphericalKernel&, 
                                       const bool,
                                       const FieldList<Dim<1>, Dim<1>::Vector>&,
                                       const FieldList<Dim<1>, Dim<1>::Scalar>&,
                                       const FieldList<Dim<1>, Dim<1>::SymTensor>&,
                                       FieldList<Dim<1>, Dim<1>::Scalar>&);

template void correctSPHSumMassDensity(const ConnectivityMap<Dim<1>>&, 
                                       const SphericalKernel&, 
                                       const bool,
                                       const FieldList<Dim<1>, Dim<1>::Vector>&,
                                       const FieldList<Dim<1>, Dim<1>::Scalar>&,
                                       const FieldList<Dim<1>, Dim<1>::SymTensor>&,
                                       FieldList<Dim<1>, Dim<1>::Scalar>&);

template void SPHHydroBase<Dim<1>>::evaluateDerivativesImpl(const Dim<1>::Scalar,
                                                            const Dim<1>::Scalar,
                                                            const DataBase<Dim<1>>&,
                                                            const State<Dim<1>>&,
                                                            StateDerivatives<Dim<1>>&,
                                                            const SphericalKernel&,
                                                            const SphericalKernel&,
                                                            const TableKernel<Dim<1>>&) const;
}