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
           [1622051553.337224, 'kisa_fc.py'],
         ('', '', 'kisa_bc.krb'):
           [1622051553.3512182, 'kisa_bc_bc.py'],
         ('', '', 'kisa_bc_question.krb'):
           [1622051553.3762152, 'kisa_bc_question_bc.py'],
         ('', '', 'questions.kqb'):
           [1622051553.3961868, 'questions.qbc'],
         ('', '', 'vrijeme.kfb'):
           [1622051553.4021854, 'vrijeme.fbc'],
        },
        compiler_version)

