import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story about toys!",
                        "https://vignette.wikia.nocookie.net/pixar/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20160329080002", # noqa
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A story about blue aliens in another world",
                     "https://i.pinimg.com/originals/c3/2e/40/c32e40b633ff92a2d3048f5ce8570c90.jpg", # noqa
                     "https://youtu.be/5PSNL1qE6VY")


the_heat = media.Movie("The Heat", "Two FBI agnets go on an adventure",
                       "https://s-i.huffpost.com/gen/1180820/thumbs/o-THE-HEAT-570.jpg?1", # noqa
                       "https://youtu.be/1O3iRdiplB0")


inside_out = media.Movie("Inside Out", "A movie about happiness and sadness",
                         "http://www.impawards.com/2015/posters/med_inside_out.jpg",# noqa
                         "https://youtu.be/seMwpP0yeu4")

boss_baby = media.Movie("Boss Baby", "A movie about a baby that is the CEO of \
                        the company",
                        "http://www.impawards.com/2017/posters/boss_baby.jpg",
                        "https://youtu.be/O2Bsw3lrhvs")

coco = media.Movie("Coco", "A movie about a mexican child who lives ina  world \
                   where he cannot play music",
                   "http://www.impawards.com/2017/posters/coco_ver2.jpg",
                   "https://youtu.be/Ga6RYejo6Hk")

movies = [toy_story, avatar, the_heat, inside_out, boss_baby, coco]
fresh_tomatoes.open_movies_page(movies)
