from datetime import datetime
from defcon import Font
from ufo2ft import compileOTF
from drawbot_skia.drawbot import *
from drawbot_skia.document import PDFDocument

prfx = str(datetime.now()).split('.')[0].replace(":", "-").replace(" ", "_")

# make the beta font
ufo = Font('sources/Garima.ufo')
otf = compileOTF(ufo, removeOverlaps=True)
otf.save('beta/%s_Garima.otf' % prfx)

# make a PDF proof
margins = 50
fSize = 18
fLeading = 20
pageHeight = 842
pageWidth = 595

pdfPath = 'proofing/%s_Garima.pdf' % prfx
doc = PDFDocument(pdfPath)

with doc.drawing() as db:
	db.newPage(pageWidth, pageHeight)
	db.font('beta/%s_Garima.otf' % prfx)
	db.fontSize(18)

	txt = open('proofing/GarimaGospelText.txt', 'r').readlines()
	j = 0
	col = 0
	for l in txt:
		l = l.strip()
		db.text(l, (margins+col, pageHeight-(margins+j)))
		j += fLeading
		if col > 0 and j >= pageHeight - 2*margins:
			db.newPage(pageWidth, pageHeight)
			db.font('beta/%s_Garima.otf' % prfx)
			db.fontSize(18)
			j = 0
			col = 0
		elif j >= pageHeight - 2*margins:
			j = 0
			col = pageWidth*.5 - margins