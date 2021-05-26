# pattern_matching_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def knows_pattern_matching(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', 'pat_master').reset()
        with engine.prove(rule.rule_base.root_name, 'knows_pat_master', context,
                          ()) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "pattern_matching.knows_pattern_matching: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_matching_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'learned_pattern_matching', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_matching_2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pat_master(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pat_master: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def learned_pattern_matching(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'taught_pattern_matching', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.learned_pattern_matching: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_matching', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.learned_pattern_matching: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_1_2_4_16(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1, 2, 4, 16):
              with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'knows_patterns', context,
                                    ()) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 4"
                      with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                        ()) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 5"
                          with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                            ()) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "pattern_matching.taught_pattern_matching_1_2_4_16: got unexpected plan from when clause 6"
                              rule.rule_base.num_bc_rule_successes += 1
                              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_3_5_6_9_15(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_3_5_6_9_15: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3, 5, 6, 9, 15):
              with engine.prove(rule.rule_base.root_name, 'knows_tuple_patterns', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_3_5_6_9_15: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_7_8_10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_7_8_10: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (7, 8, 10):
              with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_7_8_10: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_11_12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_11_12: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11, 12):
              with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_11_12: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def taught_pattern_matching_14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_master', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (14,):
              with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                ()) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                                    ()) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "pattern_matching.taught_pattern_matching_14: got unexpected plan from when clause 4"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_variable_syntax(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pat_var_syntax', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_variable_syntax: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def reset_if_wrong__right(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('special', 'claim_goal', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.reset_if_wrong__right: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def reset_if_wrong__wrong(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', context.lookup_data('question')).reset()
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_patterns(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_literal_patterns', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_patterns: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variables', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_patterns: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'knows_tuple_patterns', context,
                                  ()) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "pattern_matching.knows_patterns: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_literal_patterns(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_literal_patterns: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ask_until_correct__ask(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', context.lookup_data('question'), context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.ask_until_correct__ask: got unexpected plan from when clause 1"
            with engine.prove('special', 'claim_goal', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.ask_until_correct__ask: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ask_until_correct__try_again(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', context.lookup_data('question')).reset()
        print("Try again:")
        with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_3:
          for x_3 in gen_3:
            assert x_3 is None, \
              "pattern_matching.ask_until_correct__try_again: got unexpected plan from when clause 3"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_variables(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_variables: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_pattern_variables: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_pattern_variable_scope(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 1"
            with engine.prove('questions', 'anonymous_syntax', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(3),
                                   rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "pattern_matching.knows_pattern_variable_scope: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_how_patterns_match(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'pattern_scope', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'post_process_pattern_scope', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'ask_until_correct', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "pattern_matching.knows_how_patterns_match: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_literal_patterns', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_syntax', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 2"
                engine.get_ke('questions', 'pattern_scope').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                  ()) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "pattern_matching.post_process_pattern_scope_1: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_2: got unexpected plan from when clause 1"
            engine.get_ke('questions', 'pattern_scope').reset()
            with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "pattern_matching.post_process_pattern_scope_2: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 1"
            with engine.prove('questions', 'same_var_different_rules', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 2"
                engine.get_ke('questions', 'pattern_scope').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                  ()) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "pattern_matching.post_process_pattern_scope_4: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'same_var_different_rules', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_5: got unexpected plan from when clause 1"
            engine.get_ke('questions', 'pattern_scope').reset()
            with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                              ()) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "pattern_matching.post_process_pattern_scope_5: got unexpected plan from when clause 3"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_pattern_scope_6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'knows_patterns', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_pattern_variable_scope', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 2"
                engine.get_ke('questions', 'pattern_scope').reset()
                with engine.prove(rule.rule_base.root_name, 'knows_how_patterns_match', context,
                                  ()) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "pattern_matching.post_process_pattern_scope_6: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_rest_variable(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'rest_pattern_variable_syntax', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_rest_variable: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_rest_match', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_rest_variable: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_rest_match(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'rest_match', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_rest_match: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'post_process_rest_match', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_rest_match: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_rest_match_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        engine.get_ke('questions', 'rest_match').reset()
        with engine.prove(rule.rule_base.root_name, 'knows_rest_match', context,
                          ()) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "pattern_matching.post_process_rest_match_1: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_rest_match_4_5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('ans') in (4, 5):
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "pattern_matching.post_process_rest_match_4_5: got unexpected plan from when clause 2"
              engine.get_ke('questions', 'rest_match').reset()
              with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                                ()) \
                as gen_4:
                for x_4 in gen_4:
                  assert x_4 is None, \
                    "pattern_matching.post_process_rest_match_4_5: got unexpected plan from when clause 4"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def post_process_rest_match_correct(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('ans') in (2, 3):
          rule.rule_base.num_bc_rule_successes += 1
          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def knows_tuple_patterns(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'tuple_pattern_syntax', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "pattern_matching.knows_tuple_patterns: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'knows_rest_variable', context,
                              ()) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "pattern_matching.knows_tuple_patterns: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('pattern_matching')
  
  bc_rule.bc_rule('knows_pattern_matching', This_rule_base, 'knows_pattern_matching',
                  knows_pattern_matching, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_pattern_matching_2', This_rule_base, 'knows_pattern_matching',
                  knows_pattern_matching_2, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_pat_master', This_rule_base, 'knows_pat_master',
                  knows_pat_master, None,
                  (),
                  (),
                  (pattern.pattern_literal(13),))
  
  bc_rule.bc_rule('learned_pattern_matching', This_rule_base, 'learned_pattern_matching',
                  learned_pattern_matching, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('taught_pattern_matching_1_2_4_16', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_1_2_4_16, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_3_5_6_9_15', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_3_5_6_9_15, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_7_8_10', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_7_8_10, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_11_12', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_11_12, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('taught_pattern_matching_14', This_rule_base, 'taught_pattern_matching',
                  taught_pattern_matching_14, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('knows_pattern_variable_syntax', This_rule_base, 'knows_pattern_variable_syntax',
                  knows_pattern_variable_syntax, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('reset_if_wrong__right', This_rule_base, 'reset_if_wrong',
                  reset_if_wrong__right, None,
                  (contexts.anonymous('_'),
                   contexts.variable('right_ans'),
                   contexts.variable('right_ans'),),
                  (),
                  ())
  
  bc_rule.bc_rule('reset_if_wrong__wrong', This_rule_base, 'reset_if_wrong',
                  reset_if_wrong__wrong, None,
                  (contexts.variable('question'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_patterns', This_rule_base, 'knows_patterns',
                  knows_patterns, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_literal_patterns', This_rule_base, 'knows_literal_patterns',
                  knows_literal_patterns, None,
                  (),
                  (),
                  (pattern.pattern_literal('pat_literal'),
                   pattern.pattern_literal(6),))
  
  bc_rule.bc_rule('ask_until_correct__ask', This_rule_base, 'ask_until_correct',
                  ask_until_correct__ask, None,
                  (contexts.variable('question'),
                   contexts.variable('right_ans'),),
                  (),
                  (contexts.variable('right_ans'),))
  
  bc_rule.bc_rule('ask_until_correct__try_again', This_rule_base, 'ask_until_correct',
                  ask_until_correct__try_again, None,
                  (contexts.variable('question'),
                   contexts.variable('right_ans'),),
                  (),
                  (contexts.variable('question'),
                   contexts.variable('right_ans'),))
  
  bc_rule.bc_rule('knows_pattern_variables', This_rule_base, 'knows_pattern_variables',
                  knows_pattern_variables, None,
                  (),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_pattern_variable_scope', This_rule_base, 'knows_pattern_variable_scope',
                  knows_pattern_variable_scope, None,
                  (),
                  (),
                  (pattern.pattern_literal('multiple_matching'),
                   pattern.pattern_literal(4),
                   contexts.anonymous('_'),
                   pattern.pattern_literal('anonymous_matching'),
                   pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('knows_how_patterns_match', This_rule_base, 'knows_how_patterns_match',
                  knows_how_patterns_match, None,
                  (),
                  (),
                  (contexts.variable('ans'),
                   pattern.pattern_literal('anonymous_matching'),
                   pattern.pattern_literal(3),))
  
  bc_rule.bc_rule('post_process_pattern_scope_1', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_1, None,
                  (pattern.pattern_literal(1),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_pattern_scope_2', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_2, None,
                  (pattern.pattern_literal(2),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_pattern_scope_3', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_3, None,
                  (pattern.pattern_literal(3),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_pattern_scope_4', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_4, None,
                  (pattern.pattern_literal(4),),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('post_process_pattern_scope_5', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_5, None,
                  (pattern.pattern_literal(5),),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('post_process_pattern_scope_6', This_rule_base, 'post_process_pattern_scope',
                  post_process_pattern_scope_6, None,
                  (pattern.pattern_literal(6),),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_rest_variable', This_rule_base, 'knows_rest_variable',
                  knows_rest_variable, None,
                  (),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('knows_rest_match', This_rule_base, 'knows_rest_match',
                  knows_rest_match, None,
                  (),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('post_process_rest_match_1', This_rule_base, 'post_process_rest_match',
                  post_process_rest_match_1, None,
                  (pattern.pattern_literal(1),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_rest_match_4_5', This_rule_base, 'post_process_rest_match',
                  post_process_rest_match_4_5, None,
                  (contexts.variable('ans'),),
                  (),
                  ())
  
  bc_rule.bc_rule('post_process_rest_match_correct', This_rule_base, 'post_process_rest_match',
                  post_process_rest_match_correct, None,
                  (contexts.variable('ans'),),
                  (),
                  ())
  
  bc_rule.bc_rule('knows_tuple_patterns', This_rule_base, 'knows_tuple_patterns',
                  knows_tuple_patterns, None,
                  (),
                  (),
                  (contexts.anonymous('_'),))


Krb_filename = '..\\pattern_matching.krb'
Krb_lineno_map = (
    ((14, 18), (41, 41)),
    ((20, 20), (43, 43)),
    ((21, 26), (44, 44)),
    ((39, 43), (47, 47)),
    ((45, 50), (49, 49)),
    ((63, 67), (52, 52)),
    ((69, 74), (54, 54)),
    ((87, 91), (57, 57)),
    ((93, 98), (59, 59)),
    ((99, 104), (60, 60)),
    ((117, 121), (63, 63)),
    ((123, 128), (65, 65)),
    ((129, 129), (66, 66)),
    ((130, 135), (67, 67)),
    ((136, 141), (68, 68)),
    ((142, 147), (69, 69)),
    ((148, 153), (70, 70)),
    ((166, 170), (73, 73)),
    ((172, 177), (75, 75)),
    ((178, 178), (76, 76)),
    ((179, 184), (77, 77)),
    ((197, 201), (80, 80)),
    ((203, 208), (82, 82)),
    ((209, 209), (83, 83)),
    ((210, 215), (84, 84)),
    ((228, 232), (87, 87)),
    ((234, 239), (89, 89)),
    ((240, 240), (90, 90)),
    ((241, 246), (91, 91)),
    ((259, 263), (94, 94)),
    ((265, 270), (96, 96)),
    ((271, 271), (97, 97)),
    ((272, 277), (98, 98)),
    ((278, 283), (99, 99)),
    ((296, 300), (102, 102)),
    ((302, 307), (104, 104)),
    ((320, 324), (108, 108)),
    ((326, 331), (110, 110)),
    ((344, 348), (113, 113)),
    ((350, 350), (115, 115)),
    ((363, 367), (118, 118)),
    ((369, 374), (120, 120)),
    ((375, 380), (121, 121)),
    ((381, 386), (122, 122)),
    ((399, 403), (125, 125)),
    ((405, 411), (127, 127)),
    ((424, 428), (130, 130)),
    ((430, 435), (132, 132)),
    ((436, 441), (133, 133)),
    ((454, 458), (136, 136)),
    ((460, 460), (138, 138)),
    ((461, 461), (139, 139)),
    ((462, 468), (140, 140)),
    ((481, 485), (143, 143)),
    ((487, 492), (145, 145)),
    ((493, 498), (146, 146)),
    ((511, 515), (149, 149)),
    ((517, 523), (151, 151)),
    ((524, 529), (152, 152)),
    ((530, 536), (153, 153)),
    ((549, 553), (156, 156)),
    ((555, 560), (158, 158)),
    ((561, 566), (159, 159)),
    ((567, 573), (160, 160)),
    ((586, 590), (163, 163)),
    ((592, 597), (165, 165)),
    ((598, 603), (166, 166)),
    ((604, 604), (167, 167)),
    ((605, 610), (168, 168)),
    ((623, 627), (171, 171)),
    ((629, 634), (173, 173)),
    ((635, 635), (174, 174)),
    ((636, 641), (175, 175)),
    ((654, 658), (178, 178)),
    ((672, 676), (181, 181)),
    ((678, 683), (183, 183)),
    ((684, 689), (184, 184)),
    ((690, 690), (185, 185)),
    ((691, 696), (186, 186)),
    ((709, 713), (189, 189)),
    ((715, 720), (191, 191)),
    ((721, 721), (192, 192)),
    ((722, 727), (193, 193)),
    ((740, 744), (196, 196)),
    ((746, 751), (198, 198)),
    ((752, 757), (199, 199)),
    ((758, 758), (200, 200)),
    ((759, 764), (201, 201)),
    ((777, 781), (204, 204)),
    ((783, 788), (206, 206)),
    ((789, 794), (207, 207)),
    ((807, 811), (210, 210)),
    ((813, 818), (212, 212)),
    ((819, 824), (213, 213)),
    ((837, 841), (216, 216)),
    ((843, 843), (218, 218)),
    ((844, 849), (219, 219)),
    ((862, 866), (222, 222)),
    ((868, 868), (224, 224)),
    ((869, 874), (225, 225)),
    ((875, 875), (226, 226)),
    ((876, 881), (227, 227)),
    ((894, 898), (230, 230)),
    ((900, 900), (232, 232)),
    ((913, 917), (235, 235)),
    ((919, 924), (237, 237)),
    ((925, 930), (238, 238)),
)
