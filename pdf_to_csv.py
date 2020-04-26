import tabula

class PDF_TO_CSV:

	def __init__(self, pdf_file_name):
		self.pdf_file_name = pdf_file_name

	def converter(self, pdf_file_name):
		# convert PDF into CSV file
		tabula.convert_into("pdf_file_name", "output.csv", output_format="csv", pages='all')

		return output.csv

