def print_distance(p1, p2):
  d = (((p1[0]-p2[0])*(p1[0]-p2[0])) + ((p1[1]-p2[1])*(p1[1]-p2[1]))) ** 0.5
  print("Distance between {} and {} is {:.2f}".format(p1, p2, d))