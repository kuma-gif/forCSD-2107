import random
import math

''' ฟังก์ชัน objective_function คำนวณค่าของฟังก์ชัน
 โดยในที่นี้เราให้ฟังก์ชันนี้คำนวณค่าของ (x - 5) ** 2 แล้วทำการกลับเครื่องหมาย
 เพื่อให้ค่าที่น้อยที่สุดกลับเป็นค่าที่มากที่สุดและแสดงให้เป็นค่าติดลบ'''

# obj. function มีไว้เพื่อเปรียบเทียบค่าว่ามันดีพอไหม
def objective_function(x): 
    return -((x - 5) ** 2)

# สร้างเพื่อนบ้านขึ้นมา โดยที่่ Node เพื่อนบ้านจะอยู่ในช่วง max step (ช่วงระหว่าง -1 ถึง 1)
def get_neighbour(current, max_step):
      # สุ่มตำแหน่งใหม่ใกล้เคียง
    return current + random.uniform(-max_step, max_step) 

# ฟังก์ชันสำหรับทำการตัดสินใจเปลี่ยนตำแหน่งหรือไม่
def accept_probability(delta_e, temperature):
    if delta_e > 0:
        return math.exp(-delta_e / temperature)
    else:
        return 1.0

def simulated_annealing_search(initial_state, max_iterations, max_step, initial_temperature, cooling_rate):
    #  กำหนดค่าให้ตัวเเปร currrent_state มีค่าเท่ากับ initial_state 
    current_state = initial_state 
    # เรียกใช้ func objective_function(x) 
    current_value = objective_function(initial_state) 
    # กำหนดค่าให้ตัวเเปร best_state มีค่าเท่ากับ current_state
    best_state = current_state 
    # กำหนดค่าให้ตัวเเปร best_value มีค่าเท่ากับ current_value
    best_value = current_value 
    # ให้ค่า temp มีค่าเท่ากับ 1000
    temperature = initial_temperature 


    for _ in range(max_iterations):  # loop 50 รอบ

        # กำหนดค่าจากการเรียกใช้ func get_neighbour
        neighbour_state = get_neighbour(current_state, max_step)
        # กำหนดค่าจากการเรียกใช้ func  objective_function
        neighbour_value = objective_function(neighbour_state)
        delta_e = neighbour_value - current_value
        # (-16) - (-25) = 9

        # ตรวจสอบว่าจะยอมรับสถานะใหม่หรือไม่โดย...
        # ทำเงื่อนไข delta_e > 0 หรือ เลขสุ่ม < func accept
        if delta_e > 0 or random.random() < accept_probability(delta_e, temperature):
            # กำหนดค่าให้ตัวเเปร current_state มีค่าเท่ากับ neighbour_state
            current_state = neighbour_state
            # กำหนดค่าให้ตัวเเปร current_value มีค่าเท่ากับ neighbour_value
            current_value = neighbour_value

        # ตรวจสอบว่าสถานะใหม่ดีกว่าสถานะที่ดีที่สุดหรือไม่
        # ทำเงื่อนไข current value > best value
        if current_value > best_value:
            # กำหนดค่าให้ตัวเเปร best_state มีค่าเท่ากับ neighbour_state
            best_state = current_state
            # กำหนดค่าให้ตัวเเปร best_value มีค่าเท่ากับ current_value
            best_value = current_value

         # initial_temp * cooling_rate
         # 1000 * 0.95 = 950
        temperature *= cooling_rate

     # return ค่า best state , best value กลับไป
    return best_state, best_value



# กำหนดค่า
initial_state = 0
max_iterations = 50
max_step = 1
initial_temperature = 1000
cooling_rate = 0.95
