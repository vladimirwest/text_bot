import feedparser
import command_system

def news(arg):
	message = 'Держу тебя в курсе!\n\n'
	data_parsed = feedparser.parse('https://news.yandex.ru/Nizhny_Novgorod/index.rss')
	for news in data_parsed['entries']:
		message += "📰 " + news['title'] + '\n' 
	return message, ""

news_command = command_system.Command()

news_command.keys = ['новости', 'news', 'события']
news_command.description = 'Кину свежие новости с Яндекса'
news_command.process = news