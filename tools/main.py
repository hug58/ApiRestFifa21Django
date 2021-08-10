

#from API import HandleAPI



import aiohttp
import asyncio
import time

import logging
import  argparse
#from tools import database

from database import db_player,db_team
from database import session, db

#from database import db_player,db_team

from API import HandleAPI


logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] (%(threadName)-10s) %(message)s'
)



def _save_team_fifa(club:str):
	logging.info('INIT TEST SAVE TEAM')
	
	#club = data.pop('club')
	_team = session.query(db_team).filter_by(name = club).first()
	if _team:
		return _team
		
	query = db.insert(db_team).values(name=club) 
	
	session.execute(query)
	session.commit()

	return session.query(db_team).filter_by(name = club).first()


def _save_player_fifa(data, repeat):
	logging.info('INIT TEST SAVE PLAYER')
	### Hay repetidos usuarios en la db de fifa
	if not repeat:
		_player = session.query(db_player).filter_by(name = data.get('name'))
	else:
		_player = session.query(db_player).filter_by(id_fifa = data.get('id_fifa'))


	team = _save_team_fifa(data.pop('team'))
	if _player.first():
		_player.update(data)
	else:
		query = db.insert(db_player).values(**data,team_id=team.id) 
		session.execute(query)
	session.commit()



def main(repeat:int):
	url = f'https://www.easports.com/fifa/ultimate-team/api/fut/item'
	api_fifa = HandleAPI(url,1,908)

	data = api_fifa.get_all_pages()
	for page in data:
		for player in page:
			_save_player_fifa(player,repeat)

"""
async def get_page(session, url):
	async with session.get(url) as resp:
		logging.info("GET JSON PLAYER")
		page = await resp.json()
		data = []
		for player in page['items']:
			data.append({
				'name': player['commonName'],
				'nation': player['nation']['name'],
				'position': player['position'],
				'position_full':player['positionFull'],
				'id_fifa':player['id'], 
				'club': player['club']['name'],})
		return data

async def main():
	
	start_time = time.time()
	connector = aiohttp.TCPConnector(limit=50)

	async with aiohttp.ClientSession(connector=connector) as session:

		tasks = []
		for number in range(1, 908):
			url = f'https://www.easports.com/fifa/ultimate-team/api/fut/item?page={number}'
			tasks.append(asyncio.ensure_future(get_page(session, url)))

		result = await asyncio.gather(*tasks)

		for data in result:
			print(data)

	print("--- %s seconds ---" % (time.time() - start_time))

"""



if __name__=='__main__':
	#asyncio.run(main())
	parser = argparse.ArgumentParser(
		description ='test test test!',
		usage='%(prog)s [options] --repeat 1',
		epilog='Enjoy the program! :)'
	)
	
	parser.add_argument('--repeat',  help='<Required> Set flag', required=False,type=int)
	args = parser.parse_args()
	
	#print(args.repeat)
	main(args.repeat)
	#print(main(args.list))