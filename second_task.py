import random

def get_numbers_ticket(min, max, quantity):
    if max - min < quantity - 1:
         return []
    
    ticket_set  = set()

    if min < 1 or max > 1000:
        return "min cannot be less than 1, max cannot be more than 1000"
    for i in range(quantity):  
            current_number = random.randint(min, max)
            ticket_set.add(current_number) 
            if len(ticket_set) < quantity:
                 for i in range(quantity):  
                    current_number = random.randint(min, max)
                    ticket_set.add(current_number)
    return sorted(random.sample(list(ticket_set), k=quantity))



lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)