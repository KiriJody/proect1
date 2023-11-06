
from sendResurses import SendResurses
from dataBaseManager import DataBaseManager
import helper
 

class SimpleGetHandler(SendResurses):
   

    def homePage(self, param):
        result = ''
        
        if param is None:
            result = DataBaseManager.get_data("SELECT * FROM people")
        else:
            result = DataBaseManager.get_data("SELECT * FROM people WHERE name=?", (param,))

        card_tempalte = helper.read_tampleate("template/card.thtml")

        data_page = ""
        for person in result:
            data_page += helper.setParamTemp(card_tempalte, id = person[0], name = person[1], age = person[2])

        content = helper.read_tampleate("template/index.html")
        content = helper.setParamTemp(content, cards = data_page)
        
        self.renderPage(content)


    def remove(self, param):
        DataBaseManager.remove("DELETE FROM people WHERE id = ?", (param,))
        print("Объект с ID={param} удален!".format(param = param))


    def do_GET(self):
        path, param = helper.split_Path_And_Param(self.path)


        if path == "/index.html" or path == "/":                    
            self.homePage(param)
        elif path == "/remove":
            self.remove(param)
        else:            
            self.getContent(self.path)


