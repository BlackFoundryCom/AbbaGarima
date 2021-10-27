from datetime import datetime
from defcon import Font
from ufo2ft import compileOTF
import pathlib
from drawbot_skia.document import PDFDocument
from drawbot_skia.drawing import Drawing

# make the beta font
ufo = Font('sources/Garima.ufo')
otf = compileOTF(ufo, removeOverlaps=True)
prfx = str(datetime.now()).split('.')[0].replace(":", "-").replace(" ", "_")
otf.save('beta/%s_Garima.otf' % prfx)

# make a PDF proof

margins = 50
fSize = 18
fLeading = 20
pageHeight = 842
pageWidth = 595

pdfPath = pathlib.Path("proofing/%s_Garima.pdf" % prfx)
pdfDoc = PDFDocument(pdfPath)
with pdfDoc.drawing() as db:
	db.newPage(pageWidth, pageHeight)
	db.font('beta/%s_Garima.otf' % prfx)
	db.fontSize(18)

	txt = open('proofing/GarimaGospelText.txt', 'r').readlines()
	j = 0
	col = 0
	for l in txt:
		db.text(l, (margins+col, margins+j))
		j += fLeading
		if j >= pageHeight - margins:
			j = 0
			col = pageWidth*.5 - margins
		if col > 0 and j >= pageHeight - margins:
			db.newPage(pageWidth, pageHeight)
			db.font('beta/%s_Garima.otf' % prfx)
			db.fontSize(18)
			j = 0
			col = 0
	db.saveImage(pdfPath)