import random
import math

# ฟังก์ชัน objective_function คำนวณค่าของฟังก์ชันวัตถุประสงค์
# โดยในที่นี้จะให้ฟังก์ชันนี้คำนวณค่าของ (x - 5) ** 2 แล้วทำการกลับเครื่องหมาย
# เพื่อให้ค่าที่น้อยที่สุดกลับเป็นค่าที่มากที่สุดและแสดงให้เป็นค่าติดลบ
def objective_function(x):
    return -((x - 5) ** 2)

# ฟังก์ชัน get_neighbour ใช้ในการสร้างสถานะใหม่ (neighbors)
# โดยการสุ่มเลขจำนวนเต็มในช่วง (-max_step, max_step) 
# แล้วนำมาบวกกับสถานะปัจจุบันเพื่อให้ได้สถานะใหม่
def get_neighbour(current, max_step):
    return current + random.uniform(-max_step, max_step) 

# ฟังก์ชัน accept_probability ใช้ในการคำนวณความน่าจะเป็นในการยอมรับสถานะใหม่
# โดยใช้สูตร Boltzmann ถ้า delta_e มีค่ามากกว่า 0 และมีโอกาสสุ่มเป็นจำนวนเรขาคณิตที่สุ่มมาน้อยกว่าค่าที่คำนวณได้จากฟังก์ชัน
# ถ้า delta_e เป็นค่าลบหรือศูนย์ จะยอมรับสถานะใหม่เสมอ
def accept_probability(delta_e, temperature):
    if delta_e > 0:
        return math.exp(-delta_e / temperature)
    else:
        return 1.0

# ฟังก์ชัน simulated_annealing_search ใช้ในการทำการค้นหาด้วย Simulated Annealing
# โดยเริ่มต้นจากสถานะเริ่มต้น initial_state และทำการลูป max_iterations
# โดยทุกครั้งจะสร้างสถานะใหม่ และใช้ accept_probability เพื่อตัดสินใจในการยอมรับสถานะใหม่
# และทำการปรับอุณหภูมิเพื่อลดการยอมรับสถานะที่แย่ลง
# สุดท้ายจะส่งคืนสถานะที่ดีที่สุด (best_state) และค่าของฟังก์ชันที่ดีที่สุด (best_value)
def simulated_annealing_search(initial_state, max_iterations, max_step, initial_temperature, cooling_rate):
    current_state = initial_state
    current_value = objective_function(initial_state)
    best_state = current_state
    best_value = current_value
    temperature = initial_temperature

    for _ in range(max_iterations):
        neighbour_state = get_neighbour(current_state, max_step)
        neighbour_value = objective_function(neighbour_state)
        delta_e = neighbour_value - current_value

        if delta_e > 0 or random.random() < accept_probability(delta_e, temperature):
            current_state = neighbour_state
            current_value = neighbour_value

        if current_value > best_value:
            best_state = current_state
            best_value = current_value

        temperature *= cooling_rate

    return best_state, best_value

# กำหนดค่าพารามิเตอร์
initial_state = 0
max_iterations = 50
max_step = 1
initial_temperature = 1000
cooling_rate = 0.95
