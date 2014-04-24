BOT_NAME = 'imdb_sample'

SPIDER_MODULES = ['imdb_sample.spiders']
NEWSPIDER_MODULE = 'imdb_sample.spiders'

DATABASE = {
			'drivername': 'mysql+mysqldb',
            'username': 'root',
            'password': 'password',
            'database': 'imdbDatabase'
            }

ITEM_PIPELINES = {
    'imdb_sample.pipelines.imdbItemPipeline':300
}
