from dao.director import DirectorDAO
from dao.movie import MovieDAO
from dao.genre import GenreDAO

from service.genre import GenreService
from service.movie import MovieService
from service.director import DirectorService

from setup_db import db

director_dao = DirectorDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)
# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)