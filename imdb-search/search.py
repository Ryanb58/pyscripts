import imdb

ia = imdb.IMDb()
results = ia.search_movie('Starwars')

for movie in results:
    print(movie.get('long imdb canonical title'), movie.movieID)
