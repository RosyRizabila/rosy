with open('workfile', encoding="utf-8") as f:
        read_data = f.read()
print(f.closed)

f.close()
f.read()