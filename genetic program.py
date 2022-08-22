#----------------------------------------------------
#최대적합도 올리기, 함수, 반복 간략화, 변이 확률
#----------------------------------------------------
#genetic algorithm
import random
import matplotlib.pyplot as plt
x1=[]
y1=[]
gs=int(input("개체의 유전자수(15):"))
roop=int(input("반복 횟수 입력(100):"))
M1=int(input("변이 1 확률(10):"))
M2=int(input("변이 2 확률(2):"))
print()
#----------------------------------------------------
#Initialize
a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i=[],[],[],[],[],[],[],[],[],[]
all_gen=[a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i]
for k in range(0,10):
  for i in range(0,gs):#
    i_p=random.randint(1,5)
    if i_p==1:
      all_gen[k].append(1)
    else:
      all_gen[k].append(0)
#----------------------------------------------------
#Loop
for i in range(1,roop):
#----------------------------------------------------
#output(print,graph)
  suit=(sum(a_i)+sum(b_i)+sum(c_i)+sum(d_i)+sum(e_i)+sum(f_i)+sum(g_i)+sum(h_i)+sum(i_i)+sum(j_i))
  print(i,"generation:",a_i  ,"suitabilty:",suit/10)#
  print()
  plt.axhline(gs,c="r",linewidth=0.7)#
  x=i
  y=(suit/10)#
  x1.append(i)
  y1.append(y)
  plt.plot(x1,y1,c="b",linewidth=0.5)
  plt.scatter(x,y,s=2,c="b")
  plt.xlabel("generation")
  plt.ylabel("suitability")
  plt.pause(0.1)
  plt.ylim([0, gs+gs/10])  #
  plt.title("Generation Algorithm")
  if suit/10==gs:#
    print("최대 적합도에 도달하였습니다")#
    break
#----------------------------------------------------
#Selection
  all_gen=[a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i]
  all_gen.sort()
  a_p=all_gen[-1]
  b_p=all_gen[-2]
  c_p=all_gen[-3]
  d_p=all_gen[-4]
  p_g=[all_gen[-1],all_gen[-2],all_gen[-3],all_gen[-4]]
#----------------------------------------------------
#Crossover and Replace
  a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i=[],[],[],[],[],[],[],[],[],[]
  all_gen=[a_i,b_i,c_i,d_i,e_i,f_i,g_i,h_i,i_i,j_i]
  for k in range(0,10):
    p=p_g[random.randint(0,3)]
    q=p_g[random.randint(0,3)]
    for i in range(0,gs):#
      if p[i]+q[i]==0:
        all_gen[k].append(0)
      else:
        all_gen[k].append(1)
#----------------------------------------------------    
#Mutation(1)
  if M1==0:
    continue
  for k in range(0,10):
    m_p=random.randint(1,round(100/M1))
    if m_p==1:
      for i in range(random.randint(1,round(gs/3))):
        all_gen[k][random.randint(0,gs-1)]=random.randint(0,1) #
#Mutation(2)
  if M2==0:
    continue
  for i in range(0,10):
    m_p1=random.randint(1,round(100/M2))
    m_p2=random.randint(1,10)
    if m_p1==1:
      if m_p2==random.randint(1,10) or random.randint(1,10):
        random.shuffle(all_gen[i])
#----------------------------------------------------      
#result
plt.show()
#----------------------------------------------------
