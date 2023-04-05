child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total():
    total=sum(chocolates_received)
    return total
def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates<1:
        print('Extra chocolates is less than 1')
    elif child_id_rewarded not in child_id:
        print('Child is invalid ')
    else:
        ind=child_id.index(child_id_rewarded)
        chocolates_received[ind]+=extra_chocolates
        print(chocolates_received)

