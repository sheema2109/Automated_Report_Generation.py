import os
import pandas as pd
from fpdf import FPDF

file_path = "D:\\Elite\\data.csv"

if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found.")
    exit()

df = pd.read_csv(file_path)

print("Data Preview:")
print(df.head())

numeric_cols = df.select_dtypes(include=['number'])

stats = numeric_cols.describe()
print("\nStatistical Summary:")
print(stats)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Employee Data Report", ln=True, align='C')
pdf.ln(10)

pdf.cell(0, 10, txt="Data Preview:", ln=True, align='L')
pdf.ln(5)
for index, row in df.iterrows():
    pdf.cell(0, 10, txt=f"{row['Employee ID']} - {row['Name']} - {row['Department']} - {row['Experience (Years)']} Years - Score: {row['Performance Score']} - Cert: {row['Certifications']}", ln=True)
    
pdf.ln(5)

pdf.cell(0, 10, txt="Statistical Summary:", ln=True, align='L')
pdf.ln(5)
for col in numeric_cols.columns:
    pdf.cell(0, 10, txt=f"{col}: Mean={numeric_cols[col].mean():.2f}, Min={numeric_cols[col].min()}, Max={numeric_cols[col].max()}", ln=True)
    
pdf.ln(5)

pdf_output_path = "D:\\Elite\\report.pdf"
pdf.output(pdf_output_path)
print(f"\nReport successfully saved as '{pdf_output_path}'")
