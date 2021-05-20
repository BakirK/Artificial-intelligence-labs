import contextlib
import sys

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('vrijeme.ponijeti($ponijeti)')

def staPonijeti():
    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('kisa')
    print("doing proof")
    with fc_goal.prove(engine) as gen:
        for vars, plan in gen:
            print("Trebate ponijeti: %s" % (vars['ponijeti']))
    engine.print_stats()
    print()
    print("done")
    