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
