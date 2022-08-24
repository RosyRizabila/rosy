# words = ["mangga", "anggur", "pisang"]
# for i in words:
#     print(i)

# create a sample collection
users = {'Hans': 'active', 'Rosy': 'inactive', 'Rose': 'active'}
# strategy: Iterate over a copy
for user, status in users.copy().items():
         if status == 'inactive':
             del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
     if status == 'active':
         active_users[user] = status
             print(users)
            print(active_users)

a = {}
a["c"] = "d"
a["e"] = "f"
print(a)