import types
class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.current_value = 0
        self.result_list = []

    def __iter__(self):
        self.current_value -= 1
        for list in self.list_of_lists:
            for item in list:
                self.result_list.append(item)
        return self

    def __next__(self):
        self.current_value += 1
        if self.current_value < len(self.result_list):
            return self.result_list[self.current_value]
        else:
            raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
#     list_of_lists_1 = [ ['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None] ]
#     iterr = FlatIterator(list_of_lists_1)
#     for item in iterr:
#         print(item)

