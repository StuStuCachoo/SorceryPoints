# 1st	2
# 2nd	3
# 3rd	5
# 4th	6
# 5th	7


def add_to_all_slots(all_slots: list, cur_slots: list, slot_to_add: int) -> list:
    for i in range(len(cur_slots)):
        if 0 <= slot_to_add <= 4:
            cur_slots[i][slot_to_add] += 1
        all_slots.append(cur_slots[i])
    return all_slots


def one_slot(sp_limit, sp_remaining, recharges_left) -> list:
    if sp_limit >= sp_remaining + 2 and recharges_left != 0:
        return one_slot(sp_limit, sp_remaining + 2, recharges_left - 1)
    all_slots = []

    if recharges_left > 0 and sp_limit > sp_remaining:
        # At this point we know sp_remaining is sp_limit-1
        cur_slots = one_slot(sp_limit, sp_remaining + 1, recharges_left - 1)
        all_slots = add_to_all_slots(all_slots, cur_slots, -1)

    if sp_remaining >= 7:
        cur_slots = one_slot(sp_limit, sp_remaining - 7, recharges_left)
        all_slots = add_to_all_slots(all_slots, cur_slots, 4)

    if sp_remaining >= 6:
        cur_slots = one_slot(sp_limit, sp_remaining - 6, recharges_left)
        all_slots = add_to_all_slots(all_slots, cur_slots, 3)

    if sp_remaining >= 5:
        cur_slots = one_slot(sp_limit, sp_remaining - 5, recharges_left)
        all_slots = add_to_all_slots(all_slots, cur_slots, 2)

    if sp_remaining >= 3:
        cur_slots = one_slot(sp_limit, sp_remaining - 3, recharges_left)
        all_slots = add_to_all_slots(all_slots, cur_slots, 1)

    if sp_remaining >= 2:
        cur_slots = one_slot(sp_limit, sp_remaining - 2, recharges_left)
        all_slots = add_to_all_slots(all_slots, cur_slots, 0)

    if recharges_left == 0 and sp_remaining < 2:
        return [[0, 0, 0, 0, 0]]
    return all_slots


finalSlots = one_slot(int(input("SP Limit: ")), 0, int(input("Hours of downtime: ")) * 2)
finalSlots = [finalSlots[i] for i in range(len(finalSlots)) if
              i == 0 or finalSlots[i] != finalSlots[i - 1]]  # removes duplicate elements
print(finalSlots)
