from fpdf import FPDF

from create_table_fpdf2 import PDF




def create_pdf_file(name, last_name,email, ninvoice,date,subtotal,invoice_list, title=None):
    print(date)

    pdf = PDF('P','mm', 'Letter', 'A3')

    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()

    pdf.set_font('helvetica', '', 16)

    pdf.cell(120,10, '')


    pdf.set_font('helvetica', 'B', 25)

    pdf.cell(0,10,'Invoice',ln=1, align='L')

    pdf.set_font('helvetica', '', 10)
    pdf.cell(60,10, f'{name} {last_name}', align='L')

    pdf.cell(60,10, '', align='L')
    pdf.cell(0,10, f'N of invoice: {ninvoice}', align='L', ln=True)


    pdf.cell(60,10, f'{email}', align='L')
    pdf.cell(60,10, '', align='L')
    pdf.cell(0,10, f'Date of Invoice: {date}', align='L', ln=True)

    

    pdf.cell(120,0,'')
    pdf.cell(70,10, 'Amount owed', align='C', ln=1)
    line1_w = pdf.get_string_width('Amount owed')
    line2_w = pdf.get_string_width('')



    pdf.set_font('helvetica', 'B', 21)
    pdf.cell(120,0,'')
    pdf.cell(70,10, f'${subtotal}', align='C', ln=1)


    pdf.set_xy(143,40)
    pdf.cell(45,25,'',align='C', border=1,ln=1)


    pdf.set_font('helvetica', '', 16)

    doc_w = pdf.w
    print(line1_w, doc_w)

    


    data = [
        ["**Description**", "Quantity", "Price", "Total"],
        ["Debtchat form mobile ", "1", "10", "10"]
    ]

    print(invoice_list)
    print(data)

    invoice_title = title if title != None else ''
    print(invoice_title)

    if(title ==None):
        pdf.cell(150,10,'',ln=1)
        print('aqui')

    pdf.create_table(table_data = invoice_list,title=f'{invoice_title}', cell_width=[135,20,20,20,],emphasize_data=["**Description**", "Quantity", "Price", "Total"],  emphasize_style='BIU')

    pdf.cell(125,10,'')

    pdf.cell(40,8,'Sub Total', align='L', border=1)
    pdf.cell(30,8,f'${subtotal}', align='L', border=1,ln=1)


    pdf.cell(125,10,'')

    pdf.cell(40,8,'Total', align='L', border=1)
    pdf.cell(30,8,f'${subtotal}', align='L', border=1)

    pdf.output('pdf2.pdf')