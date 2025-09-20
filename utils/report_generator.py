import os
from fpdf import FPDF
from io import BytesIO

def generate_pdf_report_bytes(scenarios):
    pdf = FPDF()
    pdf.add_page()
    
    font_path = os.path.join("fonts", "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)
    
    pdf.cell(0, 10, "CFO Helper Full Report", ln=True, align="C")
    pdf.ln(5)
    
    for i, sc in enumerate(scenarios, start=1):
        pdf.multi_cell(0, 8,
                       f"Scenario {i}:\nRevenue: ₹{sc['Revenue']:,.0f}\n"
                       f"Expenses: ₹{sc['Expenses']:,.0f}\nProfit: ₹{sc['Profit']:,.0f}\n"
                       f"Marketing Spend: ₹{sc['Marketing']}\nHiring Cost: ₹{sc['Hiring']}\n"
                       f"Price Increase: {sc['Price Increase (%)']}%\nRunway: {sc['Runway']:.1f} months\n"
                       "-----------------------\n")
    # Export PDF to bytes
    pdf_bytes = BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)
    return pdf_bytes
