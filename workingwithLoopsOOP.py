class Pod:
    # Class variable
    member = {}
    # Class Constructor method is called when an Object is instantiated
    def __init__(self,leader,cell):
        Pod.member[leader] = cell
    # Method to add member and number to member dictionary
    def add_member(self, member_to_add,cell_number):
        Pod.member[member_to_add] = cell_number
    # Class method to print the pod_leader and cell numbers   
    def display_members(self):
        print('\n')
        for Pod.member, number in Pod.member.items():
            print(Pod.member, number)
#  Prompt for the Pod Leader name and number
leader = input('Who is the leader? ')
cell = input('What is the leaders cell number? ')

repeat_amnt = int(input("How many do you want to add: "))
# Initialize the Pod Dictionary with the leader's name and number
pod = Pod(leader,cell)
pod.add_member(leader,cell)

for i in range(0, repeat_amnt):
    member = input("What is the members name: ")
    cell = input("What is the members cell number: ")
    pod.add_member(member,cell)

    pod.display_members();
