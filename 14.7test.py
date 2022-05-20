k, E, M, S = map(int, input().split())

if k < 0 or k > 100 or E < 0 or E > 100 or M < 0 or M > 100 or S < 0 or S > 100:
  print('잘못된 점수')
else:
  if (k + E + M + S) / 4 >= 80:
    print('합격')
  else:
    print('불합격')