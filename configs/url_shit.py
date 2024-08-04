import telegram


def my_bot():
    return telegram.Bot(token='7041980499:AAEkk0mrGjKaYDKy8El_95aAdY3pLqr4aTM')


def my_bot_token():
    return '7041980499:AAEkk0mrGjKaYDKy8El_95aAdY3pLqr4aTM'


def scrap_master():
    return 'https://www.1377x.to/'


def movies_api():
    url = "https://api.themoviedb.org/3/movie/now_playing" #api reference https://www.themoviedb.org
    api_key = "api_key=your api key"
    language = "en-US"
    limit_page = "1"
    movies_api_url = f"{url}?{api_key}&language={language}&page={limit_page}"
    return movies_api_url
