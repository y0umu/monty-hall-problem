# reinvent the wheel simulating the monty hall problem
# https://en.wikipedia.org/wiki/Monty_Hall_problem

# using python3

from secrets import randbelow

# def isHit(p):
#     '''Generate a float in range [0,1] and say if is lower than p'''
#     assert p >=0 and p <=1
#     if np.random.rand() < p:
#         return True
#     else:
#         return False

# def chooseDoor():
#     '''Choose the door, returns 0,1 or 2'''
#     dice = np.random.rand()
#     if dice < 1/3:
#         return 0
#     elif dice > 2/3:
#         return 2
#     else:
#         return 1

def chooseFrom(lst):
    """
    Choose from lst
    @param lst: python list.

    Returns
    @ret ind: the chosen index of the lst
    """
    n_lst = len(lst)
    return randbelow(n_lst)

def openDoor(car_door_ind, init_choice):
    """
    Change one of the door status in list doors
    It should not open the door that has a car behind it or the player's init_choice

    @param car_door_ind: int. The index of doors that indicates there is car behind this index
    @parma init_choice: int. The index of doors that indicates the player's initial choice

    Returns
    @ret door_to_open_ind: int. the index of which door is opened
    """
    lst = [0,1,2]
    lst.remove(car_door_ind)
    if init_choice in lst:
        lst.remove(init_choice)
    door_to_open_ind = lst[chooseFrom(lst)]
    return door_to_open_ind

def switchChoice(opend_door, init_choice):
    """
    Switch to availabe door otherside than the init_choice
    @parma opend_door: int. the index of door that is opend
    @init_choice: int. 

    Returns
    @ret switched_choice: int. the index to which the door switched
    """
    lst = [0,1,2]
    lst.remove(opend_door)
    if init_choice in lst:
        lst.remove(init_choice)
    switched_choice = lst[chooseFrom(lst)]
    return switched_choice

def main():
    n_experiments = 50000
    n_sticky_wins = 0
    n_switch_wins = 0
    for t in range(n_experiments):
        car_door_ind = randbelow(3) # where is the car?
        init_choice = randbelow(3)  # initial choice
        player_stick_choice = init_choice
        opend_door = openDoor(car_door_ind, init_choice)
        player_switch_choice = switchChoice(opend_door, init_choice)

        if player_stick_choice == car_door_ind:
            n_sticky_wins += 1
        elif player_switch_choice == car_door_ind:
            n_switch_wins += 1
        # print("car_door_ind={},opend_door={},\
        # player_stick_choice={},player_switch_choice={}".format(
        #     car_door_ind, opend_door, player_stick_choice, player_switch_choice))
        # pass
    print("Sticky wins {}".format(n_sticky_wins / n_experiments))
    print("Switch wins {}".format(n_switch_wins / n_experiments))
    print("Done")

if __name__ == "__main__":
    main()