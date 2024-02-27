/*  https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/ */

// Importing libraries
import java.util.ArrayList; // เรียกใช้คลาสสำหรับสร้างจำนวนเต็ม
import java.util.Collections;
import java.util.Comparator; 
import java.util.List; // เเสดงข้อมูลที่ถูกเรียงลำดับ
import java.util.function.Function;  // นำเข้า interface ที่เเสดงถึง func ที่รับ 1 argument เเละส่งค่ากลับ

// Generates neighbors of x
public static List<Integer> generate_neighbors(int x) // function รับจำนวนเต็ม x เป็นinput เเละสร้าง (List<Integer>) เป็นจำนวนเต็มที่อยู่ไกล้เคียงกับ x
{
	// TODO: implement this function
	return new ArrayList<>();
}

// method
public static int
hill_climbing(Function<Integer, Integer> f, int x0) // ใช้รับ function f ที่รับจำนวนเต็มเป็น input เเละส่งค่าจำนวนเต็มกลับ
{
	int x = x0; // initial solution ( กำหนดค่าให้ตัวเเปรสำหรับเก็บค่า solution ปัจจุบัน เริ่มต้นด้วย x0 )
	while (true) { // Loopจนกว่าจะเจอ soluton ที่ดีที่สุด

		// find neighbors เเละ best neighbors
		List<Integer> neighbors = generate_neighbors(x); // เรียกใช้ฟังก์ชัน generate_neighbors เพื่อหา neighbors ของ x
		int best_neighbor = Collections.max(
			neighbors,
			Comparator.comparingInt(
				f::apply)); // find the neighbor with the highest function value
		// เงื่อนไขการหยุดทำงาน					
		if (f.apply(best_neighbor)
			<= f.apply(x)) // ตรวจสอบว่าค่าฟังก์ชัน f ของ best neighbor น้อยกว่าหรือเท่ากับ ค่าฟังก์ชัน f ของ x
			return x; // return x
		x = best_neighbor; // otherwise, continue with the
						// best neighbor
	}
}

public static void main(String[] args)
{
	// Example usage : ตัวอย่างการใช้งาน
	int x0 = 1; //  กำหนดค่าเริ่มต้น x0 ให้เป็น 1
	int x = hill_climbing // เรียกใช้ฟังก์ชัน hill_climbing
		((Integer y) -> y * y // ฟังก์ชัน f ที่ใช้ในอัลกอริทึม
		 , x0); 
	System.out.println("Result: " + x); // พิมพ์ค่า x
}
