def roman(n):
    val=[1000,100,5,1]
    sym=["C","M","V","I"]
    rom_n=''
    i=0
    while(n>0):
        for _ in range(n//val[i]):
            rom_n+=sym[i]
            n-=val[i]
        i+=1
    return rom_n
print(roman(1))



