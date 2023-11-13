#madebyiffa(077)
#Hashira Kimetsu no Yaiba (柱 鬼滅 の 刃)
#https://devcode.gethired.id/challenge/share/weekly-challenge-3
#https://devcode.gethired.id/job/share/WFK816

def cariHashira(parameter):
    dataHashira = [
        {"Nama": "Giyu Tomioka", "TeknikPernafasan": "Air"},
        {"Nama": "Mitsuri Kanroji", "TeknikPernafasan": "Cinta"},
        {"Nama": "Obanai Iguro", "TeknikPernafasan": "Ular"},
        {"Nama": "Sanemi Shinazugawa", "TeknikPernafasan": "Angin"},
        {"Nama": "Gyomei Himejima", "TeknikPernafasan": "Batu"},
        {"Nama": "Muichiro Tokito", "TeknikPernafasan": "Kabut"},
        {"Nama": "Muichiro Tokito", "TeknikPernafasan": "Serangga"},
        {"Nama": "Kyojuro Rengoku", "TeknikPernafasan": "Api"},
        {"Nama": "Kanae Kocho", "TeknikPernafasan": "Bunga"},
        {"Nama": "Tengen Uzui", "TeknikPernafasan": "Suara"}
    ]
    for hashira in dataHashira:
        if parameter == hashira["Nama"]: #search by Hashira name
            return f"Teknik Pernafasan: {hashira['TeknikPernafasan']}"
        elif parameter == hashira["TeknikPernafasan"]: #search based on breathing technique
            return f"Nama Hashira: {hashira['Nama']}"
    return "Data tidak ditemukan" #if not found
    """
    #search by Hashira name
    for hashira in dataHashira:
        if query == hashira["Nama"]:
            return f"Teknik Pernafasan: {hashira['TeknikPernafasan']}"
    #search based on breathing technique
    for hashira in dataHashira:
        if query == hashira["TeknikPernafasan"]:
            return f"Nama Hashira: {hashira['Nama']}"
    """

#test cases
print(cariHashira("Kanae Kocho"))
print(cariHashira("Bunga"))
print(cariHashira("Angin"))
print(cariHashira("Mitsuri Kanroji"))
print(cariHashira("Tanjiro Kamado"))