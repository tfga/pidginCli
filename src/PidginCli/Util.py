# encoding: utf-8

def containsInsensitive(text, name):
    
    text = text.lower()
    name = name.lower()
    
    return text.find(name) != -1
