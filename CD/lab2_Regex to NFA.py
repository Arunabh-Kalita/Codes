table = [ [0]*3 for _ in range(20) ]

regex = input("Regular expression : ")
regex += " "

i = 0
j = 1


while(i<len(regex)):
    if regex[i] == 'a':
        try:
            if regex[i+1] != '|' and regex[i+1] !='*':
                table[j][0] = j+1
                j += 1
            elif regex[i+1] == '|' and regex[i+2] =='b':
                table[j][2]=((j+1)*10)+(j+3)
                j+=1
                table[j][0]=j+1
                j+=1
                table[j][2]=j+3
                j+=1
                table[j][1]=j+1
                j+=1
                table[j][2]=j+1
                j+=1
                i=i+2
            elif regex[i+1]=='*':
                table[j][2]=((j+1)*10)+(j+3)
                j+=1
                table[j][0]=j+1
                j+=1
                table[j][2]=((j+1)*10)+(j-1)
                j+=1
        except:
            table[j][0] = j+1

    elif regex[i] == 'b':
        try:
            if regex[i+1] != '|' and regex[i+1] !='*':
                table[j][1] = j+1
                j += 1
            elif regex[i+1]=='|' and regex[i+2]=='a':
                table[j][2]=((j+1)*10)+(j+3)
                j+=1
                table[j][1]=j+1
                j+=1
                table[j][2]=j+3
                j+=1
                table[j][0]=j+1
                j+=1
                table[j][2]=j+1
                j+=1
                i=i+2
            elif regex[i+1]=='*':
                table[j][2]=((j+1)*10)+(j+3)
                j+=1
                table[j][1]=j+1
                j+=1
                table[j][2]=((j+1)*10)+(j-1)
                j+=1
        except:
            table[j][1] = j+1
        
    elif regex[i]=='e' and regex[i+1]!='|'and regex[i+1]!='*':
        table[j][2]=j+1
        j+=1

    elif regex[i]==')' and regex[i+1]=='*':

        table[0][2]=((j+1)*10)+1
        table[j][2]=((j+1)*10)+1
        j+=1

    i +=1


print ("\nTransition function:")
for i in range(j):
    if(table[i][0]!=0):
        print("\u03B4[{0},a]-->{1}".format(i,table[i][0]))
    if(table[i][1]!=0):
        print("\u03B4[{0},b]-->{1}".format(i,table[i][1]))
    if(table[i][2]!=0):
        if(table[i][2]<10):
            print("\u03B4[{0},e]-->{1}".format(i,table[i][2]))
        else:
            print("\u03B4[{0},e]-->{1} and {2}".format(i,int(table[i][2]/10),table[i][2]%10))