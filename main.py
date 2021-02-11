from src import MarkovAlgorithm

a = MarkovAlgorithm(
    '''
a -> b
b -> c
c -> E
'''
)
# print(a.scheme, a.sigma)
# print(a)
print(a.apply('a', True))
