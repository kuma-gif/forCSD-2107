import random

# ฟังก์ชันสร้าง neighbors โดยการเลื่อนค่า x ซ้ายหรือขวาอย่างสุ่ม
def generate_neighbors(x):
    return [x + random.uniform(-0.5, 0.5) for _ in range(3)] 

# ฟังก์ชัน Hill Climbing ใช้ในการค้นหาคำตอบของฟังก์ชัน f(x) ที่มีค่าน้อยที่สุด
def hill_climbing(f, x0):
    x = x0  # กำหนดค่าเริ่มต้น x
    while True:  # วน Loop จนกว่าเงื่อนไขข้างในจะเป็นเท็จ
        neighbors = generate_neighbors(x)  # สร้าง neighbors ของ x
        # หา neighbors ที่มีค่าของฟังก์ชันมากที่สุด
        best_neighbor = max(neighbors, key=f)
        # ถ้าค่าฟังก์ชันของ neighbors ที่ดีที่สุดไม่ดีกว่าหรือเท่ากับ x ให้หยุด
        if f(best_neighbor) <= f(x):
            return x
        x = best_neighbor  # มิฉะนั้น ใช้ neighbors ที่ดีที่สุดต่อไป

# ฟังก์ชัน f(x) ที่ใช้ในการคำนวนค่าของ x ยกกำลัง 2
def f(x):
    return x ** 2

# กำหนดค่าเริ่มต้น
x0 = 10  # กำหนดค่าเริ่มต้น x0 เป็น 10




# อันนี้ไม่อยู่ใน Slide ลงไปข้างล่างเลยก็ได้ #
# เรียกใช้ฟังก์ชัน hill_climbing เพื่อค้นหาคำตอบ
result = hill_climbing(f, x0)
print("Optimal value of x:", result) # พิมพ์ผลลัพธ์
print("Optimal value of f(x):", f(result))

# โค้ดด้านบนเป็นการใช้งาน Hill Climbing Algorithm เพื่อค้นหาค่า x ที่ทำให้ฟังก์ชัน f(x) = x ** 2 มีค่าน้อยที่สุด โดยเริ่มต้นที่ x0 = 10 และสร้าง neighbors
# โดยการเลื่อนค่า x ซ้ายหรือขวาอย่างสุ่ม และเลือกค่า x ที่มีค่าฟังก์ชัน f(x) มากที่สุดเป็นตัวแทนของ x ในแต่ละรอบ โดยทำซ้ำจนกว่าจะไม่มี neighbors ที่ดีกว่าค่าปัจจุบันของ x 
# หรือเงื่อนไขการหยุดเป็นเท็จ ซึ่งจะคืนค่า x ที่ได้ในที่สุดและค่า f(x) ที่ได้ในการทำงานของฟังก์ชัน hill_climbing