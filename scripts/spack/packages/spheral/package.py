# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import socket
import os

class Spheral(CachedCMakePackage, PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://spheral.readthedocs.io/"
    git      = "https://github.com/llnl/spheral.git"
    tags     = ['radiuss', 'simulations', 'hydrodynamics']

    maintainers = ['mdavis36','jmikeowen']

    # -------------------------------------------------------------------------
    # VERSIONS
    # -------------------------------------------------------------------------
    version('develop', branch='feature/spack', submodules=True)
    version('1.0', tag='FSISPH-v1.0', submodules=True)

    # -------------------------------------------------------------------------
    # VARIANTS
    # -------------------------------------------------------------------------
    variant('mpi', default=True, description='Enable MPI Support.')
    variant('openmp', default=True, description='Enable OpenMP Support.')
    variant('docs', default=False, description='Enable building Docs.')

    # -------------------------------------------------------------------------
    # DEPENDS
    # -------------------------------------------------------------------------
    depends_on('mpi', type=['build','run'], when='+mpi')
    depends_on('cmake@3.10.0:', type='build')

    depends_on('zlib@1.2.11 -shared +pic', type='build')

    depends_on('boost@1.74.0 -atomic -container -coroutine -chrono -context -date_time -exception -fiber -graph -iostreams -locale -log -math -mpi -program_options -python -random -regex -serialization -test -thread -timer -wave +pic', type='build')

    # TODO: ANEOS
    # TODO: qhull spack package seems to be broken...
    #depends_on('qhull@2020.2', type='build')
    #TODO: Polyclipper package.

    depends_on('eigen@3.3.7', type='build')
    depends_on('hdf5@1.8.19 ~mpi +hl', type='build')
    depends_on('silo@4.10.2 +hdf5', type='build')

    # Zlib fix has been merged into conduit, using develop until next release.
    #depends_on('conduit@develop +mpi +hdf5 -shared -test', type='build')
    depends_on('conduit@develop +mpi +hdf5 -test', type=['build','run'], when='+mpi')
    depends_on('conduit@develop ~mpi +hdf5 -test', type=['build','run'], when='~mpi')

    depends_on('axom@0.5.0 +mpi +hdf5 -lua -examples -python -fortran -umpire -raja', type=['build','run'], when='+mpi')
    depends_on('axom@0.5.0 ~mpi +hdf5 -lua -examples -python -fortran -umpire -raja', type=['build','run'], when='~mpi')

    depends_on('opensubdiv@3.4.3', type='build')
    depends_on('polytope', type='build')

    extends('python@2.7.16 +zlib +shared', type='build')

    depends_on('py-pip@9.0.1', type='build')
    depends_on('py-pybind11@2.4.3', type='build')
    depends_on('py-pyb11generator@1.0.12', type='build')

    def _get_sys_type(self, spec):
        sys_type = spec.architecture
        if "SYS_TYPE" in env:
            sys_type = env["SYS_TYPE"]
        return sys_type

    @property
    def cache_name(self):

        hostname = socket.gethostname()
        if "SYS_TYPE" in env:
            hostname = hostname.rstrip('1234567890')

        envspec = os.environ.get("SPEC")
        if envspec:
          cache_spec = envspec
        else:
          cache_spec = self.spec.compiler.name + "@" + self.spec.compiler.version
        return "{0}-{1}-{2}.cmake".format(
            hostname,
            self._get_sys_type(self.spec),
            cache_spec
        )

    def initconfig_compiler_entries(self):
        spec = self.spec
        entries = super(Spheral, self).initconfig_compiler_entries()
        return entries
    

    def initconfig_hardware_entries(self):
        spec = self.spec
        entries = super(Spheral, self).initconfig_hardware_entries()

        #if '+cuda' in spec:
        #    entries.append(cmake_cache_option("ENABLE_CUDA", True))

        #    if not spec.satisfies('cuda_arch=none'):
        #        cuda_arch = spec.variants['cuda_arch'].value
        #        entries.append(cmake_cache_string("CUDA_ARCH", 'sm_{0}'.format(cuda_arch[0])))
        #        entries.append(cmake_cache_string("CMAKE_CUDA_ARCHITECTURES={0}".format(cuda_arch[0])))
        #        flag = '-arch sm_{0}'.format(cuda_arch[0])
        #        entries.append(cmake_cache_string("CMAKE_CUDA_FLAGS", '{0}'.format(flag)))

        #    entries.append(cmake_cache_option("ENABLE_DEVICE_CONST", spec.satisfies('+deviceconst')))
        #else:
        #    entries.append(cmake_cache_option("ENABLE_CUDA", False))

        #if '+rocm' in spec:
        #    entries.append(cmake_cache_option("ENABLE_HIP", True))
        #    entries.append(cmake_cache_path("HIP_ROOT_DIR", '{0}'.format(spec['hip'].prefix)))
        #    archs = self.spec.variants['amdgpu_target'].value
        #    if archs != 'none':
        #        arch_str = ",".join(archs)
        #        entries.append(cmake_cache_string("HIP_HIPCC_FLAGS", '--amdgpu-target={0}'.format(arch_str)))
        #else:
        #    entries.append(cmake_cache_option("ENABLE_HIP", False))

        return entries

    def initconfig_package_entries(self):
        spec = self.spec
        entries = []

        # TPL locations
        #entries.append("#------------------{0}".format("-" * 60))
        #entries.append("# TPLs")
        #entries.append("#------------------{0}\n".format("-" * 60))

        #entries.append(cmake_cache_path("BLT_SOURCE_DIR", spec['blt'].prefix))
        #if spec.satisfies('@5.0.0:'):
        #    entries.append(cmake_cache_path("camp_DIR" ,spec['camp'].prefix))
        #entries.append(cmake_cache_option("ENABLE_NUMA", '+numa' in spec))
        #entries.append(cmake_cache_option("ENABLE_OPENMP", '+openmp' in spec))
        #entries.append(cmake_cache_option("ENABLE_BENCHMARKS", 'tests=benchmarks' in spec))
        #entries.append(cmake_cache_option("ENABLE_EXAMPLES", '+examples' in spec))
        #entries.append(cmake_cache_option("BUILD_SHARED_LIBS", '+shared' in spec))
        #entries.append(cmake_cache_option("ENABLE_TESTS", not 'tests=none' in spec))
        entries.append(cmake_cache_option('ENABLE_CXXONLY', False))
        entries.append(cmake_cache_option('TPL_VERBOSE', False))
        entries.append(cmake_cache_option('BUILD_TPL', True))

        entries.append(cmake_cache_option('python_BUILD', False))
        entries.append(cmake_cache_path('python_DIR', spec['python'].prefix))

        entries.append(cmake_cache_option('zlib_BUILD', False))
        entries.append(cmake_cache_path('zlib_DIR', spec['zlib'].prefix))

        entries.append(cmake_cache_option('boost_BUILD', False))
        entries.append(cmake_cache_path('boost_DIR', spec['boost'].prefix))

        #entries.append(cmake_cache_option('qhull_BUILD', False))
        #entries.append(cmake_cache_path('qhull_DIR', spec['qhull'].prefix))

        entries.append(cmake_cache_option('hdf5_BUILD', False))
        entries.append(cmake_cache_path('hdf5_DIR', spec['hdf5'].prefix))

        entries.append(cmake_cache_option('conduit_BUILD', False))
        entries.append(cmake_cache_path('conduit_DIR', spec['conduit'].prefix))

        entries.append(cmake_cache_option('axom_BUILD', False))
        entries.append(cmake_cache_path('axom_DIR', spec['axom'].prefix))

        entries.append(cmake_cache_option('silo_BUILD', False))
        entries.append(cmake_cache_path('silo_DIR', spec['silo'].prefix))

        entries.append(cmake_cache_option('eigen_BUILD', False))
        entries.append(cmake_cache_path('eigen_DIR', spec['eigen'].prefix))
        entries.append(cmake_cache_path('eigen_INCLUDES', spec['eigen'].prefix.include.eigen3))

        entries.append(cmake_cache_option('opensubdiv_BUILD', False))
        entries.append(cmake_cache_path('opensubdiv_DIR', spec['opensubdiv'].prefix))

        entries.append(cmake_cache_option('pip_BUILD', False))
        entries.append(cmake_cache_path('pip_DIR', spec['py-pip'].prefix + '/lib/python2.7/site-packages/'))

        entries.append(cmake_cache_option('setuptools_BUILD', False))
        entries.append(cmake_cache_path('setuptools_DIR', spec['py-setuptools'].prefix + '/lib/python2.7/site-packages/'))

        entries.append(cmake_cache_option('pybind11_BUILD', False))
        entries.append(cmake_cache_path('pybind11_DIR', spec['py-pybind11'].prefix))

        entries.append(cmake_cache_option('pyb11generator_BUILD', False))
        entries.append(cmake_cache_path('pyb11generator_DIR', spec['py-pyb11generator'].prefix + '/lib/python2.7/site-packages/'))

        entries.append(cmake_cache_option('polytope_BUILD', False))
        entries.append(cmake_cache_path('polytope_DIR', spec['polytope'].prefix))

        entries.append(cmake_cache_option('ENABLE_MPI', '+mpi' in spec))
        if "+mpi" in spec:
            entries.append(cmake_cache_path('-DMPI_C_COMPILER', spec['mpi'].mpicc) )
            entries.append(cmake_cache_path('-DMPI_CXX_COMPILER', spec['mpi'].mpicxx) )

        entries.append(cmake_cache_option('ENABLE_OPENMP', '+openmp' in spec))
        entries.append(cmake_cache_option('ENABLE_DOCS', '+docs' in spec))


        return entries


    def cmake_args(self):
        options = []
        spec = self.spec

        return options