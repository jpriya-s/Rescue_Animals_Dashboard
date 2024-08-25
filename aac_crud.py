from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCrud:
  
    def __init__(self, user, passwd, host, port, db, col):
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = db
        COL = col

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
   
    def create(self, data):
      ''' Method to insert animal record '''
      try:
        results = self.collection.insert_one(data)
        return True if results.inserted_id else False
      except Exception as e:
        print(f"Error in inserting document: {e}")
        return False
        
    def read(self, query):
      ''' Method to read animal record '''
      try:
        cursor = self.collection.find(query)
        return list(cursor)
      except Exception as e:
        print(f"Error quering documents: {e}")
        return []
        
    def update(self, query, new_data):
      ''' Method to update animal records '''  
      try:
        result = self.collection.update_many(query, {'$set': new_data})
        return result.modified_count
      except Exception as e:
        print(f"An error occured in update operation: {e}")
        return 0
        
    def delete(self, query):
      ''' Method to update animal records '''  
      try:
        result = self.collection.delete_many(query)
        return result.deleted_count
      except Exception as e:
        print(f"An error occured in delete operation: {e}")
        return 0
