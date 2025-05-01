class EmpIDError(Exception):
  def __init__(self,msg):
    self.msg=msg

def data(id):
  if id==1001:
    print('Valid EMP')
  else:
    raise EmpIDError ('Hey plx enter valid ID')
data(5)
