from fpdf import FPDF as pdf
from json import loads

class CV(pdf):
    """
    call upon the class CV to create you cv based off the infomation in the
    settings.json file. to know how to input info to settings.json refer
    back to the github page of this project please
    """

    def getsettings(self) -> dict:
        """
        This function gets infomation needed to build the cv from the json file
        settings.json, if the json could not be found in the same directory
        as this python file it throws an error 'file settings.json is missing'
        and it quits.
        """
        try:
            file = open("settings.json", "r")
            info = file.read()
            file.flush()
            file.close()

        except:
            print("file settings.json is missing\n")
            exit(-1)

        info = loads(info)
        return info

    def head(self):
        """
        The function head main writes the title of the cv which is meant to be
        your name at the top of the pdf file and then draws a line under the 
        title.
        """
        self.set_font("Times", "I", 32)
        self.cell(60)
        self.cell(0, 10, self.getsettings()["title"])
        self.ln()
        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)
        self.ln(5)

    def getdata(self, data : str) -> dict:
        """
        This function refines helps to refine the content of the json file
        settings.json so that the data can then be used to create the cv
        """
        info = {"header" : "", "type" : "", "data" : ""}
        data = data.split(":")
        info["header"] = data[0]
        data = data[1].split(" ")
        info["type"] = data[0]

        for item in range(1, len(data)):
            info["data"] += " " + data[item]

        info["data"] = info["data"].strip()
        return info

    def pertype(self, kind : str, info : str, item) -> tuple:
        """
        This function further refines data gotten from the getdata function
        and it uses the data to create various parts of the cv based on the
        type of information the data holds
        """
        if kind == "link":
            info = info.split(" ")
            link = info[0].replace("##", ":")
            text = info[1]

            self.set_text_color(0, 0, 0)
            width = self.get_string_width(item["header"])

            self.cell(width, 8, item["header"] + " :")
            self.cell(20)

            self.set_text_color(0, 0, 255)
            width = self.get_string_width(text)

            self.cell(width, 8, text, link = link)
            self.ln()

        elif kind == "text":
            info = info.replace("_", " ")
            self.set_text_color(0, 0, 0)
            width = self.get_string_width(item["header"])

            self.cell(width, 8, item["header"] + " :")
            self.cell(20)

            width = self.get_string_width(info)

            self.cell(width, 8, info)
            self.ln()

        elif kind == "exp":
            info = info.split(" ")
            data = []
            for x in info: data.append(x.replace("_", " "))

            info = data

            self.set_text_color(0, 0, 0)
            width = self.get_string_width(item["header"])

            self.cell(width, 8, item["header"])
            self.cell(2)

            width = self.get_string_width(info[0])
            self.cell(width, 8, info[0] + " -")
            self.cell(4)

            width = self.get_string_width(info[1])
            self.cell(width, 8, info[1])
            self.cell(2)

            width = self.get_string_width(info[2])
            self.cell(width, 8, info[2])
            self.cell(2)
            
            self.set_text_color(0, 0, 255)
            link = info[3].replace("##", ":")

            width = self.get_string_width(info[4])
            self.cell(width, 8, info[4], link = link)
            self.ln()
            self.set_text_color(0, 0, 0)

            self.set_font("Times", "I", 12)
            width = self.get_string_width(info[5])
            self.cell(width, 8, info[5])
            self.set_font("Times", "I", 15)
            self.ln()

        elif kind == "skill":
            info = info.replace("_", " ")
            self.set_text_color(0, 0, 0)
            width = self.get_string_width(item["header"])

            self.cell(width, 8, item["header"] + " :")
            self.cell(8)

            self.set_font_size(12)
            width = self.get_string_width(info)

            self.cell(width, 8, info)
            self.ln()

        elif kind == "achieve":
            info = info.split(" ")
            data = []

            for x in info: data.append(x.replace("_", " "))

            info = data
            self.set_text_color(0, 0, 0)
            width = self.get_string_width(item["header"])

            self.cell(width, 8, item["header"] + " :")
            self.ln()

            self.set_font("Times", "I", 15)
            width = self.get_string_width(info[0])

            self.cell(width, 8, info[0])
            self.cell(10)

            link = info[1].replace("##", ":")
            self.set_text_color(0, 0, 255)
            width = self.get_string_width(info[2])

            self.cell(width, 8, info[2], link = link)
            self.set_font("Times", "B", 15)
            self.set_text_color(0, 0, 0)
            self.ln()

        elif kind == "project":
            info = info.split(" ")
            data = []

            for x in info: data.append(x.replace("_", " "))

            info = data
            self.set_text_color(0, 0, 0)
            width = self.get_string_width(item["header"])

            self.cell(width, 8, item["header"] + " :")
            self.ln()

            self.set_font("Times", "I", 15)
            width = self.get_string_width(info[0])

            self.cell(width, 8, info[0])
            self.cell(10)

            link = info[1].replace("##", ":")
            self.set_text_color(0, 0, 255)
            width = self.get_string_width(info[2])

            self.cell(width, 8, info[2], link = link)
            self.set_font("Times", "B", 15)
            self.set_text_color(0, 0, 0)
            self.ln()

        else:
            pass

    def arrangecontact(self):
        
        #This function is used to create the contact section of the cv
        settings = self.getsettings()
        info = settings["contact"]
        self.set_font("Times", "I", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

    def arrangeedu(self):
        #This function is used to create the education section of the cv

        self.set_font("Times", "I", 32)
        self.cell(0, 10, "Education")
        self.ln(15)

        settings = self.getsettings()
        info = settings["education"]
        self.set_font("Times", "I", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

    def arrangeexp(self):
        #This function is used to create the experience section of the cv

        self.set_font("Times", "I", 32)
        self.cell(0, 10, "Experience")
        self.ln(15)

        settings = self.getsettings()
        info = settings["experience"]
        self.set_font("Times", "I", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

    def arrangeskill(self):
        #This function is used to create the skills section of the cv

        self.set_font("Times", "I", 32)
        self.cell(0, 10, "Computer Skills")
        self.ln(15)

        settings = self.getsettings()
        info = settings["skills"]
        self.set_font("Times", "I", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

    def arrangeachieve(self):
        #This function is used to create the achievement section of the cv

        self.set_font("Times", "I", 32)
        self.cell(0, 10, "Achivements")
        self.ln(15)

        settings = self.getsettings()
        info = settings["achievments"]
        self.set_font("Times", "B", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

    def arrangeproject(self):
        #This function is used to create the projects section of the cv

        self.set_font("Times", "I", 32)
        self.cell(0, 10, "Current Project")
        self.ln(15)

        settings = self.getsettings()
        info = settings["projects"]
        self.set_font("Times", "B", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

    def arrangelanguage(self):
        #This function is used to create the language section of the cv

        self.set_font("Times", "I", 32)
        self.cell(0, 10, "International Language")
        self.ln(15)

        settings = self.getsettings()
        info = settings["languages"]
        self.set_font("Times", "I", 15)

        for item in info:
            item = self.getdata(item)
            kind = item["type"]
            data = item["data"]
            self.pertype(kind, data, item)

        x = self.get_x()
        y = self.get_y()

        self.line(0, y, 300, y)

if __name__ == "__main__":
    """
    This doesn't need any explaination
    """
    pdf = CV()
    pdf.getsettings()
    pdf.set_author(pdf.getsettings()["title"])
    pdf.set_title("CV")
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.head()
    pdf.arrangecontact()
    pdf.arrangeedu()
    pdf.arrangeexp()
    pdf.arrangeskill()
    pdf.arrangeachieve()
    pdf.arrangeproject()
    pdf.arrangelanguage()
    pdf.output("cv.pdf", "F")