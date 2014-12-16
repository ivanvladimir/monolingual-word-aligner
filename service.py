# Flask imports                                                                
from flask import Flask, jsonify                    
from aligner import align
import codecs

app = Flask('service')

stopwords={}
with codecs.open("stopwords_en.txt",'r','utf-8') as file:
    stopwords['en']=[]
    for line in file:                                                      
       line=line.strip()                                                  
       if len(line)>0 and not line[0]=='#':                               
            stopwords['en'].append(line)                                         

def prop_al(al,lang='en'):
    num= [i for i,j in al[1] if i not in stopwords[lang]]
    return 1.0*len(num)/len([x for x in al[2] if x not in stopwords[lang]])
            
@app.route("/en/compare/<string:sntc1>/<string:sntc2>")                                         
def compareweb(sntc1,sntc2):
    sntc1=sntc1.replace('+',' ')
    sntc2=sntc2.replace('+',' ')
    res=align(sntc1,sntc2)
    prop_1=prop_al(res)    
    res=align(sntc2,sntc1)
    prop_2=prop_al(res)    
    sim=2*prop_1*prop_1/(prop_1+prop_2)

    return str(sim) 

@app.route("/es/compare/<string:sntc1>/<string:sntc2>")                                         
def comparewebes(sntc1,sntc2):
    sntc1=sntc1.replace('+',' ')
    sntc2=sntc2.replace('+',' ')
    res=align(sntc1,sntc2,lang='spanish')
    prop_1=prop_al(res)    
    res=align(sntc2,sntc1)
    prop_2=prop_al(res)    
    sim=2*prop_1*prop_1/(prop_1+prop_2)

    return str(sim) 


@app.route("/align/en/<string:sntc1>/<string:sntc2>")                                         
def alignweb(sntc1,sntc2):
    res={'result':align(sntc1,sntc2)}
    return jsonify(res) 


# Managing experiments                                                         
if __name__ == '__main__':                                                     
    app.debug = True;                                                          
    app.run()   
