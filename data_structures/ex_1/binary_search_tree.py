class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    if not self.left:
      if not self.right:
        return cb(self.value)
      
      cb(self.value)
      return self.right.depth_first_for_each(cb)
      
    cb(self.value)
    self.left.depth_first_for_each(cb)
    self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    nextVisit = []
    cb(self.value)
    self.recurseBF(cb, nextVisit)
    
  def recurseBF(self, cb, nextVisit):
    if self.right:
      nextVisit.append(self.right)
    
    if self.left:
      nextVisit.append(self.left)
    
    while len(nextVisit) > 0:
      pop = nextVisit.pop()
      cb(pop.value)
    
    if self.left:
      self.left.recurseBF(cb, nextVisit)
    
    if self.right:
      self.right.recurseBF(cb, nextVisit)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
