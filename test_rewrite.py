import nose
import rewrite

def main():
    nose.main()

def test_reduce():
    i = {'arguments': 1, 'rewrite': 0}
    k = {'arguments': 2, 'rewrite': 0}
    s = {'arguments': 3, 'rewrite': [[0, 2], [1, 2]]}
    c = {'arguments': 3, 'rewrite': [[0, 2], 1]}
    b = {'arguments': 3, 'rewrite': [0, [1, 2]]}

    va = {'arguments': 1000+0, 'rewrite': 0}
    vb = {'arguments': 1000+1, 'rewrite': 0}
    vc = {'arguments': 1000+2, 'rewrite': 0}
    vd = {'arguments': 1000+3, 'rewrite': 0}
    ve = {'arguments': 1000+4, 'rewrite': 0}
    vf = {'arguments': 1000+5, 'rewrite': 0}
    vg = {'arguments': 1000+6, 'rewrite': 0}

    rewritten = rewrite.reduce(i)
    nose.tools.eq_(rewritten, i)

    rewritten = rewrite.reduce([i, k])
    nose.tools.eq_(rewritten, k)

    rewritten = rewrite.reduce([[k, va], vb])
    nose.tools.eq_(rewritten, va)

    rewritten = rewrite.reduce([[[s, va], vb], vc])
    nose.tools.eq_(rewritten, [[va, vc], [vb, vc]])

    rewritten = rewrite.reduce([[[s, k], k], va])
    nose.tools.eq_(rewritten, va)

    rewritten = rewrite.reduce([[[[s, [k, [s, i]]], [[s, [k, k]], i]], va], vb])
    nose.tools.eq_(rewritten, [vb, va])

    rewritten = rewrite.reduce([[[c, i], va], vb])
    nose.tools.eq_(rewritten, [vb, va])

    rewritten = rewrite.reduce([[[[s, k], k], va], [[[s, k], k], vb]])
    nose.tools.eq_(rewritten, [va, vb])

    rewritten = rewrite.reduce([[[s, i], i], va])
    nose.tools.eq_(rewritten, [va, va])

if __name__ == '__main__':
    main()
