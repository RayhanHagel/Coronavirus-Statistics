# Covid Statistics Parser by @Hageru-Ray


from requests import get
from bs4 import BeautifulSoup as bs4


class Coronavirus:
    
    def __init__(self):
        self.url = 'https://www.worldometers.info/coronavirus/'
        self.data = ''
        
        self.date_update = ''
        self.total_cases = ''
        self.total_deaths = ''
        self.total_recovered = ''

        self.fetching = 'Fetching...'
        
        
    def get_status(self):
        check =  self.data.find("span", attrs={"class" : "style4"})
        if check:
            print("Didn't found the specified country, please try again!")
            quit()
        else:
            pass
        
                
    def get_data(self, url):
        print(self.fetching)
        
        fetch = get(url)
        self.data = bs4(fetch.content, 'html.parser')
        self.get_status()
        
        # Fetch Date Update
        if url == self.url:
            date = self.data.find("div", attrs={"style" : "font-size:13px; color:#999; margin-top:5px; text-align:center"})
        else:
            date = self.data.find("div", attrs={"style" : "font-size:13px; color:#999; text-align:center"})
        
        # Fetch Statistics
        total_statistics = self.data.findAll("div", {"class" : "maincounter-number"})
        for item in range(len(total_statistics)):
            total_statistics[item] = total_statistics[item].text
            total_statistics[item] = total_statistics[item].strip().strip("\n")
        
        # Defining into Class
        self.date_update = date.text[14:]
        self.total_cases = total_statistics[0]
        self.total_deaths = total_statistics[1]
        self.total_recovered = total_statistics[2]

        # Prints Out
        print('Date:', self.date_update)
        print('Total Cases:', self.total_cases)
        print('Deaths:', self.total_deaths)
        print('Recovered:', self.total_recovered)
        

    def get_total(self):
        self.get_data(self.url)
        
        
    def get_country(self, country=None):
        if country == None:
            self.get_data(self.url)
        else:
            country = country.replace(' ', '-')
            url = self.url + "country/" + country
            self.get_data(url)

        
covid = Coronavirus()

# Example
covid.get_country('Indonesia')
