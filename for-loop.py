for i in range(10):
    print(i)
print('=================')


names = ['Dew', 'Oat', 'Ice', 'Yed', 'Ont']
for name in names:
    print(name)
print('=================')


for name in names:
    if name != 'Yed':
        continue
    print(name)
print('=================')


for name in names:
    if 'c' in name:
        break
    print(name)
