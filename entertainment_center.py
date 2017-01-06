import media
import fresh_tomatoes

catch_me_if_you_can = media.Movie("Catch Me If You Can",
                                  "The true story of master trickster, check forger, and imposter Frank Abagnale, Jf.",
                                  "http://vignette1.wikia.nocookie.net/imatrix/images/a/a5/Catch-me-if-you-can-2002-poster-artwork-leonardo-dicaprio-tom-hanks-christopher-walken.jpg/revision/latest?cb=20130503095551",
                                  "https://www.youtube.com/watch?v=71rDQ7z4eFg")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                   "http://www.impawards.com/1994/posters/shawshank_redemption_ver2.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

the_intern = media.Movie("The Intern",
                         "70-year-old widower Ben Whittaker has discovered that retirement isn't all it's cracked up to be. Seizing an opportunity to get back in the game, he becomes a senior intern at an online fashion site.",
                         "https://s-media-cache-ak0.pinimg.com/564x/a2/79/ea/a279eaea8b6d8d7453da1d11e8fbbf1a.jpg",
                         "https://www.youtube.com/watch?v=ZU3Xban0Y6A")
movies = [catch_me_if_you_can, shawshank_redemption, the_intern]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
print (media.Movie.__name__)
