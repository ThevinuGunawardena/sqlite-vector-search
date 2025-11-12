import math
def cosine_sim(a, b): return sum(x*y for x, y in zip(a, b)) / (math.sqrt(sum(x**2 for x in a)) * math.sqrt(sum(y**2 for y in b)))
