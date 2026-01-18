g_dic = {}
while True:
        try:
            item = input().upper()
            if item in g_dic:
                g_dic[item] += 1
            else:
                g_dic[item] = 1
        except EOFError:
            for item in sorted(g_dic.keys()):
                print(g_dic.get(item), item)
            break
        except KeyError:
            pass
