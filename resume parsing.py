import tika
from tika import parser
import re
class ResumeParsing:
    def parseAnyFile():
        tika.initVM()
        parsed = parser.from_file("sample resume.docx")
        print(parsed["content"])
        print("------details after parsing resume--------")
        name=re.compile(r"([a-zA-Z]){3,}\s([a-zA-Z]){3,}")
        print("Name:"+re.search(name,parsed["content"]).group())
        ph=re.compile(r"(\d{10})")
        print("Phone Number:"+re.search(ph,parsed["content"]).group())
        mail = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
        print("Mail ID:"+re.search(mail,parsed["content"]).group())
        address =re.compile(r"[a-z\S0-9\S]+,\n+[a-zA-Z,\n]+[a-zA-Z.]")
        print("Address:"+re.search(address,parsed["content"]).group())
    if __name__=="__main__":
        parseAnyFile()

        
        
        
        
 output:
    
					CURRICULUM  VITAE


Paturi Anvesh
flatno-123/3,
nizampet,
kukatpally,
Hyderabad.
Email: anvesh_98@gmail.com
Phone No: +91-7508092027

CAREER OBJECTIVE: 
Seeking a position as a graphics designer in the field of media development at Pentagram Graphic Studio in London.

EDUCATIONAL QUALIFICATIONS:

Degree / Certificate                           Institution 	 			Year		CGPA/Percentage

B.Tech – CSE			         Lovely Professional Univeristy,	            Pursuing 		6  – IV Semester
				         Phagwara

Intermediate	   		         NRI Academy ,			               2013	              92.2 %
				         Hyderabad

SSC				         Bhashyam Public School,		               2011		94 %
                                                                   Hyderabad                                                                                               

TECHNICAL SKILLS:

Softwares     	        : MATLAB, Autocad,Microsoft Word
Languages 	        : C, C++, Java, HTML, CSS 


WORKSHOPS AND SEMINARS:
 
Hacktrack by AIESEC, Lovely Professional University, Phagwara, April 2014
International SWAM ROBOTICS Workshop from Technophilia Systems, Lovely Professional University, Phagwara, 
Jan 2014

EXTRA CURRICULAR ACTIVITIES: 

Participated in:
Stage play competition, Lovely Professional University, Phagwara, 2015
IPL auction Competition, Lovely Professional University, Phagwara, 2015
Intra School Kabadi Competition, Bhashyam public school, Hyderabad, 2009

AWARDS AND HONOURS: 

First Prize - University Level ROBOTICS Championship, Lovely Professional University, 2014
Second Prize - Intra School Dance Competition, Bhashyam Public school, 2007
First Prize – Group discussion, Prathiba Vidhya Nikethan Public School, 2005

LANGUAGES KNOWN:

English, Hindi, Telugu

HOBBIES:
 
Listening to music, Dancing , Playing badminton, watching movies



------details after parsing resume--------
Name:Paturi Anvesh
Phone Number:7508092027
Mail ID:anvesh_98@gmail.com
Address:flatno-123/3,
nizampet,
kukatpally,
Hyderabad.
        
