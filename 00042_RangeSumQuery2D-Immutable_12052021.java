
public class NumMatrix {
	private static int [][] dp;
	
	public NumMatrix(int [][] matrix) {
		if(matrix == null || matrix.length == 0 || matrix[0].length == 0) {
			return;
		}
		
		int m = matrix.length;
		int n = matrix[0].length;
		
		dp = new int[m+1][n+1];
		
		for(int i = 1; i <= m; ++i) {
			for(int j = 1; j <= n; ++j) {
				dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
			}
		}
		
		// dp[i][j] is sum of all number contained in a rectangle from (0,0) to position (i-1, j-1)
		
	}
	
	public static int sumRegion(int row1, int col1, int row2, int col2) {
		return dp[row2+1][col2+1] - dp[row1][col2+1] - dp[row2+1][col1] + dp[row1][col1];
	}
	
	public static void main(String[] args) {
		int arr[][] = {{3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}};
		NumMatrix numMatrix = new NumMatrix(arr);
		System.out.println(numMatrix.sumRegion(2, 1, 4, 3));
		System.out.println(numMatrix.sumRegion(1, 1, 2, 2));
		System.out.println(numMatrix.sumRegion(1, 2, 2, 4));
	}
}

// https://leetcode.com/problems/range-sum-query-2d-immutable/