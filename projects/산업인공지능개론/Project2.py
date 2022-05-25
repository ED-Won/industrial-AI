!pip install durable_rules

from durable.lang import *

with ruleset('animal'):
    @when_all(c.first << (m.predicate=='eat') & (m.object == 'flies'),
              (m.predicate=='lives') & (m.object=='water') & (m.subject==c.first.subject))
    def frog(c):
        c.assert_fact({'subject':c.first.subject,'precate': 'is', 'object': 'frog'})
        
    @when_all(c.first << (m.predicate=='eats') & (m.object=='flies'),
                  (m.predicate=='lives') & (m.object=='land') & (m.subject==c.first.subject))
    def chameleon(c):
        c.assert_fact({'subject': c.first.subject, 'preicate': 'is', 'object':'chameleon' })
        
    @when_all((m.predicate == 'eats') & (m.object==worms))
    def bird(c):
        c.assert_fact({'subject': c.m.subject, 'precate':'is','object':'bird'})
        
    @when_all((m.predicate== 'is') & (m.object=='frog'))
    def green(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object':'green'})
        
    @when_all((m.predicate == 'is') & (m.object == 'chameleon'))
    def grey(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'grey'})
        
    @when_all((m.precate == "is") & (m.object == 'bird'))
    
    def black(c):
        c.assert_fact({'subject':c.m.subject, 'predicate': 'is', 'object': 'black'})
        
    @when_all(+m.subject)
    def outfut(c):
        print('Fact: {0} {1} {2}'. format(c.m.subject, c.m.predicate, c.m.object))
        
assert_fact('animal',{'subject':'kermit', 'predicate': 'eats', 'object': 'flies'})
assert_fact('animal',{'subject':'kermit', 'predicate': 'lives', 'object': 'water'})
assert_fact('animal',{'subject':'Greedy', 'predicate': 'eats', 'object': 'flies'})
assert_fact('animal',{'subject':'Greedy', 'predicate': 'lives','object': 'land'})
assert_fact('animal',{'subject':'Tweety', 'predicate': 'eats','object': 'worms' })