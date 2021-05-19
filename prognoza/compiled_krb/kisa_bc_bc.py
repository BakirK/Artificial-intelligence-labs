# kisa_bc_bc.py

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
        with engine.prove('vrijeme', 'kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc.kabanicu: got unexpected plan from when clause 1"
            with engine.prove('vrijeme', 'vjetar', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "kisa_bc.kabanicu: got unexpected plan from when clause 2"
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
        with engine.prove('vrijeme', 'kisa', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "kisa_bc.kisobran: got unexpected plan from when clause 1"
            if context.lookup_data('vjetar') in (False,):
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
        if context.lookup_data('kisa') in (False,):
          if context.lookup_data('vjetar') in (False,):
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
        if context.lookup_data('vjetar') in (False,):
          with engine.prove('vrijeme', 'vjetar', context,
                            (rule.pattern(0),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "kisa_bc.vjetrovka: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('kisa_bc')
  
  bc_rule.bc_rule('kabanicu', This_rule_base, 'ponijeti',
                  kabanicu, None,
                  (contexts.variable('kisa'),
                   contexts.variable('vjetar'),
                   pattern.pattern_literal('kabanicu'),),
                  (),
                  (contexts.variable('kisa'),
                   contexts.variable('vjetar'),))
  
  bc_rule.bc_rule('kisobran', This_rule_base, 'ponijeti',
                  kisobran, None,
                  (contexts.variable('kisa'),
                   contexts.variable('vjetar'),
                   pattern.pattern_literal('kisobran'),),
                  (),
                  (contexts.variable('kisa'),))
  
  bc_rule.bc_rule('nista', This_rule_base, 'ponijeti',
                  nista, None,
                  (contexts.variable('kisa'),
                   contexts.variable('vjetar'),
                   pattern.pattern_literal('nista'),),
                  (),
                  ())
  
  bc_rule.bc_rule('vjetrovka', This_rule_base, 'ponijeti',
                  vjetrovka, None,
                  (contexts.variable('kisa'),
                   contexts.variable('vjetar'),
                   pattern.pattern_literal('vjetrovku'),),
                  (),
                  (contexts.variable('vjetar'),))


Krb_filename = '..\\kisa_bc.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 31), (5, 5)),
    ((44, 48), (7, 7)),
    ((50, 55), (9, 9)),
    ((56, 56), (10, 10)),
    ((69, 73), (12, 12)),
    ((75, 75), (14, 14)),
    ((76, 76), (15, 15)),
    ((89, 93), (17, 17)),
    ((95, 95), (19, 19)),
    ((96, 101), (20, 20)),
)
