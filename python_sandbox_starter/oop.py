membership_types = ['Bronze', 'Silver', 'Gold', 'Platinum']

print(range(len(membership_types)-2))

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

        if membership_types.index(self.membership_type) in range(len(membership_types)-1):
            self.membership_upgradable = True
        else:
            self.membership_upgradable = False

        if membership_types.index(self.membership_type) in range(1,len(membership_types)):
            self.membership_downgradable = True
        else:
            self.membership_downgradable = False

    def update_membership_mobility(self):

        if membership_types.index(self.membership_type) in range(len(membership_types)-1):
            self.membership_upgradable = True
        else:
            self.membership_upgradable = False

        if membership_types.index(self.membership_type) in range(1,len(membership_types)):
            self.membership_downgradable = True
        else:
            self.membership_downgradable = False

    def upgrade_membership(self):
        if self.membership_upgradable == True:
            self.membership_type = membership_types[membership_types.index(self.membership_type)+1]
            self.update_membership_mobility()
            
        else:
            print(f'Membership for {self.name} is already fully upgraded')


    def downgrade_membership(self):
        if self.membership_downgradable == True:
            self.membership_type = membership_types[membership_types.index(self.membership_type)-1]
            self.update_membership_mobility()
        else:
            print(f'Membership for {self.name} is already at the lowest level')

c = Customer('Caleb','Gold')
c2 = Customer("Brad","Bronze")
c3 = Customer("Gavin","Platinum")

# customers = [Customer('Caleb','Gold'), Customer("Brad","Bronze")]
# print(customers[1].name)

print(c.name,c.membership_type)
c.upgrade_membership()
print(c.name,c.membership_type)
c.upgrade_membership()
print(c.name,c.membership_type)
c.downgrade_membership()
c.downgrade_membership()
c.downgrade_membership()
c.downgrade_membership()


print(c3.name,c3.membership_type)
c3.upgrade_membership()
# c.upgrade_membership()
# print(c.name,c.membership_type)



# __init__() <- is a method <-> initializer or constructor

