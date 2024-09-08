s = input()
def get_suffix(s):
    idx = s.find('a')
    return s[idx:]
print(get_suffix(s))