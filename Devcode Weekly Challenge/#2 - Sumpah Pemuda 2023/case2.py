#madebyiffa(077)
#Pesan Rahasia Undangan Kongres Pemuda
#https://devcode.gethired.id/challenge/share/weekly-challenge-2
#https://devcode.gethired.id/job/share/IWU488

def konversiBiner(pesanBiner):
    total = 0
    for i in range(len(pesanBiner)):
        total += int(pesanBiner[i]) * (2 ** (len(pesanBiner) - i - 1))
    return total

#test cases
print(konversiBiner("11011"))
print(konversiBiner("11100"))
print(konversiBiner("1010"))
print(konversiBiner("11110001000"))

#binary string as input and converts it into decimal number
#rule: each digit in binary string is multiplied by corresponding power of 2