#  Topshiriq 1
# 1 2 30 - 1 hour 2 minutes 30 seconds
# 1 3 20 - 1 hour 3 minutes 20 seconds
#

h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
print((h2-h1)*3600+(m2-m1)*60+(s2-s1))
