### Task:
There is a matrix M of 2 rows and N columns, each cell contains a value of either 1 or 0. U, L are the sums of these values in first, second row respectively. C is an array of length N with the sums of these values in each column.

Given U, L and C, find M.

### Output:
- In case of no solution: return a string with `IMPOSSIBLE`.
- In case of a solution: return a string in the format `<row1_values>,<row2_values>` e.g. `111000,100001`.
- In case of multiple solutions: pick only one.

### Restrictions:
- N is inthe range `[0..100000]`.
- C values are in the range `[0..2]`.
