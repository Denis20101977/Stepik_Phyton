# var = input("Напиши что нибудь")
# fw = open("doc/file.txt", "a")
# fw.write(var)
# fw.close()

# a - запись новых данных в файл и помещение этих данных в конец списка
# w - запись новых данных НО с удалением старых данных!

# fw = open("doc/file_2.txt", "w")
# fw.write("Привет!!!")
# fw.close()



number = input("Введите число")
sn = open("doc/file_4.md", "w")
sn.write(number)
sn.close()