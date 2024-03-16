rank = str(input("등급을 입력해 주세요" ))
grade1 = ("평점 : 4.5")
grade2 = ("평점 : 4.0")
grade3 = ("평점 : 3.5")
grade4 = ("평점 : 3.0")
grade5 = ("평점 : 2.5")
grade6 = ("평점 : 2.0")
grade7 = ("평점 : 1.5")
grade8 = ("평점 : 1.0")
gradezero = ("평점 : 0")

if rank == ("A+"):
  print(rank,',', grade1)

elif rank == ("A"):
  print(rank,',', grade2)

elif rank == ("B+"):
  print(rank,',', grade3)


elif rank == ("B"):
  print(rank,',', grade4)


elif rank == ("C+"):
  print(rank,',', grade5)


elif rank == ("C"):
  print(rank,',', grade6)


elif rank == ("D+"):
  print(rank,',', grade7)


elif rank == ("D"):
  print(rank,',', grade8)


elif rank == ("F"):
  print(rank,',',gradezero)
