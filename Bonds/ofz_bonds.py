import requests
from bs4 import BeautifulSoup as BS

class OFZ_BONDS:
  def __init__(self, prof, year, bond_sort):
    self.profit = prof
    self.year = year
    self.bonds_list = []
    self.bond_sort = bond_sort
    
  
  
    link = "https://smart-lab.ru/q/ofz/"
    response = requests.get(link).text
    
    soup = BS(response, 'lxml')
    table = soup.find('table', class_='simple-little-table trades-table').find_all('tr')
    bonds = []
    for trs in table:
      tds = trs.find_all('td')
      tr = [td.text for td in tds]
      bonds.append(tr)
       

  
    bonds_OFZ = bonds[1: -1]
    for key in range(len(bonds_OFZ)):
      
      name = bonds_OFZ[key][2]
      if len(bonds_OFZ[key][10]) > 2:  
        cost = float(bonds_OFZ[key][10]) * 10
        
      cupon = float(bonds_OFZ[key][12])
      cupon_in_year = int(float(bonds_OFZ[key][13]))
      date = bonds_OFZ[key][4].split('-')
      closing_date = date[2] + '-' + date[1] + '-' + date[0]
      profit = round(1000 - cost, 2)
      profit_2 = round(profit / cost * 100, 2)
      cupon_profit = round(cupon * cupon_in_year / cost * 100, 2)
      cupon_profit_2 = round(cupon * cupon_in_year, 2)  
      if cost <= self.profit and int(date[0]) <=  self.year:
        bond = [name, cost, cupon, cupon_in_year, closing_date, profit, profit_2, cupon_profit, cupon_profit_2]        
        self.bonds_list.append(bond)
      self.bonds_list.sort(key=lambda x: x[self.bond_sort])
  
  def send_list(self):
    for i in self.bonds_list:
      print(f'{i[0]}, цена - {i[1]} рублей, стоимость купона {i[2]} рублей, количество выплат в год {i[3]}. Дата погашения {i[4]}. Можно заработать за год на купонах {i[8]} или {i[7]}%. На разнице цены при выкупе можно заработать {i[6]}%')
     