import aoc_18 as target


def test_add_to_descendant():
    assert False


def test_add_to_descendant():
    examples = []

    for tree, value_to_add, leftmost in examples:
        assert target.add_to_descendant(tree, value_to_add, leftmost) == tree


def test_traverse_tree():
    examples = [([[[[[9, 8], 1], 2], 3], 4], [9, 8], '0000'),
                ([7, [6, [5, [4, [3, 2]]]]], [3, 2], '1111'),
                ([[6, [5, [4, [3, 2]]]], 1], [3, 2], '0111'),
                ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [7, 3], '0111'),
                ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [3, 2], '1111')
                ]
    for tree, node, node_position in examples:
        assert target.traverse_tree(tree, node_position) == node


def test_reduce():
    examples = [
        ([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]], [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]),
        ([[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]],
         [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]),
        ([[[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]],
          [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]],
         [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]]),
        ([[[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]],
          [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]]],
         [[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [[[7, 7], [8, 8]], [[7, 7], [8, 7]]]]),
        ([[[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [[[7, 7], [8, 8]], [[7, 7], [8, 7]]]], [7, [5, [[3, 8], [1, 4]]]]],
         [[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [[[6, 8], [0, 8]], [[9, 9], [9, 0]]]])
    ]
    for unreduced, reduced in examples:
        assert target.reduce(unreduced) == reduced


def test_explode():
    examples = [
        ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4], '0000'),
        ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]], '1111'),
        ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3], '0111'),
        ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], '0111'),
        ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [7, 0]]]], '1111')
    ]
    for unexploded, exploded, node_position in examples:
        assert target.explode(unexploded, node_position) == exploded


def test_ancestor_position():
    examples = [
        ('0000', False, '0001'),
        ('0000', True, ''),
        ('1111', False, ''),
        ('1111', True, '1110'),
        ('0111', False, '1'),
        ('0111', True, '0110'),
        ('0111', False, '1'),
        ('0111', True, '0110'),
        ('1111', False, ''),
        ('1111', True, '0001')
    ]

    for position, left, ancester_position in examples:
        target.ancestor_position(position, left)


def test_split():
    examples = [
        ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], '010'),
        ([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], '0111'),
        ([[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]], '')
    ]
    for i in range(len(examples) - 1):
        assert target.split(examples[i][0], examples[i][1]) == examples[i + 1][0]


def test_find_first_explosive():
    examples = [
        ([[[[[9, 8], 1], 2], 3], 4], '0000'),
        ([7, [6, [5, [4, [3, 2]]]]], '1111'),
        ([[6, [5, [4, [3, 2]]]], 1], '0111'),
        ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], '0111'),
        ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], '1111')
    ]
    for unexploded, node_position in examples:
        assert target.find_first_explosive(unexploded, '') == node_position


def test_sum_list_of_numbers():
    examples = [
        ([
             [1, 1],
             [2, 2],
             [3, 3],
             [4, 4]
         ], [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]),
        ([
             [1, 1],
             [2, 2],
             [3, 3],
             [4, 4],
             [5, 5]
         ], [[[[3, 0], [5, 3]], [4, 4]], [5, 5]]),

        ([
             [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
             [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
             [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
             [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
             [7, [5, [[3, 8], [1, 4]]]],
             [[2, [2, 2]], [8, [8, 1]]],
             [2, 9],
             [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
             [[[5, [7, 4]], 7], 1],
             [[[[4, 2], 2], 6], [8, 7]],
         ], [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])
    ]

    for list_of_numbers, result in examples:
        assert target.sum_list_of_numbers(list_of_numbers) == result


def test_get_magnitude():
    examples = [
        ([[1, 2], [[3, 4], 5]], 143),
        ([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], 1384),
        ([[[[1, 1], [2, 2]], [3, 3]], [4, 4]], 445),
        ([[[[3, 0], [5, 3]], [4, 4]], [5, 5]], 791),
        ([[[[5, 0], [7, 4]], [5, 5]], [6, 6]], 1137.),
        ([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]], 3488)]
    for tree, magnitude in examples:
        assert target.get_magnitude(tree) == magnitude


def test_biggest_sum_in_list_of_numbers():
    list_of_numbers = [
    [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
    [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
    [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
    [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
    [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
    [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
    [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
    [[9, 3], [[9, 9], [6, [4, 9]]]],
    [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
    [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]]]
    assert target.biggest_sum_in_list_of_numbers(list_of_numbers)==3993

