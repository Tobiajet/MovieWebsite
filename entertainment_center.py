import fresh_tomatoes
import mediaa

power_rangers = mediaa.Movie("Power Rangers",
                        "A story of five teenage superheros",
                        "https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png",
                        "https://www.youtube.com/watch?v=5kIe6UZHSXw")
#print(power_rangers.storyline)

the_wolf_of_wall_street = mediaa.Movie("The Wolf of Wall Street",
                                "A story of an American stock broker",
                                "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                "https://www.youtube.com/watch?v=iszwuX1AK6A")
#print(the_wolf_of_wall_street.storyline)
#the_wolf_of_wall_street.show_trailer()

movies = [power_rangers, the_wolf_of_wall_street]
#fresh_tomatoes.open_movies_page(movies)
#print(mediaa.Movie.VALID_RATINGS)
print(mediaa.Movie.__doc__)
