"order dict"
from collections import OrderedDict
favourite_langue =OrderedDict()

favourite_langue['jen']='python'
favourite_langue['sarah']='c'
favourite_langue['edward']='ruby'
favourite_langue['phil']='python'

for name ,language in favourite_langue.items():
    print(name.title()+"'s favorite language is "+language.title())
