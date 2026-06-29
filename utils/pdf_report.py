from fpdf import FPDF

class Report(FPDF):

    def header(self):
        self.set_font("Helvetica","B",18)
        self.cell(0,10,"StayWise Executive Report",ln=True,align="C")

    def chapter(self,title):
        self.set_font("Helvetica","B",14)
        self.cell(0,8,title,ln=True)

    def body(self,text):
        self.set_font("Helvetica","",11)
        self.multi_cell(0,6,text)