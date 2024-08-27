from datetime import datetime

class Post:
    def __init__(self, text, timestamp=None):
        self.text = text 
        self.timestamp = timestamp if timestamp else datetime.now()
        self.user = None

    def set_user(self, user):
        self.user = user
    
    def __str__(self):
        user_str = f'{self.user.first_name} {self.user.last_name}' if self.user else "Unknown User"
        return f'@{user_str}: "{self.text}"\n\t{self.timestamp.strftime("%A, %b %d, %Y")}'



class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)

    def __str__(self):
        return super().__str__()


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return f'{super().__str__()}\n\t{self.image_url}'



class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f'{super().__str__()}\n\t{self.latitude}, {self.longitude}'

