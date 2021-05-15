import types
from pyke import contexts, pattern
import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('vrijeme.ponijeti($rain, $wind, $ponijeti)')


def fc_test(person1):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    # Runs all applicable forward-chaining rules.
    engine.activate('fc_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    with fc_goal.prove(engine, person1=person1) as gen:
        for vars, plan in gen:
            print("%s, %s are %s, %s" %
                  (person1, vars['person2'], vars['r1'], vars['r2']))
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
