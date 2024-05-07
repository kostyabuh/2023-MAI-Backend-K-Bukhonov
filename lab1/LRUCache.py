class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: str) -> str:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            print(self.cache[key])
            return self.cache[key]
        return ""

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            del_key = self.order.pop(0)
            del self.cache[del_key]
        self.cache[key] = value
        self.order.append(key)

    def rem(self, key: str) -> None:
        if key in self.cache:
            self.order.remove(key)
            del self.cache[key]

# Пример использования:
cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')

cache.get('Jesse')  # вернёт 'James'
cache.rem('Walter')
cache.get('Walter')  # вернёт ''
