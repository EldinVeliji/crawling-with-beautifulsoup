from tkinter import *
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
import matplotlib.pyplot as plt


root = Tk()
root.geometry("600x500")


def crawlData():
    url = 'http://www.imdb.com/search/title?release_date=2020&sort=num_votes,desc&page=1'
    response = get(url)
    print(response.text[:500])

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    movie_containers = html_soup.find_all(
        'div', class_='lister-item mode-advanced')
    print(type(movie_containers))
    print(len(movie_containers))
    pages = [str(i) for i in range(1, 5)]
    years_url = [str(i) for i in range(2010, 2021)]
    names = []
    years = []
    imdb_ratings = []
    metascores = []
    votes = []

    # Per cdo vit ne interval 2010-2020
    for year_url in years_url:

        # Per cdo faqe ne interval 1-4
        for page in pages:

            # Beje nje get requesr
            headers = {"Accept-Language": "en-US, en;q=0.5"}
            response = get('http://www.imdb.com/search/title?release_date=' + year_url +
                           '&sort=num_votes,desc&page=' + page, headers=headers)

            # Ndale loop-in
            sleep(randint(8, 15))
            # Parse the content of the request with BeautifulSoup
            page_html = BeautifulSoup(response.text, 'html.parser')

            # Selekto te gjitha 50 movie kontenjerat prej nje faqe te vetme
            mv_containers = page_html.find_all(
                'div', class_='lister-item mode-advanced')

            # For every movie of these 50
            for container in mv_containers:
                # If the movie has a Metascore, then:
                if container.find('div', class_='ratings-metascore') is not None:

                    # Scrape the name
                    name = container.h3.a.text
                    names.append(name)

                    # Scrape the year
                    year = container.h3.find(
                        'span', class_='lister-item-year').text
                    years.append(year)

                    # Scrape the IMDB rating
                    imdb = float(container.strong.text)
                    imdb_ratings.append(imdb)

                    # Scrape the Metascore
                    m_score = container.find('span', class_='metascore').text
                    metascores.append(int(m_score))

                    # Scrape the number of votes
                    vote = container.find('span', attrs={'name': 'nv'})[
                        'data-value']
                    votes.append(int(vote))
    movie_ratings = pd.DataFrame({'movie': names,
                                  'year': years,
                                  'imdb': imdb_ratings,
                                  'metascore': metascores,
                                  'votes': votes
                                  })
    print(movie_ratings.info())
    movie_ratings.head(10)
    movie_ratings = movie_ratings[[
        'movie', 'year', 'imdb', 'metascore', 'votes']]
    movie_ratings.head()
    movie_ratings['year'].unique()
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
    movie_ratings['year'].head(3)
    movie_ratings.describe().loc[['min', 'max'], ['imdb', 'metascore']]
    movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
    movie_ratings.head(3)
    movie_ratings.to_csv('new_movie_ratings.csv')

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 4))
    ax1, ax2, ax3 = fig.axes
    ax1.hist(movie_ratings['imdb'], bins=10, range=(0, 10))  # bin range = 1
    ax1.set_title('IMDB rating')
    ax2.hist(movie_ratings['metascore'], bins=10,
             range=(0, 100))  # bin range = 10
    ax2.set_title('Metascore')
    ax3.hist(movie_ratings['n_imdb'], bins=10, range=(0, 100), histtype='step')
    ax3.hist(movie_ratings['metascore'], bins=10,
             range=(0, 100), histtype='step')
    ax3.legend(loc='upper left')
    ax3.set_title('The Two Normalized Distributions')
    for ax in fig.axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.show()


dummyLabel1 = Label(root, text="         ")
introText = Label(
    root, text="Welcome to the program for crawling data from the IMDB page", font="Roboto 14 bold", fg="blue")
dummyLabel2 = Label(root, text="        ")
textLabel = Label(
    root, text="All you have to do is press the button and the data will be generated into an excel spreadsheet", font="Roboto 9")
dummyLabel3 = Label(root, text="     ")
button = Button(root, text="Click here to crawl for data",
                font="Roboto", command=crawlData)

dummyLabel1.pack()
introText.pack()
dummyLabel2.pack()
textLabel.pack()
dummyLabel3.pack()
button.pack()

root.mainloop()
