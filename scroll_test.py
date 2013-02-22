#!/usr/bin/python
"""A test suite for scroll.py.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'

import charisma
import menu
import scroll

def ExpectEqual(a, b):
  if a != b:
    print 'FAIL'
    print a
    print b

def TestScrollStore(scroll_store):
  ExpectEqual(scroll_store.IsValidPrice(50), True)
  ExpectEqual(scroll_store.IsValidPrice(100), True)
  ExpectEqual(scroll_store.IsValidPrice(300), True)
  ExpectEqual(scroll_store.IsValidPrice(40), False)
  ExpectEqual(scroll_store.IsValidPrice('frog'), False)


def TestGetListPricesFromSalePrice(sell_scroll_menu_item):
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(8), set([20]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(10), set([20]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(19), set([50]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(25), set([50]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(30),
              set([60, 80]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(38), set([100]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(75), set([200]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(100),
              set([200]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(113),
              set([300]))
  ExpectEqual(sell_scroll_menu_item.GetListPricesFromSalePrice(150),
              set([300]))

def TestGetListPricesFromBuyPrice(buy_scroll_menu_item):
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          100, charisma.Charisma(5).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          75, charisma.Charisma(6).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          99, charisma.Charisma(6).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          66, charisma.Charisma(8).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          88, charisma.Charisma(8).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          50, charisma.Charisma(11).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          66, charisma.Charisma(11).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          38, charisma.Charisma(16).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          50, charisma.Charisma(16).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          34, charisma.Charisma(18).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          44, charisma.Charisma(18).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          25, charisma.Charisma(19).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          33, charisma.Charisma(19).CharismaFactor(), 1.0), set([50]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          80, charisma.Charisma(11).CharismaFactor(), 1.0), set([60, 80]))

def TestGetListPricesFromBuyPriceWithSuckerFactor(buy_scroll_menu_item):
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          106, charisma.Charisma(11).CharismaFactor(), 1.33), set([60, 80]))
  ExpectEqual(buy_scroll_menu_item.GetListPricesFromBuyPrice(
          177, charisma.Charisma(11).CharismaFactor(), 1.33), set([100]))
  
def TestIdentifyScrollByElimination(scroll_store):
  scroll_store.Identify('charging', 'ZELGO MER')
  scroll_store.Identify('genocide', 'ELBIB YLOH')
  scroll_store.Identify('punishment', 'VE FORBRYDERNE')
  scroll_store.See('NR 9')
  scroll_store.AddPriceInformation('NR 9', set([300]))
  stinking_scroll = scroll_store.FindCanonical('stinking cloud')
  ExpectEqual(stinking_scroll.unidentified_description, 'NR 9')


def TestCascadingIdentifyScrollByElimination(scroll_store):
  # 1/2 scrolls at 60 is known (blank paper is free)

  # 1/2 scrolls at 80 is known
  scroll_store.Identify('enchant armor', 'DUAM XNAHT')

  # one scroll is either 60 or 80
  scroll_store.AddPriceInformation('READ ME', set([60, 80]))

  # nothing should happen here
  enchant_weapon_scroll = scroll_store.FindCanonical('enchant weapon')
  remove_curse_scroll = scroll_store.FindCanonical('remove curse')
  ExpectEqual(enchant_weapon_scroll.IsIdentified(), False)
  ExpectEqual(remove_curse_scroll.IsIdentified(), False)

  # now we find a scroll at 80
  scroll_store.AddPriceInformation('THARR', set([80]))

  # we should have seen READ ME get matched to enchant weapon and
  # THARR get matched to remove curse - let's verify
  ExpectEqual(enchant_weapon_scroll.IsIdentified(), True)
  ExpectEqual(remove_curse_scroll.IsIdentified(), True)
  ExpectEqual(enchant_weapon_scroll.unidentified_description, 'READ ME')
  ExpectEqual(remove_curse_scroll.unidentified_description, 'THARR')


def main():
  scroll_store = scroll.ScrollStore()
  menu_looper = menu.MenuLooper()
  sell_scroll_menu_item = scroll.SellScrollMenuItem(menu_looper, scroll_store)
  buy_scroll_menu_item = scroll.BuyScrollMenuItem(menu_looper, scroll_store)

  TestScrollStore(scroll_store)
  TestGetListPricesFromSalePrice(sell_scroll_menu_item)
  TestGetListPricesFromBuyPrice(buy_scroll_menu_item)
  TestGetListPricesFromBuyPriceWithSuckerFactor(buy_scroll_menu_item)
  TestIdentifyScrollByElimination(scroll_store)

  scroll_store_2 = scroll.ScrollStore()
  TestCascadingIdentifyScrollByElimination(scroll_store_2)

if __name__ == '__main__':
  main()
