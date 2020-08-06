#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:41:10 2020

@author: wufei
"""

#ex7.py - learn python the hard way
periods = 100

print("Mary had a little lamb.") #print line to console
print("Its fleece was white as {}.".format("SNOW")) #Print line to console, but there's a space for {} which takes the results from somewhere else.
print("And everwhere that Mary went.")
print("." * periods) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what h prints
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
