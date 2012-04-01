"""A framework for nethack objects.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

class NethackObjectClass:
  def __init__(self, identified_description, cost, weight, is_enchantable,
               is_damageable, unidentified_description=None,
               user_assigned_name=None, is_seen=False, is_stackable=True):
    self.identified_description = identified_description
    self.unidentified_description = unidentified_description
    self.cost = cost
    self.weight = weight
    self.is_stackable = is_stackable
    self.is_enchantable = is_enchantable
    self.is_damageable = is_damageable
    self.user_assigned_name = user_assigned_name
    self.is_seen = is_seen


  def IsKnown(self):
    return (self.identified_description != None and
            self.unidentified_description != None)

  def IsEnchantable(self):
    return self.is_enchantable

  def IsDamageable(self):
    return self.is_damageable


BUC_CURSED = -1
BUC_UNCURSED = 0
BUC_BLESSED = 1
BUC_UNKNOWN = None

class BucStatus:
  def __init__(self, status=None):
    self.SetBucStatus(status)

  def ToString(self):
    if self.status == BUC_CURSED:
      return 'cursed'
    if self.status == BUC_UNCURSED:
      return 'uncursed'
    if self.status == BUC_BLESSED:
      return 'blessed'
    if self.status == BUC_UNKNOWN:
      return ''

  def ReduceBucStatus(self):
    if self.status == BUC_UNKNOWN:
      return

    self.status -= 1
    if self.status < BUC_CURSED:
      self.status = BUC_CURSED

  def IncreaseBucStatus(self):
    if self.status == BUC_UNKNOWN:
      return

    self.status += 1
    if self.status > BUC_BLESSED:
      self.status = BUC_BLESSED

  def SetBucStatus(self, status):
    if (status != BUC_CURSED and
        status != BUC_UNCURSED and
        status != BUC_BLESSED and
        status != BUC_UNKNOWN):
      raise Exception('Invalid Status!')
    self.status = status

class NethackObject:
  def __init__(self, nethack_object_class, count=1,
               buc_status=BucStatus(BUC_UNKNOWN), user_assigned_name=None,
               enchantment=None, damage=None):
    self.nethack_object_class = nethack_object_class
    self.count = count
    self.buc_status = buc_status
    self.user_assigned_name = user_assigned_name
    self.enchantment = enchantment
    self.damage = damage

  def IsIdentified(self):
    if (self.nethack_object_class.IsEnchantable() and
        self.enchantment == None):
      return False
    if (self.nethack_object_class.IsDamageable() and
        self.damage == None):
      return False
    if (self.buc_status == BUC_UNKNOWN):
      return False
    return self.nethack_object_class.IsKnown()
               
