# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'kisa.krb'):
           [1621459795.7029445, 'kisa_fc.py'],
         ('', '', 'kisa_bc.krb'):
           [1621459795.7169256, 'kisa_bc_bc.py'],
         ('', '', 'vrijeme.kfb'):
           [1621459795.7274337, 'vrijeme.fbc'],
        },
        compiler_version)

