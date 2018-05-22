import media
import fresh_tomatoes

katamarayudu = media.movie("Katamarayudu",
                           "Story about violence",
                           "https://bit.ly/2LmxFRs", "https://bit.ly/2mES06P")
agnyathavasi = media.movie("Agnyathavasi", "Story about prince",
                           "https://bit.ly/2s0Ia47",
                           "https://www.youtube.com/watch?v=97h9fBWltBM")
gabbarsingh = media.movie("Gabbarsingh", "Story about cop",
                          "https://bit.ly/2GCGOli",
                          "https://www.youtube.com/watch?v=FpFoQPj4sgs")
rambabu = media.movie("Rambabu", "Story about power of common man",
                      "https://bit.ly/2IEMAEX",
                      "https://www.youtube.com/watch?v=TtcEOM7Fmy0")

movies = [katamarayudu, agnyathavasi, gabbarsingh, rambabu]
fresh_tomatoes.open_movies_page(movies)

