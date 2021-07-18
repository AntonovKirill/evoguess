class Variables:
    slug = 'variables'
    name = 'Variables'

    def __init__(self, _list):
        self._list = _list
        self.length = len(self._list)

    def __copy__(self):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.variables())

    def _to_str(self):
        variables, strings, i, j = self.variables(), [], 0, 1
        while i < len(variables):
            if j == len(variables) or variables[j] - variables[i] != j - i:
                if j - i > 2:
                    strings.append(f'{variables[i]}..{variables[j - 1]}')
                else:
                    strings.extend(f'{variables[k]}' for k in range(i, j))
                i, j = j, j + 1
            else:
                j += 1
        return ' '.join(strings), len(variables)

    def __str__(self):
        return '[%s](%d)' % self._to_str()

    def __repr__(self):
        return self._to_str()[0]

    def __iter__(self):
        return self.variables().__iter__()

    def __hash__(self):
        return hash(tuple(self.variables()))

    def __contains__(self, item):
        return item in self.variables()

    def __info__(self):
        return {
            'slug': self.slug,
            'name': self.name,
        }


__all__ = [
    'Variables'
]
