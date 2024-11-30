import random

def get_numbers_ticket(min, max, quantity):
    if max - min < quantity - 1:
         return []
    if min < 1 or max > 1000:
        return "min cannot be less than 1, max cannot be more than 1000"
    return sorted(random.sample(list(range(min,max+1)), k=quantity))


lottery_numbers = get_numbers_ticket(10, 14, 5)
print("Ваші лотерейні числа:", lottery_numbers)