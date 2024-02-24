/*  https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/ */

// Importing libraries
import java.util.ArrayList; // เรียกใช้คลาสสำหรับสร้างจำนวนเต็ม
import java.util.Collections;
import java.util.Comparator; 
import java.util.List; // เเสดงข้อมูลที่ถูกเรียงลำดับ
import java.util.function.Function;  // นำเข้า interface ที่เเสดงถึง func ที่รับ 1 argument เเละส่งค่ากลับ

// Generates neighbors of x
public static List<Integer> generate_neighbors(int x)
{
	// TODO: implement this function
	return new ArrayList<>();
}

// method
public static int
hill_climbing(Function<Integer, Integer> f, int x0)
{
	int x = x0; // initial solution ( กำหนดค่าให้ตัวเเปร )
	while (true) {
		List<Integer> neighbors = generate_neighbors(
			x); // generate neighbors of x
		int best_neighbor = Collections.max(
			neighbors,
			Comparator.comparingInt(
				f::apply)); // find the neighbor with the
							// highest function value
		if (f.apply(best_neighbor)
			<= f.apply(x)) // if the best neighbor is not
						// better than x, stop
			return x;
		x = best_neighbor; // otherwise, continue with the
						// best neighbor
	}
}

public static void main(String[] args)
{
	// Example usage
	int x0 = 1;
	int x = hill_climbing((Integer y) -> y * y, x0);
	System.out.println("Result: " + x);
}
