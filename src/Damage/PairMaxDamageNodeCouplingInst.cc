//------------------------------------------------------------------------------
// Explicit instantiation.
//------------------------------------------------------------------------------

#include "config.hh"
#include "Damage/PairMaxDamageNodeCoupling.cc"

namespace Spheral {
#if defined(SPHERAL_ENABLE_1D)
  template class PairMaxDamageNodeCoupling< Dim<1> >;
#endif

#if defined(SPHERAL_ENABLE_2D)
  template class PairMaxDamageNodeCoupling< Dim<2> >;
#endif

#if defined(SPHERAL_ENABLE_3D)
  template class PairMaxDamageNodeCoupling< Dim<3> >;
#endif
}