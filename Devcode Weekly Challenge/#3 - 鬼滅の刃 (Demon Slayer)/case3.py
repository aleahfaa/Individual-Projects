#madebyiffa(077)
#Serangan Hinokami Kagura
#https://devcode.gethired.id/challenge/share/weekly-challenge-3
#https://devcode.gethired.id/job/share/WFK816

def seranganHinokamiKagura(nyawaIblis):
    total_damage = 0
    serangan_ke = 0
    while total_damage < nyawaIblis and serangan_ke < 13:
        serangan_ke += 1
        total_damage += serangan_ke
    if total_damage >= nyawaIblis:
        return f'Iblis Kalah pada Serangan ke-{serangan_ke}'
    else:
        sisa_hp = nyawaIblis - total_damage
        return f'Sisa HP Iblis {sisa_hp}'

#test cases
nyawaIblis_1 = 4
output_1 = seranganHinokamiKagura(nyawaIblis_1)
print(output_1)
nyawaIblis_2 = 45
output_2 = seranganHinokamiKagura(nyawaIblis_2)
print(output_2)
nyawaIblis_3 = 100
output_3 = seranganHinokamiKagura(nyawaIblis_3)
print(output_3)

#using loop to count the total damage from Hinokami Kagura's attacks
#until the demon's life value is ≤ total damage
#or until it reaches the 13th attack
#return string according the calculation results