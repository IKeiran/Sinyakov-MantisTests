from sys import maxsize


def randomize_str(attr, max_len=5):
    import random, string
    symbols = string.ascii_letters + string.digits + " " * 10+string.punctuation
    return attr + "".join(random.choice(symbols) for i in range(max_len)).rstrip().lstrip()


class Project:
    def __init__(self, name, status, view_status, description, inherit_global_categories=None, id=None):
        self.id = id
        self.name = name
        self.status = status
        self.inherit_global_categories = inherit_global_categories
        self.view_status = view_status
        self.description = description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and (self.name == other.name) and (self.status == other.status) \
            and (self.view_status == other.view_status) and (self.description == other.description)

    def __repr__(self):
        return 'id: %s; name: %s; status = %s; visible_status = %s, desc = %s' % (self.id, self.name, self.status,
                                                                                  self.view_status, self.description)

    @classmethod
    def generate_random(cls):
        import random
        available_status = ('development', 'release', 'stable', 'obsolete')
        view_status = ('public', 'private')
        return cls(name=randomize_str('project'),
                   status=random.choice(available_status),
                   inherit_global_categories=random.randrange(2) == 1,
                   view_status=random.choice(view_status),
                   description=randomize_str('description', max_len=50))