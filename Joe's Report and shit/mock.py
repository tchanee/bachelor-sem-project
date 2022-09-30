### MOCK INTERVIEW - 2 problems
###
###


#PROBLEM 1:

# building a compiler (for packages)
# if package2 depends on package1, must build p1 before p2
# P1
#   P2
#   P3
#
#   dont mind the circular corner case

class Package:

    def __init__(self, name, dependency_list):
        #assert
        self.name = name
        self.dependencies = dependency_list # if its necessary to the class

    def build(self):
        results = []
        for pkg in self.dependencies:
            results.extend(pkg.build())
        results.append(self.name)
        return results # building it

def nodependecy_case():
    my_pkg = Package("simple", [])
    res = my_pkg.build()
    if res == ['simple']:
        print("success")
    else:
        print("failure")


def few_dependencies_returns_correct_list():
    my_dependencies = [
        Package("dep1", []),
        Package("dep2", []),
        Package("dep3", [])
        ]
    my_pkg = Package("simple", my_dependencies)
    res = my_pkg.build()
    if res == ["dep1", "dep2", "dep3", "simple"]:
        print("success")
    else:
        print("failure")

def dependency_within_dependency_works():
    my_dependencies = [
        Package("dep1", [ Package("dep4", []) ]),
        Package("dep2", [ Package("dep5", [Package("dep6", [])]) ]),
        Package("dep3", [])
        ]
    my_pkg = Package("simple", my_dependencies)
    res = my_pkg.build()
    if res == ["dep4", "dep1", "dep6", "dep5", "dep2", "dep3", "simple"]:
        print("success")
    else:
        print("failure")

# p1 depends on p2, p2 depends on p3,

if __name__ == '__main__':
    #nodependecy_case()
    #few_dependencies_returns_correct_list()
    dependency_within_dependency_works()


    value1= 1
    m = {"key1": value1, "key2" : 2  }
    print(m)

