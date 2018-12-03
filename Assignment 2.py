praise=['a','b','c','d','e']
ext='!'
def main():
    print('Type in 5 phrases to be praise at you')
    for i in range(5):
        print (i,'phrase is')
        praise[i]=raw_input('')

        add_excitement()

        def add_exitement():
            for i in range(5):
                print (praise[i]+ext)
                main()
