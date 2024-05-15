file_name = "file.txt"
data = "Hello World"
data_2 = "Hello World!!!"

# fw = open(file_mane, "a")
# fw.write(data)
# fw.close()

with open(file_name, "a") as double_files:
    double_files.write(data + data_2)
