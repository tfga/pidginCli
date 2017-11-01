# encoding: utf-8


### -- Copiado de PyVte.vteExample

def getSelectedXs(listBox, extractor):
    
    selection = listBox.get_selection()
    
    model, selectedPaths = selection.get_selected_rows()
    if selectedPaths == None:
        return None
    else:
        return map(lambda path: extractor(model[path]), selectedPaths)
    

def getSelectedItems(widget):
    
    return getSelectedXs(widget, getRowItem)

def getSelectedItem(widget):
    
    items = getSelectedItems(widget)
    
    return items[0] if items else None
    
def getSelectedItemsText():
    return getSelectedXs(getRowText)
        
def getSelectedRows(widget):
    
    return getSelectedXs(widget, lambda row: row)
        
def getRowItem(row):
    return row[1]

def getRowText(row):
    return row[0]

