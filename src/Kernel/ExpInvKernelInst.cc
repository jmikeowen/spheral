//------------------------------------------------------------------------------
// Explicit instantiation.
//------------------------------------------------------------------------------

#include "config.hh"
#include "Kernel/ExpInvKernel.hh"
#include "Geometry/Dimension.hh"

namespace Spheral {
#if defined(SPHERAL_ENABLE_1D)
  template class ExpInvKernel< Dim<1> >;
#endif

#if defined(SPHERAL_ENABLE_2D)
  template class ExpInvKernel< Dim<2> >;
#endif

#if defined(SPHERAL_ENABLE_3D)
  template class ExpInvKernel< Dim<3> >;
#endif
}