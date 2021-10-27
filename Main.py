def caesarBoxCipherEncoding(message):
    item = set() ; l = len(message) ; d = 0
    for i in range(2,int(l**0.5)+1):
        if l%i==0:
            item.update([i,l//i])
    item = sorted(item)
    if item == []: return 0
    for i in item:
        j = 0 ; pot = ''; kq = ''
        for j in range(i):
            pot+=message[j::i]
            j+=1
        j = 0
        for j in range(i):
            kq+=pot[j::i]
            j+=1
        if kq == message: d+=1
    return d
