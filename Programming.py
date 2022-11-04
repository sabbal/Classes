class Programming:

    def __init__(self, datatypes, is_functional, operators, age, owner):
        self.datatypes = datatypes
        self.is_functional = is_functional
        self.operators = operators
        self.age = age
        self.owner = owner

    def is_web_based_supportive(self):
        return not self.is_functional

    def print_owner_name(self):
        print(self.owner)

    def get_number_of_operators(self):
        return self.operators

    def is_map_supported(self):
        if ('map' or 'Dictionary') in self.datatypes:
            return True
        else:
            return False


batch_scripting = Programming(['String', 'Number'], True, 70, 50, 'Dennis Riche')
c = Programming(['String', 'Number', 'Array'], False, 70, 50, 'Dennis Riche')
java = Programming(['String', 'Number', 'List', 'Set', 'Map'], False, 70, 27, 'James Gosling')
python = Programming(['String', 'Number', 'List', 'Tuple', 'Dictionary'], False, 7, 42, 'Gudio Van Rasam')


print(batch_scripting.is_map_supported())
print(c.get_number_of_operators())
print(java.owner)
print(python.is_web_based_supportive())


