import time
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "шутка",
            "ЩИЩ": "одобрение или восторг",
            "КРИПОВЫЙ": "страшный, пугающий",
            "АГРИТЬСЯ": "злиться",
            "АПРУВИТЬ": "утвердить",
            "АЧИВКА": "достижение",
            "БАЙТИТЬ": "копировать, красть чужое, заниматься плагиатом. Служить приманкой для кого-то, чего-то",
            "БАТТХЕРТ": "раздражение, обида",
            "ГАЗЛАЙТИНГ": "форма психологического насилия, при которой манипулятор отрицает произошедшие факты",
            "ДАУНЛОУДИТЬ": "захламлять память ненужным",
            "КОЛЛАБЫ": "коллективное",
            "КРАЩ": "предмет обожания",
            "МАТЧИТЬСЯ": "подходить",
            "СВАЙПИТЬ": "смахнуть фото",
            "ОТФАКТЧЕКИТЬ": "соблюдать правило двух надежных источников",
            "ПУШИТЬ": "настойчиво торопить",
            "САСНЫЙ": "соблазнительный, симпатичный, сексуальный",
            "САММЭРИТЬ": "делать выводы",
            "ФАСИЛИТИРОВАТЬ": "упрощать, облегчать",
            "ФЕЙСПАЛМ": "лицо, прикрытое рукой. Жест разочарования и стыда",
            "ХЕЙТИТЬ": "ненавидеть",
            "ЧИЛИТЬ": "расслаблять",
            "ЧИТЕР": "жулик",
            "ЧСВ": "чувство собственной важности",
            "ШЕЙМИТЬ": "стыдить кого-либо",
            "ШИППЕРИТЬ": "представлять, что какие-то персонажи (книги, фильма, сериала, игры) или популярные люди состоят в романтических отношениях, хотя в действительности это не так",
            "СИМП": "Человек, очень сильно увлеченный, фанатеющий от кого-либо или чего-либо, симпающий на него"
            }
#Загрузка Системы
print("====================================================================================")
time.sleep(0.5)
print("ЗАГРУЗКА СИСТЕМЫ Phantom OS")
time.sleep(0.5)
print("====================================================================================")
time.sleep(0.5)
print("Загрузка.")
time.sleep(0.5)
print("Загрузка..")
time.sleep(0.5)
print("Загрузка...")
time.sleep(0.5)
print("Загрузка.")
time.sleep(0.5)
print("Загрузка..")
time.sleep(0.5)
print("Загрузка...")
time.sleep(0.5)
print("====================================================================================")
time.sleep(0.5)
while True:
    #Начало программы
    print("Добро пожаловать в программу объяснялку современных слов!")
    time.sleep(1)
    word = input("Введите непонятное вам современное слово (БОЛЬШИМИ БУКВАМИ!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Ничего не нашлось')
