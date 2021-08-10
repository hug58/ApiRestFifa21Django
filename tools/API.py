
import requests
import os.path
import logging

import concurrent.futures
import time


'''
	112.1304759979248 seconds thread
'''

class HandleAPI:


	def __init__(self, base_url:str, page:int=1, total_pages:int=1, workers:int=20):

		logging.basicConfig(
			level=logging.DEBUG,
		)

		self.base_url:str = base_url 
		self.total_pages:int = total_pages
		self.page = page

		self.headers:Dict[str]= { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
		self.status_code:int = 0
		self.workers = workers
		self.start_time = None	
	

	def get(self,url,timeout=0):

		logging.info("GET JSON PLAYER")
		time.sleep(0.01)
		response = requests.get(url=url)

		if response.status_code == 200:
			page = response.json()['items']
			data = []

			for player in page:
				data.append({
					'name': player['name'],
					'country': player['nation']['name'],
					'position': player['position'],
					'position_full':player['positionFull'],
					'id_fifa':player['id'], 
					'team': player['club']['name'],
				})

			return data		


		elif response.status_code == 404:
			pass


		return None 


	def get_all_pages(self):
		url = os.path.join(self.base_url)
		self.start_time = time.time()
		data = []

		with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
			futures = []
			
			for number in range(self.page, self.total_pages):
				url = f'{self.base_url}?page={number}'
				futures.append(executor.submit(self.get, url=url))

			for future in concurrent.futures.as_completed(futures):
				data.append(future.result())



		print('Threaded time ', time.time() - self.start_time)
		return data		



