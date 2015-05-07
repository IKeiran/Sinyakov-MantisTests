def randomize_str(attr, max_len=5):
    import random, string
    symbols = string.ascii_letters + string.digits +" " * 10+ string.punctuation
    return attr + "".join(random.choice(symbols) for i in range(max_len)).rstrip().lstrip()

class Project:
    def __init__(self, name, status, inherit_global_categiries, view_status, description):
        self.name = name
        self.status = status
        self.inherit_global_categiries = inherit_global_categiries
        self.view_status = view_status
        self.description = description

    @classmethod
    def generate_random(cls):
        import random
        return cls(name=randomize_str('project'),
                   status=random.randrange(4),
                   inherit_global_categiries=random.randrange(2) == 1,
                   view_status=random.randrange(2),
                   description=randomize_str('description', max_len=50))
