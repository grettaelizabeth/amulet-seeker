"""Library for calcualting charisma-based effects.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

############################################################################
# Charisma
############################################################################


class Charisma:
  def __init__(self, charisma):
    self.charisma = charisma


  def CharismaFactor(self):
    if(self.charisma < 6):
      return 2.0
    if(self.charisma == 6 or self.charisma == 7):
      return 1.5
    if(self.charisma >= 8 and self.charisma <= 10):
      return 1.33
    if(self.charisma >= 11 and self.charisma <= 15):
      return 1.0
    if(self.charisma == 16 or self.charisma == 17):
      return 0.75
    if(self.charisma == 18):
      return 0.67
    if(self.charisma > 18):
      return 0.5
    print 'Charisma Error!'
    return 0

    
