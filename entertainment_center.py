import fresh_tomatoes
import media

# Create instances of movies
interstellar = media.Movie("Interstellar",
                        "In the near future, Earth has been devastated by drought and famine, causing a scarcity in food and extreme changes in climate. When humanity is facing extinction, a mysterious rip in the space-time continuum is discovered, giving mankind the opportunity to widen its lifespan. A group of explorers must travel beyond our solar system in search of a planet that can sustain life. The crew of the Endurance are required to think bigger and go further than any human in history as they embark on an interstellar voyage into the unknown. Coop, the pilot of the Endurance, must decide between seeing his children again and the future of the human race.",
                        "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar2.jpg",
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA")

fifth_element = media.Movie("The Fifth Element",
                           "Two hundred and fifty years in the future, life as we know it is threatened by the arrival of Evil. Only the Fifth Element can stop the Evil from extinguishing life, as it tries to do every five thousand years. She is assisted by a former elite commando turned cab driver, Korben Dallas, who is, in turn, helped by Prince/Arsenio clone, Ruby Rhod. Unfortunately, Evil is being assisted by Mr. Zorg, who seeks to profit from the chaos that Evil will bring, and his alien mercenaries.",
                           "http://i.kinja-img.com/gawker-media/image/upload/s--gz-ivJhU--/775126109255191106.jpg",
                           "https://www.youtube.com/watch?v=VkX7dHjL-aY")

blade_runner = media.Movie("Blade Runner",
                           "In a cyberpunk vision of the future, man has developed the technology to create replicants, human clones used to serve in the colonies outside Earth but with fixed lifespans. In Los Angeles, 2019, Deckard is a Blade Runner, a cop who specializes in terminating replicants. Originally in retirement, he is forced to re-enter the force when four replicants escape from an off-world colony to Earth.",
                           "http://www.impawards.com/1982/posters/blade_runner_xlg.jpg",
                           "https://www.youtube.com/watch?v=4lW0F1sccqk")

gattaca = media.Movie("Gattaca",
                        "In the not-too-distant future, a less-than-perfect man wants to travel to the stars. Society has categorized Vincent Freeman as less than suitable given his genetic make-up and he has become one of the underclass of humans that are only useful for menial jobs. To move ahead, he assumes the identity of Jerome Morrow, a perfect genetic specimen who is a paraplegic as a result of a car accident. With professional advice, Vincent learns to deceive DNA and urine sample testing. Just when he is finally scheduled for a space mission, his program director is killed and the police begin an investigation, jeopardizing his secret.",
                        "http://www.impawards.com/1997/posters/gattaca_ver1.jpg",
                        "https://www.youtube.com/watch?v=ZppWok6SX88")

contact = media.Movie("Contact",
                        "Contact is the story of a free thinking radio astronomer who discovers an intelligent signal broadcast from deep space. She and her fellow scientists are able to decipher the Message and discover detailed instructions for building a mysterious Machine. Will the Machine spell the end of our world, or the end of our superstitions? Will we take our place among the races of the Galaxy, or are we just an upstart species with a long way to go?",
                        "http://www.optionated.com/wp-content/uploads/2011/11/Contact-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=SRoj3jK37Vc")


serenity = media.Movie("Serenity",
                        "In the future, a spaceship called Serenity is harboring a passenger with a deadly secret. Six rebels on the run. An assassin in pursuit. When the renegade crew of Serenity agrees to hide a fugitive on their ship, they find themselves in an awesome action-packed battle between the relentless military might of a totalitarian regime who will destroy anything - or anyone - to get the girl back and the bloodthirsty creatures who roam the uncharted areas of space. But, the greatest danger of all may be on their ship.",
                        "http://www.impawards.com/2005/posters/serenity_ver2_xlg.jpg",
                        "https://www.youtube.com/watch?v=JY3u7bB7dZk")

# An array that holds all the movies
movies = [interstellar, fifth_element, blade_runner, gattaca, contact, serenity]

# Display movies and information on a web page
fresh_tomatoes.open_movies_page(movies)
