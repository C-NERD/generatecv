from fpdf import FPDF as pdf
from pathlib import Path
from json import loads

ROOTDIR = Path(__file__).resolve().parent.parent

class CV(pdf):
    '''
    call upon the class CV to create you cv based off the infomation in the
    settings.json file. to know how to input info to settings.json refer
    back to the github page of this project please
    '''

    def initialise(self):
        try:
            file = open(ROOTDIR / 'assets/settings.json', 'r')
            self.data = loads(file.read())
            self.settings = self.data['settings']
            file.flush()
            file.close()

            if not Path(ROOTDIR / 'assets/img/link.png').is_file():
                print('Could not find the image file link.png in assets/img')
                print('Exiting program...')
                quit(-1)

            fill = self.settings['background']
            color = self.settings['color']
            self.add_page()
            self.set_fill_color(fill[0], fill[1], fill[2])
            self.set_text_color(color[0], color[1], color[2])
            

        except:
            print('Could not find settings.json file in the root directory')
            print('Exiting program...')
            quit(-1)

    def createtopic(self, name, lines : int = 0):
        self.set_font(self.settings['font_family'], 'B', int(self.settings['topic_font_size']))
        height = int(self.settings['topic_font_size']) * 0.5
        self.cell(0, height, name, fill = True)
        self.ln(height)
        self.ln(lines)

    def createtitle(self):
        self.createtopic(self.data['name'], 10)

    def createcontact(self):
        #This function is used to create the contact section of the cv
        contacts = self.data['contact']
        self.createtopic('Contact')
        self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))

        for item in contacts:
            info = '{} : {} '.format(item['type'], item['name'])
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)
            self.cell(5)
            x = self.get_x() 
            y = self.get_y() + int(height * 0.25)

            if item['link'].strip() != '':
                image_size = int(int(self.settings['sentence_font_size']) * 0.3)
                self.image(str(ROOTDIR / 'assets/img/link.png'), x = x, y = y, w = image_size, h = image_size, link = item['link'])

            self.ln(height)

        self.ln(10)

    def createeducation(self):
        #This function is used to create the contact section of the cv
        eduction = self.data['education']
        self.createtopic('Education')
        self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))

        for item in eduction:
            info = '{} :    {}      '.format(item['name'], item['institution'])
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)

            self.set_font(self.settings['font_family'], 'I', int(self.settings['sentence_font_size']))
            self.write(height, '{} to {} '.format(item['start_date'], item['end_date']))

            self.cell(5)
            x = self.get_x() 
            y = self.get_y() + int(height * 0.25)

            if item['link'].strip() != '':
                image_size = int(int(self.settings['sentence_font_size']) * 0.3)
                self.image(str(ROOTDIR / 'assets/img/link.png'), x = x, y = y, w = image_size, h = image_size, link = item['link'])

            self.ln(height)

        self.ln(10)

    def createexperience(self):
        #This function is used to create the contact section of the cv
        experience = self.data['experience']
        self.createtopic('Experience')

        for item in experience:
            self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))
            
            tools = ' | '.join(item['tools'])
            info = '{} :    {}     '.format(item['name'], tools)
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)

            self.set_font(self.settings['font_family'], 'I', int(self.settings['sentence_font_size']))
            self.write(height, '{} to {}   '.format(item['start_date'], item['end_date']))

            self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))
            self.write(height, item['work_place'])

            self.cell(5)
            x = self.get_x() 
            y = self.get_y() + int(height * 0.25)

            if item['link'].strip() != '':
                image_size = int(int(self.settings['sentence_font_size']) * 0.3)
                self.image(str(ROOTDIR / 'assets/img/link.png'), x = x, y = y, w = image_size, h = image_size, link = item['link'])

            self.ln(height)
            self.ln(10)

    def createskill(self):
        #This function is used to create the contact section of the cv
        skills = self.data['skills']
        self.createtopic('Skills')
        self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))

        for item in skills:

            libs = ' | '.join(item['libraries'])
            info = '{} :    {}'.format(item['name'], libs)
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)
            self.ln(height)

        self.ln(10)
        
    def createachivement(self):
        #This function is used to create the contact section of the cv
        achivements = self.data['achievments']
        self.createtopic('Achivements')
        self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))

        for item in achivements:
            info = '{} :    {}'.format(item['name'], item['description'])
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)
            self.cell(5)
            x = self.get_x() 
            y = self.get_y() + int(height * 0.25)

            if item['link'].strip() != '':
                image_size = int(int(self.settings['sentence_font_size']) * 0.3)
                self.image(str(ROOTDIR / 'assets/img/link.png'), x = x, y = y, w = image_size, h = image_size, link = item['link'])

            self.ln(height)

        self.ln(10)

    def createprojects(self):
        #This function is used to create the contact section of the cv
        projects = self.data['projects']
        self.createtopic('Achivements')
        self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))

        for item in projects:
            info = '{} :    {}'.format(item['name'], item['description'])
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)
            self.cell(5)
            x = self.get_x() 
            y = self.get_y() + int(height * 0.25)

            if item['link'].strip() != '':
                image_size = int(int(self.settings['sentence_font_size']) * 0.3)
                self.image(str(ROOTDIR / 'assets/img/link.png'), x = x, y = y, w = image_size, h = image_size, link = item['link'])

            self.ln(height)
            self.ln(10)

    def createlanguages(self):
        #This function is used to create the contact section of the cv
        languages = self.data['languages']
        self.createtopic('Languages')
        self.set_font(self.settings['font_family'], '', int(self.settings['sentence_font_size']))

        for item in languages:
            info = '{} :    {}'.format(item['name'], item['description'])
            height = int(self.settings['sentence_font_size']) * 0.5

            self.write(height, info)
            self.ln(height)

        self.ln(10)


if __name__ == "__main__":
    """
    This doesn't need any explaination
    """
    pdf = CV()
    pdf.initialise()
    pdf.createtitle()
    pdf.createcontact()
    pdf.createeducation()
    pdf.createexperience()
    pdf.createskill()
    pdf.createachivement()
    pdf.createprojects()
    pdf.createlanguages()
    pdf.output(ROOTDIR / "cv.pdf", "F")