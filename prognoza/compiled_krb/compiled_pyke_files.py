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
           [1621112112.8804228, 'kisa_fc.py'],
         ('', '', 'vrijeme.kfb'):
           [1621112112.8844194, 'vrijeme.fbc'],
        },
        compiler_version)

