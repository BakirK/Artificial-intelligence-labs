import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)
print(engine)

fc_goal = goal.compile('vrijeme.ponijeti($rain, $wind, $ponijeti)')


def staPonijeti(rain, wind):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    # Runs all applicable forward-chaining rules.
    engine.activate('kisa')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    with fc_goal.prove(engine, rain=rain, wind=wind) as gen:
        for vars, plan in gen:
            print("Trebate ponijeti %s" %
                  (vars['ponijeti']))
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec" %
          (fc_time, engine.get_kb('vrijeme').get_stats()[2] / fc_time))
