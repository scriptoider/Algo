import functools

class Sequence:
    
    @functools.lru_cache()
    def fibonacci(self, n1):
        if n1 in [0,1]:
            return n1
        return self.fibonacci(n1-1) + self.fibonacci(n1-2)
