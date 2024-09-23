stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

inverse = [(value, key) for key, value in stats.items()]
print(max(inverse)[1]) #использует метки в качестве ключей, при наличии дубликатов ключей
                         #максимального значения - вернет только один ключ

# max_key = max(stats, key=lambda k: stats[k])  #самый удобный и быстрый способ, но тоже выдает только один ключ
# print(max_key)

# max_value = max(stats.items(), key=lambda x: x[1]) #выдает ключ со значением, а не посто max ключ
# print(max_value)

# max_v = max(zip(stats.values(), stats.keys())) #тоже выдает только один ключ
# print(max_v)


# list_num_max_value = []
# max_value = stats.get(max(stats))
# for letter in stats:
#       if stats.get(letter) == max_value:
#         list_num_max_value.append(max_value)
# print (list_num_max_value)  # выдаст ключи


