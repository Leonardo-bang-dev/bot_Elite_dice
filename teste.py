import random


def dice(command):
    hits = 0
    fail = 0
    repeat = 0

    command = command.replace('!roll', '')
    command = command.split('d')
    command[0] = int(command[0])
    command[1] = int(command[1])

    while command[0] != 0:
        repeat = 0
        for a in range(0, command[0]):
            random_value = random.randint(1, command[1])
            if random_value % 2 == 0:
                hits += 1
                if random_value == 6:
                    repeat += 1
            else:
                fail += 1
                if random_value == 1:
                    hits -= 1
            print(f'Acertos: {hits} | Falhas: {fail} | Dado: {random_value}')
        command[0] = repeat


dice('!roll 3d6')
