#!/usr/bin/python
"""A test suite for potion.py.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

import charisma
import menu
import potion

def ExpectEqual(a, b):
  if a != b:
    print 'FAIL'
    print a
    print b

def TestPotionStore(potion_store):
  ExpectEqual(potion_store.IsValidPrice(50), True)
  ExpectEqual(potion_store.IsValidPrice(150), True)
  ExpectEqual(potion_store.IsValidPrice(300), True)
  ExpectEqual(potion_store.IsValidPrice(40), False)
  ExpectEqual(potion_store.IsValidPrice('frog'), False)


def TestGetListPricesFromSalePrice(sell_potion_menu_item):
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          19, 1.0), set([50]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          25, 1.0), set([50]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          38, 1.0), set([100]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          57, 1.0), set([150]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          75, 1.0), set([150, 200]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          94, 1.0), set([250]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          100, 1.0), set([200]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          113, 1.0), set([300]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          125, 1.0), set([250]))
  ExpectEqual(sell_potion_menu_item.GetListPricesFromSalePrice(
          150, 1.0), set([300]))


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

def TestIdentifyPotionByElimination(potion_store):
  potion_store.Identify('booze', 'ruby')
  potion_store.Identify('fruit juice', 'pink')
  potion_store.Identify('see invisible', 'orange')
  potion_store.See('yellow')
  potion_store.AddPriceInformation('yellow', set([50]))
  sickness_potion = potion_store.FindCanonical('sickness')
  ExpectEqual(sickness_potion.unidentified_description, 'yellow')


def TestCascadingIdentifyPotionByElimination(potion_store):
  # 4/5 potions at 150 are known - all but object detection
  potion_store.Identify('blindness', 'ruby')
  potion_store.Identify('gain energy', 'pink')
  potion_store.Identify('invisibility', 'orange')
  potion_store.Identify('monster detection', 'yellow')

  # 4/5 potions at 200 are known - all but speed
  potion_store.Identify('enlightenment', 'emerald')
  potion_store.Identify('full healing', 'dark green')
  potion_store.Identify('levitation', 'cyan')
  potion_store.Identify('polymorph', 'sky blue')

  # one potion is either 150 or 200
  potion_store.AddPriceInformation('brilliant blue', set([150, 200]))

  # nothing should happen here
  object_detection_potion = potion_store.FindCanonical('object detection')
  speed_potion = potion_store.FindCanonical('speed')
  ExpectEqual(object_detection_potion.IsIdentified(), False)
  ExpectEqual(speed_potion.IsIdentified(), False)

  # now we find a potion at 150
  potion_store.AddPriceInformation('magenta', set([150]))

  # we should have seen magenta get matched to object detection and
  # brilliant blue get matched to speed - let's verify
  ExpectEqual(object_detection_potion.IsIdentified(), True)
  ExpectEqual(speed_potion.IsIdentified(), True)
  ExpectEqual(object_detection_potion.unidentified_description, 'magenta')
  ExpectEqual(speed_potion.unidentified_description, 'brilliant blue')


def main():
  potion_store = potion.PotionStore()
  menu_looper = menu.MenuLooper()
  sell_potion_menu_item = potion.SellPotionMenuItem(menu_looper, potion_store)
  buy_potion_menu_item = potion.BuyPotionMenuItem(menu_looper, potion_store)

  TestPotionStore(potion_store)
  TestGetListPricesFromSalePrice(sell_potion_menu_item)
  TestGetListPricesFromBuyPrice(buy_potion_menu_item)
  TestIdentifyPotionByElimination(potion_store)

  potion_store_2 = potion.PotionStore()
  TestCascadingIdentifyPotionByElimination(potion_store_2)

if __name__ == '__main__':
  main()
