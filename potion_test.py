#!/usr/bin/python
"""A test suite for potion.py.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

import charisma
import menu
import object_knowledge_repository
import potion

def ExpectEqual(a, b):
  if a != b:
    print 'FAIL'
    print a
    print b

def TestPotionStore(kr):
  ExpectEqual(kr.IsValidPrice('potion', 50), True)
  ExpectEqual(kr.IsValidPrice('potion', 150), True)
  ExpectEqual(kr.IsValidPrice('potion', 300), True)
  ExpectEqual(kr.IsValidPrice('potion', 40), False)
  ExpectEqual(kr.IsValidPrice('potion', 'frog'), False)


def TestGetListPricesFromSalePrice(sell_potion_menu_item):
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(19), set([50]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(25), set([50]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(38), set([100]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(57), set([150]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(75),
              set([150, 200]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(94), set([250]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(100),
              set([200]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(113),
              set([300]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(125),
              set([250]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(150),
              set([300]))

def TestGetListPricesFromBuyPrice(buy_potion_menu_item):
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          100, charisma.Charisma(5).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          75, charisma.Charisma(6).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          99, charisma.Charisma(6).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          66, charisma.Charisma(8).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          88, charisma.Charisma(8).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          50, charisma.Charisma(11).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          66, charisma.Charisma(11).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          38, charisma.Charisma(16).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          50, charisma.Charisma(16).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          34, charisma.Charisma(18).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          44, charisma.Charisma(18).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          25, charisma.Charisma(19).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          33, charisma.Charisma(19).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          100, charisma.Charisma(19).CharismaFactor(), 1.0), set([150, 200]))

def TestGetListPricesFromBuyPriceWithSuckerFactor(buy_potion_menu_item):
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          177, charisma.Charisma(11).CharismaFactor(), 1.33), set([100]))
  ExpectEqual(buy_potion_menu_item.GetListPricesFromBuyPrice(
          266, charisma.Charisma(11).CharismaFactor(), 1.33), set([150, 200]))
  
def TestIdentifyPotionByElimination(kr):
  kr.Identify('potion', 'booze', 'ruby')
  kr.Identify('potion', 'fruit juice', 'pink')
  kr.Identify('potion', 'see invisible', 'orange')
  kr.See('potion', 'yellow')
  kr.AddPriceInformation('potion', 'yellow', set([50]))
  sickness_potion = kr.FindCanonical('potion', 'sickness')
  ExpectEqual(sickness_potion.unidentified_description, 'yellow')


def TestCascadingIdentifyPotionByElimination(kr):
  # 4/5 potions at 150 are known - all but object detection
  kr.Identify('potion', 'blindness', 'ruby')
  kr.Identify('potion', 'gain energy', 'pink')
  kr.Identify('potion', 'invisibility', 'orange')
  kr.Identify('potion', 'monster detection', 'yellow')

  # 4/5 potions at 200 are known - all but speed
  kr.Identify('potion', 'enlightenment', 'emerald')
  kr.Identify('potion', 'full healing', 'dark green')
  kr.Identify('potion', 'levitation', 'cyan')
  kr.Identify('potion', 'polymorph', 'sky blue')

  # one potion is either 150 or 200
  kr.AddPriceInformation('potion', 'brilliant blue', set([150, 200]))

  # nothing should happen here
  object_detection_potion = kr.FindCanonical('potion', 'object detection')
  speed_potion = kr.FindCanonical('potion', 'speed')
  ExpectEqual(object_detection_potion.IsIdentified(), False)
  ExpectEqual(speed_potion.IsIdentified(), False)

  # now we find a potion at 150
  kr.AddPriceInformation('potion', 'magenta', set([150]))

  # we should have seen magenta get matched to object detection and
  # brilliant blue get matched to speed - let's verify
  ExpectEqual(object_detection_potion.IsIdentified(), True)
  ExpectEqual(speed_potion.IsIdentified(), True)
  ExpectEqual(object_detection_potion.unidentified_description, 'magenta')
  ExpectEqual(speed_potion.unidentified_description, 'brilliant blue')


def main():
  kr = object_knowledge_repository.ObjectKnowledgeRepository()
  potion.SetUpPotionClasses(kr)

  menu_looper = menu.MenuLooper()
  sell_potion_menu_item = potion.SellPotionMenuItem(menu_looper, kr)
  buy_potion_menu_item = potion.BuyPotionMenuItem(menu_looper, kr)

  TestPotionStore(kr)
  TestGetListPricesFromSalePrice(sell_potion_menu_item)
  TestGetListPricesFromBuyPrice(buy_potion_menu_item)
  TestGetListPricesFromBuyPriceWithSuckerFactor(buy_potion_menu_item)
  TestIdentifyPotionByElimination(kr)

  kr_2 = object_knowledge_repository.ObjectKnowledgeRepository()
  potion.SetUpPotionClasses(kr_2)
  TestCascadingIdentifyPotionByElimination(kr_2)

if __name__ == '__main__':
  main()
