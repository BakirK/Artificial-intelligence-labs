import contextlib
import sys

from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)

def staPonijeti(k, v):
    print('kisa:' + k)
    print('vjetar:' + v)
    engine.reset()
    engine.activate('kisa_bc')
    print("doing proof")
    try:
        with engine.prove_goal(
            'vrijeme.ponijeti($kisa, $vjetar, $ponijeti)',
             kisa=k,
              vjetar=v
              ) as gen:
            for vars, plan in gen:
                print("Trebate ponijeti: %s" % (vars['ponijeti']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1) 
    engine.print_stats()
    print()
    print("done")
    