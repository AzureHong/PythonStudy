address = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is ",address['Swaroop'])

# 删除一对键值-值匹配
del address['Spammer']
print('\nThere are {} contacts in the addresss-book\n'.format(len(address)))

# 通过使用字典的items() 来访问字典中的每一对键值信息
for name,ad in address.items():
    print('Contact {} at {}'.format(name,ad))

# 添加键值对
address['Guido'] = 'guido@python.org'
if 'Guido' in address:
    print("\nGuido's address is ",address['Guido'])