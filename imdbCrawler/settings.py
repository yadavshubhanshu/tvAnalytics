BOT_NAME = 'imdbCrawler'

SPIDER_MODULES = ['imdbCrawler.spiders']
NEWSPIDER_MODULE = 'imdbCrawler.spiders'

DATABASE = {
			'drivername': 'mysql+mysqldb',
            'username': 'shubhanshu',
            'password': 'password',
            'database': 'imdbDatabase'
            }

ITEM_PIPELINES = {
    'imdbCrawler.pipelines.imdbItemPipeline':300
}
