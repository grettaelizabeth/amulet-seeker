#!/usr/bin/python
"""A menuing system for taking user input.

A menuing system for taking user input to manipulate and display the
object store, the world state, and other data associated with a
running game of nethack.
"""

__author__ = 'gretta@gmail.com (Gretta Bartels)'


class MenuItem:
  """Prints a specific menu option and handles user selection of that option.

  This is an abstract base class.  Subclass from this to create MenuItems
  that actually do things.

  Attributes:
  description: What to print in the menu.
  menu_looper: The controller for all the menus.
  """

  def __init__(self, description, menu_looper):
    """Inits MenuItem."""
    self.description = description
    self.menu_looper = menu_looper


  def Print(self):
    """Prints the menu item."""
    print self.description


  def Handle(self):
    """Handle this item being selected by the player."""
    raise Exception('MenuItem is abstract!')


class SubMenuMenuItem(MenuItem):
  """A menu item that switches to a different menu.
  """

  def __init__(self, description, menu_looper, sub_menu):
    MenuItem.__init__(self, description, menu_looper)
    self.sub_menu = sub_menu


  def Handle(self):
    self.menu_looper.SetCurrentMenu(self.sub_menu)


class QuitMenuItem(MenuItem):
  """A menu item that quits.
  """

  def __init__(self, menu_looper):
    MenuItem.__init__(self, 'Quit', menu_looper)


  def Handle(self):
    self.menu_looper.Quit()


class ReturnToTopMenuItem(MenuItem):
  """A menu item that returns to the top.
  """

  def __init__(self, menu_looper):
    MenuItem.__init__(self, 'Start Over', menu_looper)


  def Handle(self):
    print
    self.menu_looper.ReturnToTop()


# toy code starts here
class AdditionMenuItem(MenuItem):
  def __init__(self, menu_looper):
    MenuItem.__init__(self, 'Add', menu_looper)

  def Handle(self):
    first = raw_input('First number to add: ')
    second = raw_input('Second number to add: ')
    print 'Sum is: %d' % (int(first) + int(second))
    print
    self.menu_looper.ReturnToTop()

class SubtractionMenuItem(MenuItem):
  def __init__(self, menu_looper):
    MenuItem.__init__(self, 'Subtract', menu_looper)

  def Handle(self):
    first = raw_input('First number to subtract: ')
    second = raw_input('Second number to subtract: ')
    print 'Difference is: %d' % (int(first) - int(second))
    print
    self.menu_looper.ReturnToTop()
# toy code ends here


class Menu:
  """Prints a list of options and invokes handlers for those options.

  Attributes:
  menu_items: the list of options on the menu
  """

  def __init__(self):
    """Inits Menu with menu items."""
    self.menu_items = []
    self.selection_prompt = 'What would you like to do? '


  def AddMenuItem(self, item):
    """Adds an item to the menu."""
    self.menu_items.append(item)


  def SetSelectionPrompt(self, prompt):
    """Overrides the default selection prompt."""
    self.selection_prompt = prompt


  def Print(self):
    """Prints the menu."""
    number = 1
    for item in self.menu_items:
      print number, ']',
      item.Print()
      number += 1


  def Validate(self, selection):
    try:
      int_sel = int(selection)
      if int_sel > 0 and int_sel <= len(self.menu_items):
        return int_sel - 1
      else:
        return None
    except:
      return None


  def GetPlayerSelection(self):
    """Prints the menu and finds out what the player wants to do."""
    self.Print()
    selection = self.Validate(raw_input(self.selection_prompt))
    if selection == None:
      print 'That is not a valid selection.'
      print
      return False
    return self.menu_items[selection].Handle()


class GoBackMenuItem(MenuItem):
  def __init__(self):
    MenuItem.__init__(self, 'Go back', None)

  def Handle(self):
    return None


class DynamicMenu(Menu):
  def __init__(self):
    Menu.__init__(self)

  def SetMenuItems(self):
    raise Exception('Not implemented!  Subclass this!')

  def GetPlayerSelection(self):
    self.SetMenuItems()
    return Menu.GetPlayerSelection(self)


class MenuLooper:
  """Prints menus and takes selections in a loop until the player quits.

  Attributes:
  current_menu: the menu we're working from right now.
  top_menu: the top level menu to go back to after an action selection.
  """

  def __init__(self):
    """Inits MenuLooper."""
    self.top_menu = None
    self.current_menu = None
    self.should_quit = False


  def SetCurrentMenu(self, menu):
    self.current_menu = menu


  def SetTopMenu(self, menu):
    self.top_menu = menu


  def ReturnToTop(self):
    self.current_menu = self.top_menu


  def Quit(self):
    self.should_quit = True


  def Loop(self):
    while(not self.should_quit and self.current_menu):
      self.current_menu.GetPlayerSelection()


def main():
  menu_looper = MenuLooper()

  math_menu = Menu()
  math_menu.AddMenuItem(AdditionMenuItem(menu_looper))
  math_menu.AddMenuItem(SubtractionMenuItem(menu_looper))
  math_menu.AddMenuItem(ReturnToTopMenuItem(menu_looper))

  main_menu = Menu()
  main_menu.AddMenuItem(SubMenuMenuItem('Do Math', menu_looper, math_menu))
  main_menu.AddMenuItem(QuitMenuItem(menu_looper))

  menu_looper.SetTopMenu(main_menu)
  menu_looper.ReturnToTop()
  menu_looper.Loop()


if __name__ == "__main__":
  main()
