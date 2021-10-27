from datetime import datetime
from defcon import Font
from ufo2ft import compileOTF

ufo = Font('sources/Garima.ufo')
otf = compileOTF(ufo, removeOverlaps=True)
prfx = str(datetime.now()).split('.')[0].replace(":", "-").replace(" ", "_")
otf.save('beta/%s_Garima.otf' % prfx)