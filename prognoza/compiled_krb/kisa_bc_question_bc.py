# kisa_bc_question_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def kabanicu(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.kabanicu: got unexpected plan from when clause 1"
            with engine.prove('questions', 'puse_vjetar', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "kisa_bc_question.kabanicu: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def kisobran(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.kisobran: got unexpected plan from when clause 1"
            with engine.prove('questions', 'puse_vjetar', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "kisa_bc_question.kisobran: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nista(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.nista: got unexpected plan from when clause 1"
            with engine.prove('questions', 'puse_vjetar', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "kisa_bc_question.nista: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def vjetrovka(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'pada_kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.vjetrovka: got unexpected plan from when clause 1"
            with engine.prove('questions', 'puse_vjetar', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "kisa_bc_question.vjetrovka: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cizme(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'katastrofa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.cizme: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def maska(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'katastrofa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.maska: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nistaDodatno(rule, arg_patterns, arg_context):
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
        with engine.prove('questions', 'katastrofa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc_question.nistaDodatno: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('kisa_bc_question')
  
  bc_rule.bc_rule('kabanicu', This_rule_base, 'ponijeti',
                  kabanicu, None,
                  (pattern.pattern_literal('kabanicu'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('kisobran', This_rule_base, 'ponijeti',
                  kisobran, None,
                  (pattern.pattern_literal('kisobran'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('nista', This_rule_base, 'ponijeti',
                  nista, None,
                  (pattern.pattern_literal('nista'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('vjetrovka', This_rule_base, 'ponijeti',
                  vjetrovka, None,
                  (pattern.pattern_literal('vjetrovku'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('cizme', This_rule_base, 'dodatno',
                  cizme, None,
                  (pattern.pattern_literal('cizme'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('maska', This_rule_base, 'dodatno',
                  maska, None,
                  (pattern.pattern_literal('maska'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('nistaDodatno', This_rule_base, 'dodatno',
                  nistaDodatno, None,
                  (pattern.pattern_literal('nistaDodatno'),),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '..\\kisa_bc_question.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 31), (5, 5)),
    ((44, 48), (7, 7)),
    ((50, 55), (9, 9)),
    ((56, 61), (10, 10)),
    ((74, 78), (12, 12)),
    ((80, 85), (14, 14)),
    ((86, 91), (15, 15)),
    ((104, 108), (17, 17)),
    ((110, 115), (19, 19)),
    ((116, 121), (20, 20)),
    ((134, 138), (22, 22)),
    ((140, 145), (24, 24)),
    ((146, 146), (25, 25)),
    ((159, 163), (27, 27)),
    ((165, 170), (29, 29)),
    ((171, 171), (30, 30)),
    ((184, 188), (32, 32)),
    ((190, 195), (34, 34)),
    ((196, 196), (35, 35)),
)
