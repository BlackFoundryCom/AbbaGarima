from defcon import Font
from ufo2ft import compileOTF


ufo = Font('../sources/Garima.ufo')
otf = compileOTF(ufo, removeOverlaps=True)
otf.save('../beta/Garima.otf')