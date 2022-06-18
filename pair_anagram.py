import os
def anagrams(s):
    # algorithm
    aux = dict()
    for i in range(len(s)):
        subs = ""
        for j in range(i,len(s)):
            subs += s[j]
            s_subs = "".join(sorted(subs))
            if aux.keys().__contains__(s_subs):
                aux[s_subs].append(subs)
            else:
                aux[s_subs] = [subs]
    res = []
    for key, value in aux.items():
        if len(value) > 1:
            # print all pairs
            for i in range(len(value)):
                for j in range(i+1,len(value)):
                    res.append((
                        value[i],
                        value[j]
                    ))
    #print result
    return res
    
def main():
    q = int(input("Ingrese cantidad de queries: "))
    for i in range(q):
        s = input("Ingrese la cadena: ")
        print(f"Q{i+1}: {anagrams(s)}")

if __name__ == "__main__":
    main()
    exit(0)
    
        
