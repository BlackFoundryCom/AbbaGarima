from datetime import datetime
from defcon import Font
from ufo2ft import compileOTF
from drawbot_skia.document import PDFDocument
from drawbot_skia.drawing import Drawing

# make the beta font
ufo = Font('sources/Garima.ufo')
otf = compileOTF(ufo, removeOverlaps=True)
prfx = str(datetime.now()).split('.')[0].replace(":", "-").replace(" ", "_")
otf.save('beta/%s_Garima.otf' % prfx)

# make a PDF proof

margins = 50

pdfDoc = PDFDocument("proofing/%s_Garima.pdf" % prfx)
with pdfDoc.drawing() as db:
	db.newPage(595, 842)
	db.font('beta/%s_Garima.otf' % prfx)
	db.fontSize(18)

	txt = open('proofing/GarimaGospelText.txt', 'r').read()
	txt = db.textBox(txt, (margins, margins, db.width()*.5-margins*2, db.height()-margins*2))
	if txt:
		txt = db.textBox(txt, (db.width()*.5, margins, db.width()*.5-margins*3, db.height()-margins*2))
	while txt:
		db.newPage('A4')
		db.font('beta/%s_Garima.otf' % prfx)
		db.fontSize(18)
		txt = db.textBox(txt, (margins, margins, db.width()*.5-margins*2, db.height()-margins*2))
		if txt:
			txt = db.textBox(txt, (db.width()*.5, margins, db.width()*.5-margins*3, db.height()-margins*2))

