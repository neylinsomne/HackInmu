import pymongo 

class Connect_To_Mongo():
    def __init__(self , URI):
        self.URI = URI

    def connection(self):
        try:
            client = pymongo.MongoClient(self.URI)
            db = client['bogota']
            print('||| Connect to Mongo')
            return db
        except :
          print('An exception occurred')


mongo = Connect_To_Mongo('mongodb+srv://tharasoftorigen:kGn4ofLJXohlIxz8@cluster0.uzirn.mongodb.net/')

mongo_connect = mongo.connection()

