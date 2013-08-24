def generator():
    generators = []
    n = 0
    while True:
        n += 1
        generators.append(applications(n))
        for generator in generators:
            yield generator.next()

def applications(arguments, depth=None):
    if depth == None:
        depth = 1
        for argument in range(arguments):
            yield {'arguments': arguments, 'rewrite': argument}
        while True:
            depth += 1
            for a in applications(arguments, depth=depth-1):
                for b in applications(arguments, depth=depth-1):
                    yield {'arguments': arguments, 'rewrite': [a, b]}
    if depth == 0:
        for argument in range(arguments):
            yield argument
    if depth > 0:
        for argument in range(arguments):
            yield argument
        for a in applications(arguments=arguments, depth=depth-1):
            for b in applications(arguments=arguments, depth=depth-1):
                yield [a, b]
