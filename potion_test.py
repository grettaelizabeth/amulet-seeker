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


def main():
  potion_store = potion.PotionStore()
  menu_looper = menu.MenuLooper()
  sell_potion_menu_item = potion.SellPotionMenuItem(menu_looper, potion_store)
  buy_potion_menu_item = potion.BuyPotionMenuItem(menu_looper, potion_store)

  TestPotionStore(potion_store)
  TestGetListPricesFromSalePrice(sell_potion_menu_item)
  TestGetListPricesFromBuyPrice(buy_potion_menu_item)

if __name__ == '__main__':
  main()
