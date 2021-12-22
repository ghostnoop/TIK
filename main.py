def swap_element(my_list, index):
    my_list.insert(0, my_list.pop(index)) #0 porque es la primera pos

def move2front(strng, configuration):
    sequence = []
    total_cost = 0
    for char in strng:
        unit_cost = 0
        for i in configuration:
            if (configuration.index(char) == i):
                unit_cost = i + 1
                swap_element(configuration, configuration.index(char))
                total_cost += unit_cost
                sequence.append([configuration[:], unit_cost])
                break

    print("Costo total : " + str(total_cost) + "\n")
    return sequence

print("======  a)  =======\n")
configuration = [0, 1, 2, 3, 4]
request_list = [0, 1, 2, 3, 4,0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
move2front(request_list, configuration)

