from sre_constants import RANGE_UNI_IGNORE
def compute_square_root (N, num_loops):
  x_n = N/2.0
  for i in range(num_loops):
    x_np1 = (x_n + N/x_n) / 2.0
    x_n = x_np1
    return x_np1
print(compute_square_root(N=9, num_loops=10))
print(compute_square_root(N=2, num_loops=10))
