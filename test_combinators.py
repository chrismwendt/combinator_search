import nose
import itertools
import combinators

def main():
    nose.main()

def take(iterable, n):
    return list(itertools.islice(iterable, n))

def test_binary_trees():
    nose.tools.eq_(list(combinators.binary_trees(leaves=1)), [
            None
        ]
    )
    nose.tools.eq_(list(combinators.binary_trees(leaves=2)), [
            [None, None]
        ]
    )
    nose.tools.eq_(list(combinators.binary_trees(leaves=3)), [
            [None, [None, None]],
            [[None, None], None]
        ]
    )
    nose.tools.eq_(list(combinators.binary_trees(leaves=4)), [
            [None, [None, [None, None]]],
            [None, [[None, None], None]],
            [[None, None], [None, None]],
            [[None, [None, None]], None],
            [[[None, None], None], None]
        ]
    )

def test_applications_for_binary_tree():
    nose.tools.eq_(list(combinators.applications(arguments=1, tree=None)), [
            0
        ]
    )
    nose.tools.eq_(list(combinators.applications(arguments=1, tree=[None, None])), [
            [0, 0]
        ]
    )
    nose.tools.eq_(list(combinators.applications(arguments=1, tree=[None, [None, None]])), [
            [0, [0, 0]]
        ]
    )
    nose.tools.eq_(list(combinators.applications(arguments=2, tree=None)), [
            0,
            1
        ]
    )
    nose.tools.eq_(list(combinators.applications(arguments=2, tree=[None, None])), [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
        ]
    )
    nose.tools.ok_(0 in list(combinators.applications(arguments=1, tree=None)))
    nose.tools.ok_(0 in list(combinators.applications(arguments=2, tree=None)))
    nose.tools.ok_([[0, 2], [1, 2]] in list(combinators.applications(arguments=3, tree=[[None, None], [None, None]])))

def test_generator():
    # arguments=1
    #     leaves=1 [0]
    #     leaves=2 [[0, 0]]
    #     leaves=3 [[0, [0, 0]], [[0, 0], 0]]
    #     leaves=4 [[0, [0, [0, 0]]], [0, [[0, 0], 0]], [[0, 0], [0, 0]], [[0, [0, 0]], 0], [[[0, 0], 0], 0]]
    #     ...
    # arguments=2
    #     leaves=1 [0, 1]
    #     leaves=2 [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     leaves=3 [[0, [0, 0]], [0, [0, 1]], [0, [1, 0]], [0, [1, 1]], [1, [0, 0]], [1, [0, 1]], [1, [1, 0]], [1, [1, 1]], [[0, 0], 0], [[0, 0], 1], ...]
    #     ...
    # arguments=3
    #     leaves=1 [0, 1, 2]
    #     leaves=2 [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    #     ...

    combinator_generator = combinators.generator()

    nose.tools.eq_(combinator_generator.next(), {'arguments': 1, 'rewrite': 0})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': 0})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': 1})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 1, 'rewrite': [0, 0]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': 0})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': 1})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': 2})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [0, 0]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [0, 1]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [1, 0]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [1, 1]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 1, 'rewrite': [0, [0, 0]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 4, 'rewrite': 0})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 4, 'rewrite': 1})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 4, 'rewrite': 2})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 4, 'rewrite': 3})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [0, 0]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [0, 1]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [0, 2]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [1, 0]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [1, 1]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [1, 2]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [2, 0]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [2, 1]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 3, 'rewrite': [2, 2]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [0, [0, 0]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [0, [0, 1]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [0, [1, 0]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [0, [1, 1]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [1, [0, 0]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [1, [0, 1]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [1, [1, 0]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 2, 'rewrite': [1, [1, 1]]})
    nose.tools.eq_(combinator_generator.next(), {'arguments': 1, 'rewrite': [[0, 0], 0]})

    nose.tools.ok_({'arguments': 1, 'rewrite': 0} in combinators.generator())
    nose.tools.ok_({'arguments': 2, 'rewrite': 0} in combinators.generator())
    nose.tools.ok_({'arguments': 3, 'rewrite': [[0, 2], [1, 2]]} in combinators.generator())

    # ...

if __name__ == '__main__':
    main()
