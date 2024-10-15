def kalkulator():
    operasi = input("Pilih operasi (+, -, *, /): ")
    a, b = map(float, input("Masukkan dua angka (pisahkan dengan spasi): ").split())
    if operasi == '+': print(a + b)
    
    elif operasi == '-': print(a - b)
    
    elif operasi == '*': print(a * b)
    
    elif operasi == '/': print(a / b if b != 0 else "Error: Pembagian dengan nol.")
    
    else: print("Operasi tidak valid.")

kalkulator()