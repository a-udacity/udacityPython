import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story_line, movie_poster, movie_trailer):
        self.title = movie_title
        self.story_line = movie_story_line
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_poster

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)

