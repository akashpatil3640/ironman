def perfect(a):
    if(a**(1/2) *(a**(1/2)) ==a):
        return 1
    else:
        return 0

n=int(input())
stack=[]

if(n>0):
    for i in range(n):
        inp=input().split(" ")
        #print(inp[0])
        if(int(inp[0]+inp[1])>0 and int(inp[0])<50):
            if(int(inp[1])>0 and int(inp[1])<30):
                if(int(inp[2])>0 and int(inp[2])<30):
                    if(int(inp[1])<18 and int(inp[2])<10):
                        #print("PASS")
                        
                        volume=int(inp[0])*int(inp[1])*int(inp[2])
                        #print(volume)
                        akash=perfect(volume)
                        if(akash):
                            #print("TRUE")
                            stack.append([1,volume,1])
                        else:
                            #print("FALSE")
                            stack.append([1,volume,0])
                    else:
                        #print("FAIL")
                        stack.append([0])
                else:
                    #print("FAIL")
                    stack.append([0])
            else:
                #print("FAIL")
                stack.append([0])
        else:
            #print("FAIL")
            stack.append([0])

    for i in stack:
        if(len(i)==3):
            if(i[0]==1):
                print("PASS")
                print(i[1])
                if(i[2]==1):
                    print("TRUE")
                else:
                    print("FALSE")

            else:
                print("FAIL")
        else:
            print("FAIL")
        print("\n")
            
