import nose
import combinators

def main():
    nose.main()

def test_enumerate_first():
    # n=1
    #     depth=1 [0]
    #     depth=2 [[0, 0]]
    #     depth=3 [[0, [0, 0]], [[0, 0], 0], [[0, 0], [0, 0]]]
    #     ...
    # n=2
    #     depth=1 [0, 1]
    #     depth=2 [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     ...
    # n=3
    #     depth=1 [0, 1, 2]
    #     depth=2 [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    #     ...
    # n=4
    #     depth=1 [0, 1, 2, 3]
    #     depth=2 [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
    #     ...

    combinator_generator = combinators.generator()

    nose.tools.eq_(combinator_generator.next(),  {'arguments': 1, 'rewrite': 0})

    nose.tools.eq_(combinator_generator.next(),  {'arguments': 1, 'rewrite': [0, 0]})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 2, 'rewrite': 0})

    nose.tools.eq_(combinator_generator.next(),  {'arguments': 1, 'rewrite': [0, [0, 0]]})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 2, 'rewrite': 1})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 3, 'rewrite': 0})

    nose.tools.eq_(combinator_generator.next(),  {'arguments': 1, 'rewrite': [[0, 0], 0]})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 2, 'rewrite': [0, 0]})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 3, 'rewrite': 1})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 4, 'rewrite': 0})

    nose.tools.eq_(combinator_generator.next(),  {'arguments': 1, 'rewrite': [[0, 0], [0, 0]]})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 2, 'rewrite': [0, 1]})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 3, 'rewrite': 2})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 4, 'rewrite': 1})
    nose.tools.eq_(combinator_generator.next(),  {'arguments': 5, 'rewrite': 0})

    # ...

def test_enumerate_iks():
    nose.tools.ok_({'arguments': 1, 'rewrite': 0} in combinators.generator())
    nose.tools.ok_({'arguments': 2, 'rewrite': 0} in combinators.generator())
    nose.tools.ok_({'arguments': 3, 'rewrite': [[0, 2], [1, 2]]} in combinators.generator())

if __name__ == '__main__':
    main()
