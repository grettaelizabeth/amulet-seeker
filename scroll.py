#!/usr/bin/python
"""A system for keeping track of nethack scrolls.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

import charisma
import menu
import object_knowledge_repository
import objects


############################################################################
# ScrollClass
############################################################################


class ScrollClass(objects.NethackObjectClass):
  def __init__(self, identified_description=None, cost=None,
               unidentified_description=None, user_assigned_name=None,
               is_seen=False):
    objects.NethackObjectClass.__init__(self, identified_description, cost,
                                        5, False, False,
                                        unidentified_description,
                                        user_assigned_name, is_seen)


  def IsIdentified(self):
    if self.identified_description and self.unidentified_description:
      return True
    return False


  def See(self):
    self.is_seen = True


############################################################################
# Canonical ScrollClasses
############################################################################

class MailScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'mail', 0)
    self.unidentified_description = 'stamped'

class IdentifyScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'identify', 20)

class LightScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'light', 50)

class BlankPaperScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'blank paper', 60)
    self.unidentified_description = 'unlabeled'

class EnchantWeaponScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'enchant weapon', 60)

class EnchantArmorScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'enchant armor', 80)

class RemoveCurseScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'remove curse', 80)

class ConfuseMonsterScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'confuse monster', 100)

class DestroyArmorScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'destroy armor', 100)

class FireScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'fire', 100)

class FoodDetectionScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'food detection', 100)

class GoldDetectionScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'gold detection', 100)

class MagicMappingScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'magic mapping', 100)

class ScareMonsterScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'scare monster', 100)

class TeleportationScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'teleportation', 100)

class AmnesiaScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'amnesia', 200)

class CreateMonsterScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'create monster', 200)

class EarthScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'earth', 200)

class TamingScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'taming', 200)

class ChargingScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'charging', 300)

class GenocideScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'genocide', 300)

class PunishmentScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'punishment', 300)

class StinkingCloudScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, 'stinking cloud', 300)


############################################################################
# ScrollClass Descriptions
############################################################################

class ZelgoScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='ZELGO MER')

class PratyavayahScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='PRATYAVAYAH')

class ElbibScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='ELBIB YLOH')

class YumScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='YUM YUM')

class AndovaScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='ANDOVA BEGARIN')

class VeloxScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='VELOX NEB')

class ReadScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='READ ME')

class JuyedScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='JUYED AWK YACC')

class DaiyenScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='DAIYEN FOOELS')

class VerrScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='VERR YED HORRE')

class KernodScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='KERNOD WEL')

class KirjeScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='KIRJE')

class FoobieScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='FOOBIE BLETCH')

class NrScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='NR 9')

class LepScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='LEP GEX VEN ZEA')

class VenzarScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='VENZAR BORGAVVE')

class ElamScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='ELAM EBOW')

class VeScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='VE FORBRYDERNE')

class TemovScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='TEMOV')

class XixaxaScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='XIXAXA XOXAXA XUXAXA')

class PrirutsenieScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='PRIRUTSENIE')

class TharrScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='THARR')

class DuamScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='DUAM XNAHT')

class HackemScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='HACKEM MUCHE')

class GarvenScrollClass(ScrollClass):
  def __init__(self):
    ScrollClass.__init__(self, unidentified_description='GARVEN DEH')


############################################################################
# ScrollClassFilter
############################################################################

class ScrollClassFilter():
  def __init__(self, is_seen=False, not_seen=False,
               is_identified=False, not_identified=False):
    if is_seen and not_seen:
      raise Error('Invalid scroll class filter')
    if is_identified and not_identified:
      raise Error('Invalid scroll class filter')
    self.is_seen = is_seen
    self.not_seen = not_seen
    self.is_identified = is_identified
    self.not_identified = not_identified

  def Passes(self, scroll_class):
    if self.is_seen and not scroll_class.is_seen:
      return False
    if self.not_seen and scroll_class.is_seen:
      return False
    if self.is_identified and not scroll_class.IsIdentified():
      return False
    if self.not_identified and scroll_class.IsIdentified():
      return False
    return True


############################################################################
# Scroll
############################################################################


class Scroll(objects.NethackObject):
  def __init__(self, count=1, nethack_object_class=ScrollClass,
           buc_status=objects.BucStatus(objects.BUC_UNKNOWN),
           user_assigned_name=None):
    objects.NethackObject.__init__(self, nethack_object_class, count,
                                   buc_status, user_assigned_name)


############################################################################
# Menu stuff
############################################################################


class GetUnidentifiedScrollTypeMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, type):
    self.type = type
    menu.MenuItem.__init__(self, type, menu_looper)

  def Handle(self):
    return self.type


class GetUnidentifiedScrollTypeMenu(menu.DynamicMenu):
  def __init__(self, menu_looper, kr, scroll_class_filter,
               selection_prompt):
    menu.DynamicMenu.__init__(self)
    self.menu_looper = menu_looper
    self.kr = kr
    self.scroll_class_filter = scroll_class_filter
    self.SetSelectionPrompt(selection_prompt)

  def SetMenuItems(self):
    for scroll_class in self.kr.canonical_classes['scroll']:
      if self.scroll_class_filter.Passes(scroll_class):
        self.AddMenuItem(
          GetUnidentifiedScrollTypeMenuItem(
            self.menu_looper, scroll_class.identified_description))
    self.AddMenuItem(menu.GoBackMenuItem())


class GetUnidentifiedScrollDescriptionMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, description):
    self.description = description
    menu.MenuItem.__init__(self, description, menu_looper)

  def Handle(self):
    return self.description


class GetUnidentifiedScrollDescriptionMenu(menu.DynamicMenu):
  def __init__(self, menu_looper, kr, scroll_class_filter,
               selection_prompt):
    menu.DynamicMenu.__init__(self)
    self.menu_looper = menu_looper
    self.kr = kr
    self.scroll_class_filter = scroll_class_filter
    self.SetSelectionPrompt(selection_prompt)

  def SetMenuItems(self):
    for scroll_class in self.kr.unidentified_classes['scroll']:
      if self.scroll_class_filter.Passes(scroll_class):
        self.AddMenuItem(
          GetUnidentifiedScrollDescriptionMenuItem(
            self.menu_looper, scroll_class.unidentified_description))
    self.AddMenuItem(menu.GoBackMenuItem())


class SawScrollMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'See a scroll', menu_looper)
    self.kr = kr


  def Handle(self):
    scroll_unseen_filter = ScrollClassFilter(not_seen=True)
    desc_menu = GetUnidentifiedScrollDescriptionMenu(self.menu_looper,
      self.kr, scroll_unseen_filter,
      'What was the label on the scroll you saw? ')
    description = desc_menu.GetPlayerSelection()
    if description != False:
      self.kr.See('scroll', description)
    print
    self.menu_looper.ReturnToTop()


class IdentifyScrollMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Identify a scroll', menu_looper)
    self.kr = kr

  def Handle(self):
    scroll_unidentified_filter = ScrollClassFilter(not_identified=True)
    type_menu = GetUnidentifiedScrollTypeMenu(
      self.menu_looper, self.kr, scroll_unidentified_filter,
      'What type of scroll did you identify? ')
    scroll_type = type_menu.GetPlayerSelection()
    if scroll_type == False:
      return

    desc_menu = GetUnidentifiedScrollDescriptionMenu(
      self.menu_looper, self.kr, scroll_unidentified_filter,
      'What label did the scroll have on it? ')
    description = desc_menu.GetPlayerSelection()
    if description == False:
      return

    self.kr.Identify('scroll', scroll_type, description)
    print
    self.menu_looper.ReturnToTop()


# Player is selling something to a shopkeeper
class SellScrollMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Put a scroll up for sale', menu_looper)
    self.kr = kr

  def Handle(self):
    seen_filter = ScrollClassFilter(is_seen=True)
    desc_menu = GetUnidentifiedScrollDescriptionMenu(self.menu_looper,
      self.kr, seen_filter,
      'What was the label on the scroll you put up for sale? ')
    description = desc_menu.GetPlayerSelection()
    if description == False:
      return

    # actually all of this is going to get bubbled up to a generic
    # selling library eventually, but for now we'll do it here in the
    # scroll code.

    sale_price = int(raw_input('What sale price was offered? '))

    self.kr.AddPriceInformation('scroll', description,
      self.GetListPricesFromSalePrice(sale_price))

    self.menu_looper.ReturnToTop()

  # this definitely doesn't belong here
  def GetListPricesFromSalePrice(self, sale_price):
    prices = []
    list_price = int(2.0 * sale_price)
    for price in [list_price, list_price - 1]:
      if self.kr.IsValidPrice('scroll', price):
        prices.append(price)
      shop_markup_price = int(price * 1.334)
      for shop_price in [shop_markup_price, shop_markup_price - 1]:
        if self.kr.IsValidPrice('scroll', shop_price):
          prices.append(shop_price)
    return set(prices)


# Player is buying something from a shopkeeper
class BuyScrollMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Buy a scroll', menu_looper)
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
    null_filter = ScrollClassFilter()
    desc_menu = GetUnidentifiedScrollDescriptionMenu(self.menu_looper,
      self.kr, null_filter,
      'What was the label on the scroll you offered to buy? ')
    description = desc_menu.GetPlayerSelection()
    if description == False:
      return

    # actually all this is going to get bubbled up to a generic
    # buying library eventually, but for now we'll do it here in the
    # scroll code.

    buy_price = int(raw_input('What buy price was offered? '))

    player_charisma = charisma.Charisma(
      int(raw_input('What is your charisma? ')))
    charisma_factor = player_charisma.CharismaFactor()

    sucker_factor = self.GetSuckerFactor()

    self.kr.AddPriceInformation('scroll', description,
      self.GetListPricesFromBuyPrice(buy_price, charisma_factor,
                                     sucker_factor))
    self.menu_looper.ReturnToTop()

  # this definitely doesn't belong here
  def GetListPricesFromBuyPrice(self, buy_price, charisma_factor,
                                sucker_factor):
    list_price = int(buy_price / (charisma_factor * sucker_factor))
    prices = []
    for price in [list_price, list_price + 1]:
      if self.kr.IsValidPrice('scroll', price):
        prices.append(price)
      shop_markup_price = int(price / 1.333)
      for shop_price in [shop_markup_price, shop_markup_price + 1]:
        if self.kr.IsValidPrice('scroll', shop_price):
          prices.append(shop_price)
    return set(prices)

class ShowScrollInfoMenuItem(menu.MenuItem):
  def __init__(self, menu_looper, kr):
    menu.MenuItem.__init__(self, 'Show all scroll information', menu_looper)
    self.kr = kr

  def Handle(self):
    self.kr.PrintCanonicalObjects('scroll')
    self.kr.PrintUnidentifiedObjects('scroll')
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

def SetUpScrollClasses(kr):
  canonical_scroll_classes = [
    MailScrollClass(),
    IdentifyScrollClass(),
    LightScrollClass(),
    BlankPaperScrollClass(),
    EnchantWeaponScrollClass(),
    EnchantArmorScrollClass(),
    RemoveCurseScrollClass(),
    ConfuseMonsterScrollClass(),
    DestroyArmorScrollClass(),
    FireScrollClass(),
    FoodDetectionScrollClass(),
    GoldDetectionScrollClass(),
    MagicMappingScrollClass(),
    ScareMonsterScrollClass(),
    TeleportationScrollClass(),
    AmnesiaScrollClass(),
    CreateMonsterScrollClass(),
    EarthScrollClass(),
    TamingScrollClass(),
    ChargingScrollClass(),
    GenocideScrollClass(),
    PunishmentScrollClass(),
    StinkingCloudScrollClass(),
  ]
  unidentified_scroll_classes = [
    ZelgoScrollClass(),
    PratyavayahScrollClass(),
    ElbibScrollClass(),
    YumScrollClass(),
    AndovaScrollClass(),
    VeloxScrollClass(),
    ReadScrollClass(),
    JuyedScrollClass(),
    DaiyenScrollClass(),
    VerrScrollClass(),
    KernodScrollClass(),
    KirjeScrollClass(),
    FoobieScrollClass(),
    NrScrollClass(),
    LepScrollClass(),
    VenzarScrollClass(),
    ElamScrollClass(),
    VeScrollClass(),
    TemovScrollClass(),
    XixaxaScrollClass(),
    PrirutsenieScrollClass(),
    TharrScrollClass(),
    DuamScrollClass(),
    HackemScrollClass(),
    GarvenScrollClass(),
  ]
  kr.SetClasses('scroll', canonical_scroll_classes,
                unidentified_scroll_classes)


def main():
  kr = object_knowledge_repository.ObjectKnowledgeRepository()
  SetUpScrollClasses(kr)

  menu_looper = menu.MenuLooper()

  scroll_menu = menu.Menu()
  scroll_menu.AddMenuItem(SawScrollMenuItem(menu_looper, kr))
  scroll_menu.AddMenuItem(IdentifyScrollMenuItem(menu_looper, kr))
  scroll_menu.AddMenuItem(SellScrollMenuItem(menu_looper, kr))
  scroll_menu.AddMenuItem(BuyScrollMenuItem(menu_looper, kr))
  scroll_menu.AddMenuItem(ShowScrollInfoMenuItem(menu_looper, kr))
  scroll_menu.AddMenuItem(menu.ReturnToTopMenuItem(menu_looper))

  main_menu = menu.Menu()
  main_menu.AddMenuItem(menu.SubMenuMenuItem('Work on identifying scrolls',
                                             menu_looper, scroll_menu))
  main_menu.AddMenuItem(SaveToFileMenuItem(menu_looper, kr))
  main_menu.AddMenuItem(LoadFromFileMenuItem(menu_looper, kr))
  main_menu.AddMenuItem(menu.QuitMenuItem(menu_looper))

  menu_looper.SetTopMenu(main_menu)
  menu_looper.ReturnToTop()
  menu_looper.Loop()


if __name__ == '__main__':
  main()
