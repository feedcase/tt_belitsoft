def second_test_task(list_of_values):
    set_of_values = set()
    for value in list_of_values:
        if value in set_of_values:
            return value
        else:
            set_of_values.add(value)
    return 'No repeating values'


if __name__ == '__main__':
    print(second_test_task(['asdf', 'a', 'b', 'sdf', 'sasdf', 'asdf', 'a']))
    print(second_test_task([0,1,2,3,5,112,9918,1287,256,9,23,112,0]))
