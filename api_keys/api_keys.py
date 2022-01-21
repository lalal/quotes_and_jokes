from decouple import config


dad_jokes_url = "https://dad-jokes.p.rapidapi.com/random/joke"

dad_jokes_headers = {
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': config("RAPID_API_KEY")
    }


motivation_quotes_url = "https://motivational-quotes1.p.rapidapi.com/motivation"

motivational_quotes_headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
    'x-rapidapi-key': config("RAPID_API_KEY")
    }

famous_quotes_url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
famous_quotes_headers = {
    'x-rapidapi-host': "andruxnet-random-famous-quotes.p.rapidapi.com",
    'x-rapidapi-key': config("RAPID_API_KEY")
    }

game_of_thrones_quotes_url = "https://got-quotes.herokuapp.com/quotes"

philosophy_quotes_url = "http://philosophy-quotes-api.glitch.me/quotes"

quotel_url = "https://quotel-quotes.p.rapidapi.com/quotes/random"

quotel_headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "quotel-quotes.p.rapidapi.com",
    'x-rapidapi-key': config("RAPID_API_KEY")
    }

game_of_thrones2_quotes_url = "https://game-of-thrones-quotes.p.rapidapi.com/api/quote/random"

game_of_thrones2_headers = {
    'x-rapidapi-host': "game-of-thrones-quotes.p.rapidapi.com",
    'x-rapidapi-key': config("RAPID_API_KEY")
    }

quotes_api_ninja_url = "https://quotes-by-api-ninjas.p.rapidapi.com/v1/quotes"

quotes_api_ninja_headers = {
    'x-rapidapi-host': "quotes-by-api-ninjas.p.rapidapi.com",
    'x-rapidapi-key': config("RAPID_API_KEY")
    }

