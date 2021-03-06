from random import randint
import matplotlib.pyplot as plt
import imageio


def bubble_sort(array, lenght):
    swap_happened = True
    array_numbers = []
    while swap_happened:
        swap_happened = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                array_numbers.extend(array)
                swap_happened = True

    result = [array_numbers[i:i + lenght] for i in range(0, len(array_numbers), lenght)]
    return result


def generate_numbers(lenght):
    array = [randint(0, lenght) for i in range(lenght)]
    return array


def show(list_numbers, lenght):
    for index in range(len(list_numbers)):
        plt.cla()
        plt.title("Bubble Sort swap = " + str(index))
        plt.bar(range(lenght), list_numbers[index])
        plt.pause(0.0001)
        plt.savefig('img' + str(index) + '.png')
    plt.show()

def build_gif(list_numbers):
    with imageio.get_writer('bubble_sort.gif', mode='I') as writer:
        for filename in range(len(list_numbers)):
            image = imageio.imread(f'img{filename}.png')
            writer.append_data(image)


if __name__ == '__main__':
    def main(lenght):
        array = generate_numbers(lenght)
        list_numbers = bubble_sort(array, lenght)
        show(list_numbers, lenght)
        build_gif(list_numbers)

    main(25)
