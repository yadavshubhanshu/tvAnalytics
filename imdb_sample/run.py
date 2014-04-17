import os,subprocess
subprocess.check_call(['scrapy', 'crawl', 'imdb', '-a', 'category="30 rock"', '-o', 'items.json', '-t', 'json'])