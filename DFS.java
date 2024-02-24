import java.util.*;

public class DFS {

  public static List<Integer> dfs(int[][] graph, int start, int depth) {
    List<Integer> visited = new ArrayList<>();

    def _dfs(int node) {
        // ตรวจสอบว่าถึงระดับความลึกที่จำกัดแล้วหรือโหนดนี้เคยถูกสำรวจแล้ว
      if (depth == 0 || visited.contains(node)) {
        return;
      }
      // เพิ่มโหนดนี้ลงในรายการโหนดที่สำรวจแล้ว
      visited.add(node);

      // สำรวจโหนดที่อยู่ติดกัน
      for (int neighbor : graph[node]) {
        _dfs(neighbor);
      }
    }

    _dfs(start);

    return visited;
  }

  public static void main(String[] args) {
    // สร้างกราฟ
    int[][] graph = {
      {1, 2},
      {0, 2, 3},
      {0, 1, 3, 4},
      {1, 2, 4, 5},
      {2, 3, 5, 6},
      {3, 4, 6},
      {4, 5}
    };

    // เริ่มต้นจากโหนด 0
    int start = 0;

    // กำหนดระดับความลึกของการค้นหาเป็น 10
    int depth = 10;

    // ทำการค้นหา
    List<Integer> visited = dfs(graph, start, depth);

    // แสดงผลเส้นทางที่พบ
    for (int node : visited) {
      System.out.println(node);
    }
  }
}
