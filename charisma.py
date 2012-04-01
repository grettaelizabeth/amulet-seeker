"""Library for calcualting charisma-based effects.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

############################################################################
# Charisma
############################################################################


class Charisma:
  def __init__(self, charisma):
    self.charisma = charisma


  # fix these to be right
  def CharismaFactor(self):
    if(self.charisma <= 7):
      return 0.5
    if(self.charisma == 8 or self.charisma == 9):
      return 0.666
    if(self.charisma == 10 or self.charisma == 11):
      return 0.75
    if(self.charisma >= 12 and self.charisma <= 15):
      return 1.0
    if(self.charisma == 16 or self.charisma == 17):
      return 1.25
    if(self.charisma >= 18):
      return 1.33
    print 'Charisma Error!'
    return 0

    
