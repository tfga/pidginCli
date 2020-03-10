# encoding: utf-8

import gtk
from PidginCli.buddies import getBuddy, getAllBuddies, getBuddyLogin,\
    getFullName
from PidginCli.Util import containsInsensitive
from PidginCli.send import send
import keybinder
import itertools
from PidginQuickLaunch.TreeViewUtil import getSelectedItem



class Buddy:
    
    def __init__(self, login, fullName):
        
        self.login    = login
        self.fullName = fullName
        
    def __str__(self):
        
        return '{} ({})'.format(self.login, self.fullName)
        
        

def getBuddyList():
    
    buddies = getAllBuddies()
    
    return [Buddy(getBuddyLogin(b), getFullName(b))           
            for b in buddies]


# i = 0

def matches(entrystr, buddy):
    
#     ## DEBUG
# 
#     global i
#     i += 1 
#     print i, 'matches()'
# 
#     ## DEBUG

    return containsInsensitive(buddy.login    , entrystr) \
        or containsInsensitive(buddy.fullName , entrystr)



def getFirstCandidate():
    
    return candidateBuddies[0] if candidateBuddies else None


def getSelectedBuddy():
    
    return getSelectedItem(listBox)


def chat():

    selectedBuddy = getSelectedBuddy() or getFirstCandidate()

#     # DEBUG
#     print 'getSelectedBuddy =', selectedBuddy
#     return
#     # DEBUG
        
    if selectedBuddy:
    
        chatWith(selectedBuddy.login)
        hideWindow()


def chatWith(buddyLogin):
    
    send('', buddyLogin)


def matchingBuddies(text):
    
    gen = (b for b in buddies if matches(text, b))  # @UndefinedVariable   # Maluquice do PyDev...
    
    return list(itertools.islice(gen, 10))

    # Deveria ter funcionado...
    # _.chain() não é lazy, cacete?!?!
#     return _.chain(buddies)                      \
#             .filter(lambda b: matches(text, b))  \
#             .take(10)                            \
#             .value()



def selectFirstOption(widget): # text, completion):
    
    mb = matchingBuddies(widget.get_text())
    
    if mb:
        
#         completion.emmit("match-selected") # Outra idéia...
        
        buddy = mb[0]
        
        setSelectedBuddy(buddy)
        
        widget.set_text(str(buddy))





RETURN = gtk.gdk.keyval_from_name('Return')  # @UndefinedVariable
TAB    = gtk.gdk.keyval_from_name('Tab')     # @UndefinedVariable
ESC    = gtk.gdk.keyval_from_name('Escape')  # @UndefinedVariable


def onKeyPress(widget, event):
    
    print event, event.keyval, event.state # & gtk.gdk.CONTROL_MASK:
    
    key = event.keyval
    
    if key == RETURN:
        
        chat()
        
    elif key == TAB:
        
        selectFirstOption(widget)
        
    elif key == ESC:
        
        hideWindow()
        

def setSelectedBuddy(buddy):
    
    global selectedBuddy
    
    selectedBuddy = buddy
    
    
def onMatchSelected(completion, model, iter):
    
    setSelectedBuddy(model[iter][1]) 
    
    
###################################################################################################################
# Globals

buddies = getBuddyList()
candidateBuddies = []
selectedBuddy = None
window = None
listBox = None

###################################################################################################################

def newEntry():

    def onChange(widget):
        
        print widget, 'changed!!!'

#        global i    # DEBUG
#        i = 0

        text = widget.get_text()
        
#         if len(text) < 3:
#             
#             return
        
        global candidateBuddies
        candidateBuddies = matchingBuddies(text) if text else []
        
        listBox.set_model(newListStore(candidateBuddies))
        

    entry = gtk.Entry()
    entry.set_width_chars(50)
    
    entry.connect('changed', onChange)
    entry.connect('key-press-event', onKeyPress)
    
    
    return entry

    


def globalShortcut(window):
    
    def on_show_keyboard_shortcut():
    
#         print 'Global shortcut, baby!!!'
        
        window.show_all()
        
    
#     mergeKey = '<Super>p'  # TODO
    mergeKey = "<Ctrl><Alt>m"
    print 'Binding shortcut %s to PidginQuickLaunch' % mergeKey
    keybinder.bind(mergeKey, on_show_keyboard_shortcut)
    

def hideWindow():
    
    window.hide()
    
def onDelete(w, event):
    
    hideWindow()
    return True


def newListStore(buddies):
    
    liststore = gtk.ListStore(str, object)
    
    for buddy in buddies:
        
        liststore.append([str(buddy), buddy])
        
    return liststore

    
def newListBox():
    
    global listBox

    listBox = gtk.TreeView()
    
    # Configures the listBox
    # Create a renderer and set the 'text' property
    renderer = gtk.CellRendererText()
    
#         def setWrapWidth(w):
#             renderer.props.wrap_width = w
        
#         renderer.props.wrap_mode = pango.WRAP_WORD
    
#         font = pango.FontDescription('Monospace 10')
#         renderer.set_property('font-desc', font)

    # No header
    listBox.set_headers_visible(False)

    # Add column using our renderer
    col = gtk.TreeViewColumn(None, renderer, text = 0)
    
    # É óbvio que eu não quero que o tamanho máximo seja esse.
    # Mas se eu não colocar limite nenhum, em alguns casos a coluna fica maior do que a tela
    # e aí quando eu mando maximizar, ele fica doidão.
#         col.set_max_width(400)
    
    listBox.append_column(col)
    
    listBox.connect('select-cursor-row', lambda treeview, start_editing: chat()) # ENTER na listBox
    
    return listBox



# TODO mover para GtkUtils (Já existe um em PyVte. Mover para PyUtil?)
# def newVBox(*widgets):
#     
#     vpane = gtk.VBox()
#     
#     for w in widgets:
#         
#         vpane.add(w)
#     
#     return vpane

def newVBox(entry, listBox):
    
    vpane = gtk.VBox()
    
#     vpane.set_spacing(0)
    
    vpane.pack_start(entry   , expand=False)
    vpane.pack_end  (listBox)
    
    return vpane


# Copiado de GtkUtil (PyVte)
def wrapInScrolledWindow(component):
    scrollTree = gtk.ScrolledWindow()
    scrollTree.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
    scrollTree.add(component)
    
    return scrollTree


def newWindow():
    
    global listBox
    
    # boilerplate
    window = gtk.Window()
    window.add(newVBox(newEntry()
                      ,listBox = newListBox()
                      ))
    
    # On close, don't destroy: hide
    window.connect('delete-event', onDelete)
    
    globalShortcut(window)
    
    return window


def main():
    
    global window
    
    window = newWindow()

    gtk.main()
    




def entryPoint():
    main()

if __name__ == '__main__':
    entryPoint()
