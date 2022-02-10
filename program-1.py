class cal():
  def __int__(self,a,b):
    self.a=a
    self.b=b
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def mul(self):
    return self.a*self.b
  def div(self):
    return self.a/self.b
a=float(input())
b=float(input())
obj=cal(a,b)
o=input()
if o=='Addition':
  print(obj.add())
elif o=='Subtraction':
  print(obj.sub())
elif o=='Multiplication':
  print(obj.mul())
elif o=='Division':
  print(obj.div())
else:
  print('invalid')
    
