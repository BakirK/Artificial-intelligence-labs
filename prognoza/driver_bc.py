import contextlib
import sys

from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)

def staPonijeti():
    engine.reset()
    #engine.activate('kisa_bc')
    engine.activate('kisa_bc_question')
    print("doing proof")
    try:
        with engine.prove_goal('kisa_bc_question.ponijeti($staPonijeti)') as gen:
            for vars, plan in gen:
                print("Trebate ponijeti: %s" % (vars['staPonijeti']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    try:
        with engine.prove_goal('kisa_bc_question.dodatno($dodatno)') as gen:
            for vars, plan in gen:
                print("Trebate dodatno ponijeti: %s" % (vars['dodatno']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    print()
    print("done")
    