cnt =[]
checks = ['+++n+++', '+++n+++', '+bbn+++', '+++n+++']
all3x3 = ['bbn', 'bnb', 'nbb', 'bb+n', 'nbb+', 'n+bb', 'bbn+', '+bbn', 'bnb+', 'bn+b', 'nb+b', 'b+nb', 'b+bn', '+nbb', '+bnb']

for check in checks:
    for per in all3x3:
        if per in check:
            cnt.append((per, check))
            break
print(cnt)