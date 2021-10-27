from datetime import datetime
from defcon import Font
from ufo2ft import compileOTF
import drawBot

# make the beta font
ufo = Font('sources/Garima.ufo')
otf = compileOTF(ufo, removeOverlaps=True)
prfx = str(datetime.now()).split('.')[0].replace(":", "-").replace(" ", "_")
otf.save('beta/%s_Garima.otf' % prfx)

# make a PDF proof
drawBot.newDrawing()


drawBot.newPage('A4')
drawBot.font('beta/%s_Garima.otf' % prfx)
drawBot.fontSize(18)
margins = 50
txt = open('proofing/GarimaGospelText.txt', 'r').read()
txt = drawBot.textBox(txt, (margins, margins, drawBot.width()*.5-margins*2, drawBot.height()-margins*2))
if txt:
	txt = drawBot.textBox(txt, (drawBot.width()*.5, margins, drawBot.width()*.5-margins*3, drawBot.height()-margins*2))
while txt:
	drawBot.newPage('A4')
	drawBot.font('beta/%s_Garima.otf' % prfx)
	drawBot.fontSize(18)
	txt = drawBot.textBox(txt, (margins, margins, drawBot.width()*.5-margins*2, drawBot.height()-margins*2))
	if txt:
		txt = drawBot.textBox(txt, (drawBot.width()*.5, margins, drawBot.width()*.5-margins*3, drawBot.height()-margins*2))

drawBot.saveImage("proofing/%s_Garima.pdf" % prfx)

drawBot.endDrawing()