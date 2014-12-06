import os,subprocess
subprocess.check_call(['scrapy', 'crawl', 'imdb', '-a', 'category="breaking bad"', '-o', 'items.json', '-t', 'json'])