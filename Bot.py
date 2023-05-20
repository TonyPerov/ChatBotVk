import vk_api
from vk_api.longpoll import VkLongPoll, VkEnventType

"...cылочка..."

class Vk_Bot:
    def __init__(self, bot_name, api_token):
        self.session = vk_api.VkApi(token=api_token)
        self.longpoll = VkLongPoll(self.session)
        self.vk = self.session.get_api()
        self.bot_name = bot_name

    def send_message(self, message, id):
        self.vk.messages.send(message=message, user_id=id, random_id=datetime.datetime.now().microsecond)

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkEnventType.MESSAGE_NEW and event.to_me and event.text.split(" ")[0] == self.bot_name:
                self.send_message( event.text, event.user_id)


bot = Vk_Bot("KvantBot", "...cылочка...")
bot.start()

#GitHub
#:(