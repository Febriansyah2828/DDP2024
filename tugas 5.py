{"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":437,"status":"ok","timestamp":1729654424274,"user":{"displayName":"Zombie 188","userId":"10121409333489154795"},"user_tz":-420},"id":"j61FssUALDMU","outputId":"f0f991f6-ed2b-4620-c4c9-142cfdbd4b05"},"outputs":[{"name":"stdout","output_type":"stream","text":["kendaraan\n","['Honda Vario', 'Sepeda Motor', 125, 'Pink', 2]\n","========\n","['Honda Vario', 'Sepeda Motor', 125, 'Pink', 2, 200000000]\n","========\n","['Honda Vario', 'Sepeda Motor', 'Honda', 125, 'Pink', 2, 200000000]\n","=========\n"]}],"source":["\n","# Jawaban no.1\n","kendaraan = ['Honda Vario', 'Sepeda Motor', 125,'Pink', 2]\n","print (\"kendaraan\")\n","print(kendaraan)\n","print(\"========\")\n","\n","kendaraan.append(200000000)\n","print(kendaraan)\n","print(\"========\")\n","\n","kendaraan.insert(2, 'Honda')\n","print(kendaraan)\n","print(\"=========\")"]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"background_save":true,"base_uri":"https://localhost:8080/"},"id":"9kTz12dUb5Cn"},"outputs":[{"name":"stdout","output_type":"stream","text":["ini adalah program sederhana untuk menghitung luas bangun datar\n","Pilih Menu angka 1-3 : \n","1. Persegi\n","2. Lingkaran\n","3. Segitiga\n"]}],"source":["# Jawaban no.2\n","\n","print('ini adalah program sederhana untuk menghitung luas bangun datar')\n","print(\"Pilih Menu angka 1-3 : \\n1. Persegi\\n2. Lingkaran\\n3. Segitiga\")\n","rumus = int(input('masukan rumus yang ingin dilihat '))\n","\n","match rumus:\n","  case 1:\n","    print(\"Luas persegi = sisi * sisi\")\n","    sisi= int(input(\"masukan angka\"))\n","    luas= sisi*sisi\n","    print(int(luas))\n","\n","  case 2:\n","    print:(\"luas lingkaran = phi*r*r\")\n","    r= int(input(\"masukan angka\"))\n","    phi= 3.14\n","    luas= phi*r*r\n","    print(int(luas))\n","\n","  case 3:\n","    print(\"luas segitiga = 1/2*alas*tinggi\")\n","    alas= int(input(\"masukan angka alas\"))\n","    tinggi= int(input(\"masukan angka tinggi\"))\n","    luas= 1/2*alas*tinggi\n","    print(int(luas))\n","  case _:\n","    print(\"salah pilih\")"]}],"metadata":{"colab":{"authorship_tag":"ABX9TyPkR81ALMDs5XW2VwJqPss+","name":"","version":""},"kernelspec":{"display_name":"Python 3","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":0}