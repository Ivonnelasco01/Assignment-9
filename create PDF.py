#import
import json
from fpdf import FPDF
#read json
data_json = open("my_info.json")
info = json.loads(data_json.read())

# create pdf object
# format
pdf = FPDF('p', 'mm', 'A4')

# add page
pdf.add_page()
pdf.image('picture.jpg', 15, 10, 40)

#font
pdf.set_text_color(0,0,0)
pdf.set_fill_color(10,0,25)
pdf.set_font('Helvetica', size = 18)

#header
pdf.set_draw_color(0,0,102)
pdf.multi_cell(200, 11, txt = info['myInfo']['name'], align='C' )

#info
pdf.set_font('Helvetica', size = 12)
pdf.multi_cell(120, 11,txt = info['myInfo']['Age'], align='C' )
pdf.multi_cell(210, 11,txt = info['myInfo']['Address'], align='C' )
pdf.multi_cell(137, 11,txt = info['myInfo']['Birthdate'], align='C' )
pdf.multi_cell(128, 11,txt = info['myInfo']['Status'], align='C' )

pdf.set_font('Helvetica', size = 15)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(20,200,200)
pdf.set_draw_color(0,0,0)
pdf.multi_cell(190,11, "Background", align = 'L', fill =1, border = 'TB')

pdf.set_font('Helvetica', size = 12)
pdf.multi_cell(120, 11,txt = info['myExpandDeg']['degree'], align='L' )
pdf.multi_cell(120, 11,txt = info['myExpandDeg']['work'], align='L' )

pdf.set_font('Helvetica', size = 15)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(20,200,200)
pdf.set_draw_color(0,0,0)
pdf.multi_cell(190,11, "Contact Information", align = 'L', fill =1, border = 'TB')

pdf.set_font('Helvetica', size = 12)
pdf.multi_cell(120, 11,txt = info['myContacts']['celphone_no.'], align='L' )
pdf.multi_cell(120, 11,txt = info['myContacts']['email'], align='L' )
pdf.multi_cell(120, 11,txt = info['myContacts']['social_media'], align='L' )

pdf.set_font('Helvetica', size = 15)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(20,200,200)
pdf.set_draw_color(0,0,0)
pdf.multi_cell(190,11, "Skills", align = 'L', fill =1, border = 'TB')

pdf.set_font('Helvetica', size = 12)
pdf.multi_cell(120, 11,txt = info['mySkills']['skill_1'], align='L' )
pdf.multi_cell(120, 11,txt = info['mySkills']['skill_2'], align='L' )
pdf.multi_cell(120, 11,txt = info['mySkills']['skill_3'], align='L' )
pdf.multi_cell(120, 11,txt = info['mySkills']['skill_4'], align='L' )

pdf.set_font('Helvetica', size = 15)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(20,200,200)
pdf.set_draw_color(0,0,0)
pdf.multi_cell(190,11, "Educational Background", align = 'L', fill =1, border = 'TB')

pdf.set_font('Helvetica', size = 12)
pdf.multi_cell(120, 11,txt = info['mySchool']['Elementary_School'], align='L' )
pdf.multi_cell(120, 11,txt = info['mySchool']['Junior_High_School'], align='L' )
pdf.multi_cell(120, 11,txt = info['mySchool']['Senior_High_School'], align='L' )
pdf.multi_cell(120, 11,txt = info['mySchool']['College'], align='L' )


pdf.output("LASCO, IVONNE GLYNN.pdf")

