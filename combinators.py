import itertools

def generator():
    tree_generator = binary_trees()
    tree_list = []
    for n in itertools.count(1):
        tree_list.append(tree_generator.next())
        for i in range(n):
            for application in applications(arguments=n-i, tree=tree_list[i]):
                yield {'arguments': n-i, 'rewrite': application}

def applications(arguments=0, tree=None):
    if tree is None:
        for argument in range(arguments):
            yield argument
    else:
        for left, right in itertools.product(applications(arguments=arguments, tree=tree[0]), applications(arguments=arguments, tree=tree[1])):
            yield [left, right]

def binary_trees(leaves=None):
    if leaves is None:
        for leaves in itertools.count(1):
            for tree in binary_trees(leaves=leaves):
                yield tree
    if leaves == 1:
        yield None
    else:
        for i in range(1, leaves):
            for left, right in itertools.product(binary_trees(leaves=i), binary_trees(leaves=leaves-i)):
                yield [left, right]
