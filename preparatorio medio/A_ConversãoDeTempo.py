_input = int(input())
h = int(_input/3600)
m = int((_input%3600)/60)
s = int((_input%3600)%60)
print('{}:{}:{}'.format(h, m, s))