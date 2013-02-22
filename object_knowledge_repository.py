#!/usr/bin/python
"""A system for keeping track of what we know about objects."""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

import objects
import pickle

class ObjectKnowledgeRepository:
  """Stores everything we know about every type of object in the game.

  Attributes:
  version: The version of the object, for serialization purposes.
  canonical_classes: a dict, keyed by object type, with one class for each
    of the subtypes of this type.  For example, canonical_classes['potion']
    contains one BoozePotion, one LevitationPotion, and so on.
  unidentified_classes: a dict, keyed by object type, with one class for
    each of the unidentified subtypes of this type.  For example,
    unidentified_classes['potion'] starts out containing one RubyPotion, one
    BrilliantBluePotion, and so on.
  price_bands: a dict, keyed by object type and then by list price, of all
    the canonical objects of this type.  For example,
    price_bands['potion'][50] contains BoozePotion, FruitJuicePotion,
    SeeInvisiblePotion, and SicknessPotion.
  """

  def __init__(self):
    self.version = 1
    self.canonical_classes = { }
    self.unidentified_classes = { }
    self.price_bands = { }


  def SetClasses(self, object_type, canonical_classes, unidentified_classes):
    self.canonical_classes[object_type] = canonical_classes
    self.unidentified_classes[object_type] = unidentified_classes
    self.InitPriceBands(object_type)


  def InitPriceBands(self, object_type):
    self.price_bands[object_type] = { }
    for object_class in self.canonical_classes[object_type]:
      try:
        self.price_bands[object_type][object_class.cost].append(object_class)
      except KeyError:
        self.price_bands[object_type][object_class.cost] = [object_class]


  def SaveToFile(self, filename):
    output_file = open(filename, 'wb')
    pickle.dump(self.version, output_file)
    pickle.dump(self.canonical_classes, output_file)
    pickle.dump(self.unidentified_classes, output_file)
    pickle.dump(self.price_bands, output_file)
    output_file.close()


  def LoadFromFile(self, filename):
    input_file = open(filename, 'rb')
    try:
      version = pickle.load(input_file)
    except:
      print "Can't read this file!"
      return
    if version != self.version:
      print "File version does not match!  Can't load this file."
      return
    try:
      self.canonical_classes = pickle.load(input_file)
      self.unidentified_classes = pickle.load(input_file)
      self.price_bands = pickle.load(input_file)
      return
    except:
      print "Can't read this file!"
    input_file.close()


  def See(self, object_type, description):
    object_class = self.FindUnidentified(object_type, description)
    object_class.See()


  def FindUnidentified(self, object_type, description):
    for object_class in self.unidentified_classes[object_type]:
      if object_class.unidentified_description == description:
        return object_class
    return None


  def FindCanonical(self, object_type, object_subtype):
    for object_class in self.canonical_classes[object_type]:
      if object_class.identified_description == object_subtype:
        return object_class
    return None


  def Merge(self, object_type, canonical_class, unidentified_class):
    canonical_class.unidentified_description = \
      unidentified_class.unidentified_description
    canonical_class.user_assigned_name = \
      unidentified_class.user_assigned_name
    canonical_class.is_seen = True
    self.unidentified_classes[object_type].remove(unidentified_class)

  
  def Identify(self, object_type, object_subtype, description):
    canonical_class = self.FindCanonical(object_type, object_subtype)
    if canonical_class == None:
      print 'That %s type does not exist.' % object_type
      return
    unidentified_class = self.FindUnidentified(object_type, description)
    if unidentified_class == None:
      print 'That %s has already been identified.' % object_type
      return
    self.Merge(object_type, canonical_class, unidentified_class)
    self.CollapsePriceBands(object_type)


  def IsValidPrice(self, object_type, price):
    return self.price_bands[object_type].has_key(price)


  def CollapsePriceBands(self, object_type):
    change = True
    while change == True:
      change = False
      for cost, object_classes in self.price_bands[object_type].iteritems():
        num_unidentified = 0
        for object_class in object_classes:
          if not object_class.IsIdentified():
            num_unidentified = num_unidentified + 1
            canonical_class = object_class
        # if there is only one unidentified class in this price band,
        # and we know an unidentified class at that price, identify it
        if num_unidentified == 1:
          for object_class in self.unidentified_classes[object_type]:
            if object_class.cost == cost:
              self.Merge(object_type, canonical_class, object_class)
              print 'By process of elimination, %s is %s!' % (
                canonical_class.unidentified_description,
                canonical_class.identified_description)
              change = True
        # if there are no unidentified classes in this price band,
        # eliminate this price as a possible price for other classes
        if num_unidentified == 0:
          for object_class in self.unidentified_classes[object_type]:
            if type(object_class.cost) == set and cost in object_class.cost:
              object_class.cost.remove(cost)
              if len(object_class.cost) == 1:
                object_class.cost = object_class.cost.pop()
              print '%s can\'t cost %d' % (
                object_class.unidentified_description, cost)
              change = True


  def AddPriceInformation(self, object_type, description, list_prices):
    unidentified_class = self.FindUnidentified(object_type, description)
    if len(list_prices) == 1:
      unidentified_class.cost = list_prices.pop()
      print "The %s %s's list price is %d" % (
        description, object_type, unidentified_class.cost)
      self.CollapsePriceBands(object_type)
    else:
      unidentified_class.cost = list_prices
      print "The %s %s's list price is one of %s" % (
        description, object_type, unidentified_class.cost)


  def PrintCanonicalObjects(self, object_type):
    print 'Canonical %ss:' % object_type
    for cost, object_classes in sorted(
        self.price_bands[object_type].iteritems()):
      print '  %d' % cost
      for object_class in object_classes:
        unidentified_description = object_class.unidentified_description
        if unidentified_description == None:
          unidentified_description = '?'
        print '    %s - %s' % (object_class.identified_description,
                             unidentified_description)

  def PrintUnidentifiedObjects(self, object_type):
    print 'Unidentified %ss:' % object_type
    for object_class in self.unidentified_classes[object_type]:
      is_seen = ''
      if object_class.is_seen == True:
        is_seen = '(seen)'
      cost = ''
      if object_class.cost != None:
        if type(object_class.cost) == set:
          cost = '(ambiguous cost)'
        else:
          cost = '(%d)' % object_class.cost
      print '  %s %s %s' % (object_class.unidentified_description,
                            is_seen, cost)

