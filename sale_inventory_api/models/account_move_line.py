# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import requests
import urllib.request, json


class AccountMoveLine(models.Model):
	_inherit = "account.move.line"

	def prepare_and_send_invoice_data(self):
		# sale_data = {'storeId': 20929,
		#              'productNo': product.barcode,
		#              'lineQuantity': sale_order_line.product_uom_qty,
		#              'salesDate': str(self.date_order),
		#              'salesReference': self.name,
		#              'lineNo': self.order_line.id,
		#              'productDescription': product.name,
		#              'serialNumber': 'not required',
		#              'storeName': self.company.name,
		#              }
		# sale_data_list = []
		# for rec in self:
		#     sale_data_list.append()

		# temp_dict = { 'storeId': 20929,
		#         'productNo': rec.product_id.id,
		#         'lineQuantity': float(rec.quantity),
		#         'salesDate': str(self.move_id.date),
		#         # 'salesReference': self.name,
		#         'lineNo': self.move_id.id,
		#         'productDescription': rec.product_id.name,
		#         'storeName': self.company_id.name,}

		self.get_response({'storeId': 20929,
		                   'productNo': 1,
		                   'lineQuantity': 20,
		                   'salesDate': '2012-05-29T19:30:03.283Z',
		                   'salesReference': 'Sale Reference',
		                   'lineNo': 7,
		                   'productDescription': 'My Product',
		                   'storeName': 'abc', })

	def get_response(self, data):
		url = "https://api.bang-olufsen.dk/posdata/v1-test/api/Sale"

		hdr = {
			# Request headers
			'Content-Type': 'application/json-patch+json',
			'Cache-Control': 'no-cache',
			'Ocp-Apim-Subscription-Key': 'd83f37a2e6da4fe5a078b2388d8c5972',
		}
		# Request body
		data = json.dumps(data)
		response = requests.post(url, headers=hdr, json=data)
		print(">>>>>>response.json()", response)
		# import pdb;
		# pdb.set_trace()
		return response

	def post_invoice_data(self):
		self.env['account.move.line'].search([], limit=1).prepare_and_send_invoice_data()
