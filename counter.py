class Counter():
    data = {}

    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            return 0

    def __setitem__(self, key, value):
        self.data[key] = value
