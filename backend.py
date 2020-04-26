from flask import Flask, render_template, make_response
from flask_restful import Resource, Api
from flask import jsonify, request
import csv
import pdf_to_csv

class data(Resource):

	def post(self):
		Query_variable = request.form["Query_variable"]
		Query_year = request.form["Query_year"]
		csv_file_name = request.form["file_name"]
		headers = {'Content-Type': 'text/html'}
		result = self.query(Query_variable, Query_year, csv_file_name)
		return make_response(render_template('result.html', result = result, file_name = csv_file_name), 200, headers)

	def query(self, Query_variable, Query_year, csv_file_name):
		#pdf_to_csv_obj = pdf_to_csv.PDF_TO_CSV()
		#csv_file_name = pdf_to_csv_obj(pdf_file_name)

		result = None
		
		with open(csv_file_name, 'r') as csvfile:
			spamreader = csv.reader(csvfile)
			s = []
			for row in spamreader:
				s = row
				break

			index = 0
			for column in s:
				if Query_year == column:
					break
				index += 1
				
			for row in spamreader:
				if row[0] == Query_variable:
					result = row[index]

		return result
