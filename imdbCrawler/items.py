from scrapy.item import Item, Field

 
def serializeToInt(value):
   value = value.partition(',')
   return int(value[0]+value[2])

def serializeToFloat(value):
    return float(value)

class imdbItem(Item):
    showName = Field()
    link = Field()
    seriesRating = Field(serializer=serializeToFloat)
    episode = Field()
    episodeRating = Field(serializer=serializeToFloat)
    votes = Field()
    genre = Field()
    director = Field()
    airDate = Field()
    videoLink = Field()

