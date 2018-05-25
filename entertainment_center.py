import media
import fresh_tomatoes

katamarayudu = media.movie("Katamarayudu",
                           "Story about violence",
                           "https://bit.ly/2LmxFRs", "https://bit.ly/2mES06P")
agnyathavasi = media.movie("Agnyathavasi", "Story about prince",
                           "https://bit.ly/2s0Ia47", "https://bit.ly/2D6FEOI")
gabbarsingh = media.movie("Gabbarsingh", "Story about cop",
                          "https://bit.ly/2GCGOli", "https://bit.ly/2GPtWIv")
rambabu = media.movie("Rambabu", "Story about power of common man",
                      "https://bit.ly/2IEMAEX", "https://bit.ly/2xbzoGi")

movies = [katamarayudu, agnyathavasi, gabbarsingh, rambabu]
# used to open movie trailers web page
fresh_tomatoes.open_movies_page(movies)
