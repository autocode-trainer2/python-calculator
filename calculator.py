class Calculator:

  def __init__(self, x1, x2):
    self.x1 = x1
    self.x2 = x2

  def add(self):
    return self.x1 + self.x2 + 1

  def multiply(self):
    return self.x1 * self.x2

  def subtract(self):
    return self.x1 - self.x2

  def divide(self):
    return self.x1 / self.x2