# Scrapy settings for imdb_sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imdb_sample'

SPIDER_MODULES = ['imdb_sample.spiders']
NEWSPIDER_MODULE = 'imdb_sample.spiders'

DATABASE = {
			'drivername': 'mysql+mysqldb',
            'username': 'root',
            'password': 'shristika',
            'database': 'imdbDatabase'
            }

ITEM_PIPELINES = {
    'imdb_sample.pipelines.imdbItemPipeline':300
}
