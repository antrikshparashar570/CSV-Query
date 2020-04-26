import tabula

class PDF_TO_CSV:
	def converter(self, pdf_file_name):
		# convert PDF into CSV file
		tabula.convert_into("pdf_file_name", "output.csv", output_format="csv", pages='all')

		return "output.csv"

