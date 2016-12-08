import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=lo_VGCi41J4")

avatar = media.Movie("Avatar", "A story of marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

revenant = media.Movie("Revenant", "Revenge movie",
                     "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                     "https://www.youtube.com/watch?v=LoebZZ8K5N0")

three_idiots = media.Movie("3 Idiots", "Two friends are searching for their long lost companion",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                        "https://www.youtube.com/watch?v=xvszmNXdM4w")

gladiator = media.Movie("Gladiator", "A story of marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                     "https://www.youtube.com/watch?v=AxQajgTyLcM")

airplane = media.Movie("Airplane", "Revenge movie",
                     "https://upload.wikimedia.org/wikipedia/en/f/f5/Airplane%21.jpg",
                     "https://www.youtube.com/watch?v=qaXvFT_UyI8")

movies = [toy_story, avatar, revenant, three_idiots, gladiator, airplane]
fresh_tomatoes.open_movies_page(movies)