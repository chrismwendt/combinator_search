import pprint
import copy
import combinators
import rewrite

a = {'arguments': 10000, 'rewrite': 0}
b = {'arguments': 10001, 'rewrite': 0}
c = {'arguments': 10002, 'rewrite': 0}

def main():
    print bases().next()

def bases():
    combinator_generator = combinators.generator()
    candidate_list = []
    pair_list = []
    while True:
        candidate = {
            'combinator': combinator_generator.next(),
            'program_template_generator': combinators.binary_trees(),
            'K': None,
            'S': None
        }
        candidate_list.append(candidate);
        for candidate in candidate_list:
            program = template(candidate['program_template_generator'].next(), candidate['combinator'])
            global a, b, c
            program_k = [[program, a], b]
            program_s = [[[copy.deepcopy(program), a], b], c]
            pair_list.append({
                    'candidate': candidate,
                    'K': {
                        'program': program_k,
                        'rewritten': None,
                        'steps': rewrite.rewrite(copy.deepcopy(program_k)),
                        'done': False
                    },
                    'S': {
                        'program': program_s,
                        'rewritten': None,
                        'steps': rewrite.rewrite(copy.deepcopy(program_s)),
                        'done': False
                    }
                }
            )
        for pair in pair_list:
            if not pair['K']['done']:
                try:
                    pair['K']['rewritten'] = pair['K']['steps'].next()['expression']
                except StopIteration:
                    pair['K']['done'] = True
                    for base in process(pair, 'K'):
                        yield base
            if not pair['S']['done']:
                try:
                    pair['S']['rewritten'] = pair['S']['steps'].next()['expression']
                except StopIteration:
                    pair['S']['done'] = True
                    for base in process(pair, 'S'):
                        yield base
        before = len(pair_list)
        pair_list = filter(lambda pair: [pair['K']['done'], pair['S']['done']] != [True, True], pair_list)
        after = len(pair_list)
        print before, '->', after

def process(pair, match):
    if match == 'K':
        if not pair['candidate']['K'] and pair[match]['rewritten'] == a:
            print pair[match]['program']
            print pair['candidate']['combinator']
            pair['candidate']['K'] = pair['K']['program']
    if match == 'S':
        if not pair['candidate']['S'] and pair[match]['rewritten'] == [[a, c], [b, c]]:
            print pair[match]['program']
            print pair['candidate']['combinator']
            pair['candidate']['S'] = pair['S']['program']
    if pair['candidate']['K'] is not None and pair['candidate']['S'] is not None:
        yield candidate

def template(t, c):
    if t == None:
        return c
    return [template(i, c) for i in t]

if __name__ == '__main__':
    main()
