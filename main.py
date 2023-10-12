def build_array_from(permutation):
    array = [0] * len(permutation)

    for val, num in enumerate(permutation):
        array[num] = permutation[val]

    return array

if __name__ == '__main__':
    build_array_from('PyCharm')
