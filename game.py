def rock():
  import random
  h=input("choose one rock,scissors,paper:")
  c=("paper","scissors","rock")
  while h not in c:
    h=input("wrong input try again:")
  if h=="scissors":
    h=0
  if h=="rock":
    h=1
  if h=="paper":
    h=2
  p=(random.randint(0,2))
  #결과
  if h==p:
    print("(it was draw)")
  if h-2==p:
    print("(you are lose)")
  if h-1==p:
    print("(you are win)")
  if h+2==p:
    print("(your are win)")
  if h+1==p:
    print("(your are lose)")
  if h==0:
    h="scissors"
  if h==1:
    h="rock"
  if h==2:
    h="paper"
  if p==0:
    p="scissors"
  if p==1:
    p="rock"
  if p==2:
    p="paper"
  print("you:"+str(h))
  print("computer:"+str(p))
  r = input("if you want to play again type 'restart':")
  if r == "restart":
    rock()
y = input("Do you want to play rock scissors paper? if you want to play rock scissors paper type 'yes' or if you don't want to play game type 'no':")
if y == 'yes':
  rock()
  
