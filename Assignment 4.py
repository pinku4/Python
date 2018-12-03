def main():
    num=raw_input('enter the number to find it digital root')
    print (num, '\n')
    D_root(num)
    print('the digital root of',num,'is:',D_root(num)

    def D_root(num):
          if len(num)==1:
             return num
          else:
               sum = 0
          for i in num:
               sum+= int(i)
          num = str(sum)
          return D_root(num)
          main()
