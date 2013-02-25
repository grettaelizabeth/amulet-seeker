#!/usr/bin/python
"""A system for keeping track of nethack potions."""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

import charisma
import menu
import object_knowledge_repository
import objects


############################################################################
# PotionClass
############################################################################


class PotionClass(objects.NethackObjectClass):
  def __init__(self, identified_description=None, cost=None,
               unidentified_description=None, user_assigned_name=None,
               is_seen=False):
    objects.NethackObjectClass.__init__(self, identified_description, cost,
                                        20, False, False,
                                        unidentified_description,
                                        user_assigned_name, is_seen)


  def IsIdentified(self):
    if self.identified_description and self.unidentified_description:
      return True
    return False


  def See(self):
    self.is_seen = True


############################################################################
# Canonical PotionClasses
############################################################################


class BoozePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'booze', 50)

class FruitJuicePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'fruit juice', 50)

class SeeInvisiblePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'see invisible', 50)

class SicknessPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'sickness', 50)

class ConfusionPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'confusion', 100)

class ExtraHealingPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'extra healing', 100)

class HallucinationPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'hallucination', 100)

class HealingPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'healing', 100)

class RestoreAbilityPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'restore ability', 100)

class SleepingPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'sleeping', 100)

class WaterPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'water', 100)
    self.unidentified_description = 'clear'

class BlindnessPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'blindness', 150)

class GainEnergyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'gain energy', 150)

class InvisibilityPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'invisibility', 150)

class MonsterDetectionPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'monster detection', 150)

class ObjectDetectionPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'object detection', 150)

class EnlightenmentPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'enlightenment', 200)

class FullHealingPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'full healing', 200)

class LevitationPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'levitation', 200)

class PolymorphPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'polymorph', 200)

class SpeedPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'speed', 200)

class AcidPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'acid', 250)

class OilPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'oil', 250)

class GainAbilityPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'gain ability', 300)

class GainLevelPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'gain level', 300)

class ParalysisPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, 'paralysis', 300)

############################################################################
# PotionClass Descriptions
############################################################################

class RubyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='ruby')

class PinkPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='pink')

class OrangePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='orange')

class YellowPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='yellow')

class EmeraldPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='emerald')

class DarkGreenPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='dark green')

class CyanPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='cyan')

class SkyBluePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='sky blue')

class BrilliantBluePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='brilliant blue')

class MagentaPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='magenta')

class PurpleRedPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='purple-red')

class PucePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='puce')

class MilkyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='milky')

class SwirlyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='swirly')

class BubblyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='bubbly')

class SmokyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='smoky')

class CloudyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='cloudy')

class EffervescentPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='effervescent')

class BlackPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='black')

class GoldenPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='golden')

class BrownPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='brown')

class FizzyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='fizzy')

class DarkPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='dark')

class WhitePotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='white')

class MurkyPotionClass(PotionClass):
  def __init__(self):
    PotionClass.__init__(self, unidentified_description='murky')


############################################################################
# PotionClassFilter
############################################################################

class PotionClassFilter():
  def __init__(self, is_seen=False, not_seen=False,
               is_identified=False, not_identified=False):
    if is_seen and not_seen:
      raise Error('Invalid potion class filter')
    if is_identified and not_identified:
      raise Error('Invalid potion class filter')
    self.is_seen = is_seen
    self.not_seen = not_seen
    self.is_identified = is_identified
    self.not_identified = not_identified

  def Passes(self, potion_class):
    if self.is_seen and not potion_class.is_seen:
      return False
    if self.not_seen and potion_class.is_seen:
      return False
    if self.is_identified and not potion_class.IsIdentified():
      return False
    if self.not_identified and potion_class.IsIdentified():
      return False
    return True


############################################################################
# Potion
############################################################################


class Potion(objects.NethackObject):
  def __init__(self, count=1, nethack_object_class=PotionClass,
           buc_status=objects.BucStatus(objects.BUC_UNKNOWN),
           user_assigned_name=None, diluted=False):
    objects.NethackObject.__init__(self, nethack_object_class, count,
                                   buc_status, user_assigned_name)
    self.diluted = diluted


############################################################################
# Menu stuff
############################################################################


class GetUnidentifiedPotionTypeMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, type):
    self.type = type
    menu.MenuItem.__init__(self, type, menu_looper)

  def Handle(self):
    return self.type


class GetUnidentifiedPotionTypeMenu(menu.DynamicMenu):
  def __init__(self, menu_looper, kr, potion_class_filter,
               selection_prompt):
    menu.DynamicMenu.__init__(self)
    self.menu_looper = menu_looper
    self.kr = kr
    self.potion_class_filter = potion_class_filter
    self.SetSelectionPrompt(selection_prompt)

  def SetMenuItems(self):
    for potion_class in self.kr.canonical_classes['potion']:
      if self.potion_class_filter.Passes(potion_class):
        self.AddMenuItem(
          GetUnidentifiedPotionTypeMenuItem(
            self.menu_looper, potion_class.identified_description))
    self.AddMenuItem(menu.GoBackMenuItem())


class GetUnidentifiedPotionDescriptionMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, description):
    self.description = description
    menu.MenuItem.__init__(self, description, menu_looper)

  def Handle(self):
    return self.description


class GetUnidentifiedPotionDescriptionMenu(menu.DynamicMenu):
  def __init__(self, menu_looper, kr, potion_class_filter,
               selection_prompt):
    menu.DynamicMenu.__init__(self)
    self.menu_looper = menu_looper
    self.kr = kr
    self.potion_class_filter = potion_class_filter
    self.SetSelectionPrompt(selection_prompt)

  def SetMenuItems(self):
    for potion_class in self.kr.unidentified_classes['potion']:
      if self.potion_class_filter.Passes(potion_class):
        self.AddMenuItem(
          GetUnidentifiedPotionDescriptionMenuItem(
            self.menu_looper, potion_class.unidentified_description))
    self.AddMenuItem(menu.GoBackMenuItem())


class SawPotionMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'See a potion', menu_looper)
    self.kr = kr


  def Handle(self):
    potion_unseen_filter = PotionClassFilter(not_seen=True)
    desc_menu = GetUnidentifiedPotionDescriptionMenu(self.menu_looper,
      self.kr, potion_unseen_filter,
      'What color potion did you see? ')
    description = desc_menu.GetPlayerSelection()
    if description != False:
      self.kr.See('potion', description)
    print
    self.menu_looper.ReturnToTop()


class IdentifyPotionMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Identify a potion', menu_looper)
    self.kr = kr

  def Handle(self):
    potion_unidentified_filter = PotionClassFilter(not_identified=True)
    type_menu = GetUnidentifiedPotionTypeMenu(
      self.menu_looper, self.kr, potion_unidentified_filter,
      'What type of potion did you identify? ')
    potion_type = type_menu.GetPlayerSelection()
    if potion_type == False:
      return

    desc_menu = GetUnidentifiedPotionDescriptionMenu(
      self.menu_looper, self.kr, potion_unidentified_filter,
      'What color potion was it? ')
    description = desc_menu.GetPlayerSelection()
    if description == False:
      return

    self.kr.Identify('potion', potion_type, description)
    print
    self.menu_looper.ReturnToTop()


# Player is selling something to a shopkeeper
class SellPotionMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Put a potion up for sale', menu_looper)
    self.kr = kr

  def Handle(self):
    seen_filter = PotionClassFilter(is_seen=True)
    desc_menu = GetUnidentifiedPotionDescriptionMenu(self.menu_looper,
      self.kr, seen_filter,
      'What color potion did you put up for sale? ')
    description = desc_menu.GetPlayerSelection()
    if description == False:
      return

    # actually all of this is going to get bubbled up to a generic
    # selling library eventually, but for now we'll do it here in the
    # potion code.

    sale_price = int(raw_input('What sale price was offered? '))

    self.kr.AddPriceInformation('potion', description,
                                self.GetListPricesFromSalePrice(sale_price))

    self.menu_looper.ReturnToTop()

  # this definitely doesn't belong here
  def GetListPricesFromSalePrice(self, sale_price):
    prices = []
    list_price = int(2.0 * sale_price)
    for price in [list_price, list_price - 1]:
      if self.kr.IsValidPrice('potion', price):
        prices.append(price)
      shop_markup_price = int(price * 1.334)
      for shop_price in [shop_markup_price, shop_markup_price - 1]:
        if self.kr.IsValidPrice('potion', shop_price):
          prices.append(shop_price)
    return set(prices)


# Player is buying something from a shopkeeper
class BuyPotionMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Buy a potion', menu_looper)
    self.kr = kr

  # this definitely doesn't belong here
  # input needs to be validated better, should create y/n question function
  def GetSuckerFactor(self):
    sucker_factor = 1.0
    if ((raw_input(
           'Are you a tourist of level 15 or less? (y/n) ') == 'y') or
        (raw_input(
           'Are you wearing a visible Hawaiian shirt? (y/n) ') == 'y') or
        (raw_input(
           'Are you wearing a visible T-Shirt? (y/n) ') == 'y')):
      sucker_factor = 1.33
    return sucker_factor

  def Handle(self):
    null_filter = PotionClassFilter()
    desc_menu = GetUnidentifiedPotionDescriptionMenu(self.menu_looper,
      self.kr, null_filter,
      'What color potion did you offer to buy? ')
    description = desc_menu.GetPlayerSelection()
    if description == False:
      return

    # actually all this is going to get bubbled up to a generic
    # buying library eventually, but for now we'll do it here in the
    # potion code.

    buy_price = int(raw_input('What buy price was offered? '))

    player_charisma = charisma.Charisma(
      int(raw_input('What is your charisma? ')))
    charisma_factor = player_charisma.CharismaFactor()

    sucker_factor = self.GetSuckerFactor()

    self.kr.AddPriceInformation('potion', description,
                                self.GetListPricesFromBuyPrice(buy_price,
                                                               charisma_factor,
                                                               sucker_factor))
    self.menu_looper.ReturnToTop()

  # this definitely doesn't belong here
  def GetListPricesFromBuyPrice(self, buy_price, charisma_factor,
                                sucker_factor):
    list_price = int(buy_price / (charisma_factor * sucker_factor))
    prices = []
    for price in [list_price, list_price + 1]:
      if self.kr.IsValidPrice('potion', price):
        prices.append(price)
      shop_markup_price = int(price / 1.333)
      for shop_price in [shop_markup_price, shop_markup_price + 1]:
        if self.kr.IsValidPrice('potion', shop_price):
          prices.append(shop_price)
    return set(prices)

class ShowPotionInfoMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Show all potion information', menu_looper)
    self.kr = kr

  def Handle(self):
    self.kr.PrintCanonicalObjects('potion')
    self.kr.PrintUnidentifiedObjects('potion')
    print
    self.menu_looper.ReturnToTop()


class SaveToFileMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Save state to file', menu_looper)
    self.kr = kr

  def Handle(self):
    filename = raw_input('File to save to: ')
    self.kr.SaveToFile(filename)
    print
    self.menu_looper.ReturnToTop()


class LoadFromFileMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self,
                           'Load state from file (current state will be lost!)',
                           menu_looper)
    self.kr = kr

  def Handle(self):
    filename = raw_input('File to load from: ')
    self.kr.LoadFromFile(filename)
    print
    self.menu_looper.ReturnToTop()


############################################################################
# main
############################################################################

def SetUpPotionClasses(kr):
  canonical_potion_classes = [
    BoozePotionClass(),
    FruitJuicePotionClass(),
    SeeInvisiblePotionClass(),
    SicknessPotionClass(),
    ConfusionPotionClass(),
    ExtraHealingPotionClass(),
    HallucinationPotionClass(),
    HealingPotionClass(),
    RestoreAbilityPotionClass(),
    SleepingPotionClass(),
    WaterPotionClass(),
    BlindnessPotionClass(),
    GainEnergyPotionClass(),
    InvisibilityPotionClass(),
    MonsterDetectionPotionClass(),
    ObjectDetectionPotionClass(),
    EnlightenmentPotionClass(),
    FullHealingPotionClass(),
    LevitationPotionClass(),
    PolymorphPotionClass(),
    SpeedPotionClass(),
    AcidPotionClass(),
    OilPotionClass(),
    GainAbilityPotionClass(),
    GainLevelPotionClass(),
    ParalysisPotionClass(),
  ]
  unidentified_potion_classes = [
    RubyPotionClass(),
    PinkPotionClass(),
    OrangePotionClass(),
    YellowPotionClass(),
    EmeraldPotionClass(),
    DarkGreenPotionClass(),
    CyanPotionClass(),
    SkyBluePotionClass(),
    BrilliantBluePotionClass(),
    MagentaPotionClass(),
    PurpleRedPotionClass(),
    PucePotionClass(),
    MilkyPotionClass(),
    SwirlyPotionClass(),
    BubblyPotionClass(),
    SmokyPotionClass(),
    CloudyPotionClass(),
    EffervescentPotionClass(),
    BlackPotionClass(),
    GoldenPotionClass(),
    BrownPotionClass(),
    FizzyPotionClass(),
    DarkPotionClass(),
    WhitePotionClass(),
    MurkyPotionClass()
  ]
  kr.SetClasses('potion', canonical_potion_classes,
                unidentified_potion_classes)


def main():
  kr = object_knowledge_repository.ObjectKnowledgeRepository()
  SetUpPotionClasses(kr)

  menu_looper = menu.MenuLooper()

  potion_menu = menu.Menu()
  potion_menu.AddMenuItem(SawPotionMenuItem(menu_looper, kr))
  potion_menu.AddMenuItem(IdentifyPotionMenuItem(menu_looper, kr))
  potion_menu.AddMenuItem(SellPotionMenuItem(menu_looper, kr))
  potion_menu.AddMenuItem(BuyPotionMenuItem(menu_looper, kr))
  potion_menu.AddMenuItem(ShowPotionInfoMenuItem(menu_looper, kr))
  potion_menu.AddMenuItem(menu.ReturnToTopMenuItem(menu_looper))

  main_menu = menu.Menu()
  main_menu.AddMenuItem(menu.SubMenuMenuItem('Work on identifying potions',
                                             menu_looper, potion_menu))
  main_menu.AddMenuItem(SaveToFileMenuItem(menu_looper, kr))
  main_menu.AddMenuItem(LoadFromFileMenuItem(menu_looper, kr))
  main_menu.AddMenuItem(menu.QuitMenuItem(menu_looper))

  menu_looper.SetTopMenu(main_menu)
  menu_looper.ReturnToTop()
  menu_looper.Loop()


if __name__ == '__main__':
  main()
