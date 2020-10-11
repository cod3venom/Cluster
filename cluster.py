from Vendors.AWS import AWS
from Server import Server
_server = Server("UDP")


strs = Strings()
aws = AWS()
# with open("/opt/lampp/htdocs/silicon/Stuxnet/Spider/Extractor/Selectors/log.txt","r", encoding="utf8") as reader:
#     content = str(reader.read()).strip()
#     lines = content.split("\n")
#     for line in lines:
#         stack = strs.getKeyandVal(strs.Clean(line),'~')
#         aws.Segregate(stack)
#     aws.end = True
#     aws.Segregate("")



