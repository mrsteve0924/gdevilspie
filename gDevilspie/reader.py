import gDevilspie.sparser as parser

def geo_parse(gstring):
        return

def stripper(listitem):
        return listitem.strip('"')

def not_checker(matdict,item):
        if item[0] == 'is':
                matdict[str(item[1].pop())] = ["is","not", stripper(item[2])]
        elif item[0] == 'matches':
                matdict[str(item[1].pop())] = ["matches","not", stripper(item[2])]
        elif item[0]== 'contains':
                matdict[str(item[1].pop())] = ["contains","not", stripper(item[2])]
    
def condition_checker(matdict,item):
        if item[0] == 'is':
                matdict[str(item[1].pop())] = ["is", stripper(item[2])]
        elif item[0] == 'matches':
                matdict[str(item[1].pop())] = ["matches", stripper(item[2])]
        elif item[0]== 'contains':
                matdict[str(item[1].pop())] = ["contains", stripper(item[2])]
        elif item[0]== "not":
                not_checker(matdict,item[1])

def read_file(filename):
# open a file and pass it to parser.py
        with open(filename, encoding="utf-8") as rule_file:
                z = parser.parse_file(rule_file)
# clean some of the parser crap
        rule = z[0]

#the dicts we will use
        matdict = {}
        actiondict = {}

#the reader part...
        if rule[0] == 'if':
                matcond = z[0][1]
                action = z[0][2]

        if matcond[0] in ("and", "begin"):
                for item in matcond:
                        condition_checker(matdict, item)
        else:
                condition_checker(matdict, matcond)


        if action[0] == 'begin':
                #FIXME: Handle Actions correctly.
                for i in action[1:]:
                        if len(i) > 1:
                                if ( i[1] == "'" ):
                                        last = len(i) - 1
                                        joint = " ".join(i[2:last])
                                        actiondict[i[0]] = stripper(joint)
                                else:
                                        actiondict[i[0]] = stripper(i[1])
                        elif i[0][:2] != "un":
                                actiondict[i[0]] = "True"
                        elif i[0][:2] == "un":
                                actiondict[i[0][2:]] = "False"
                                actiondict[i[0]] = "True"
        else:
                actiondict[action[0]] = stripper(action[1]) if len(action) > 1 else "True"

        return [matdict,actiondict]


#print read_file("test.ds")
#geo_parse("FIXME: Write that part phaeron :P")
