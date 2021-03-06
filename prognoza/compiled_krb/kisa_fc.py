# kisa_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def kabanicu(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'kisa', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'vjetar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponijeti',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def kisobran(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'kisa', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'vjetar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponijeti',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def vjetrovka(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'kisa', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'vjetar', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponijeti',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def nista(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('vrijeme', 'vjetar', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('vrijeme', 'kisa', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('vrijeme', 'ponijeti',
                           (rule.pattern(0).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('kisa')
  
  fc_rule.fc_rule('kabanicu', This_rule_base, kabanicu,
    (('vrijeme', 'kisa',
      (pattern.pattern_literal(True),),
      False),
     ('vrijeme', 'vjetar',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('kabanicu'),))
  
  fc_rule.fc_rule('kisobran', This_rule_base, kisobran,
    (('vrijeme', 'kisa',
      (pattern.pattern_literal(True),),
      False),
     ('vrijeme', 'vjetar',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('kisobran'),))
  
  fc_rule.fc_rule('vjetrovka', This_rule_base, vjetrovka,
    (('vrijeme', 'kisa',
      (pattern.pattern_literal(False),),
      False),
     ('vrijeme', 'vjetar',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal('vjetrovku'),))
  
  fc_rule.fc_rule('nista', This_rule_base, nista,
    (('vrijeme', 'vjetar',
      (pattern.pattern_literal(False),),
      False),
     ('vrijeme', 'kisa',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal('nista'),))


Krb_filename = '..\\kisa.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 21), (4, 4)),
    ((22, 23), (6, 6)),
    ((32, 36), (9, 9)),
    ((37, 41), (10, 10)),
    ((42, 43), (12, 12)),
    ((52, 56), (15, 15)),
    ((57, 61), (16, 16)),
    ((62, 63), (18, 18)),
    ((72, 76), (21, 21)),
    ((77, 81), (22, 22)),
    ((82, 83), (24, 24)),
)
