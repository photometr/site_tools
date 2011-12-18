#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 02:50:23 2011

@author: Dmitriy Blinov
"""
import sys,os
import time
import math
from urllib2 import urlopen
from urllib2 import URLError
import lxml.html
from StringIO import StringIO
import webbrowser

year_start = 1990
year_end = 2011
"""
FIXME strange but it's the same for reffered and only articles now
#reffered
url_start = "http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PRE&qform=AST&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&sim_query=YES&ned_query=YES&adsobj_query=YES&aut_logic=OR&obj_logic=OR&author=Hagen-thorn%2C+V.+A.%2C%0D%0ALarionov%2C+V.+M.%2C%0D%0AJorstad%2C+S.+G.%2C%0D%0AKopatskaya%2C+E.+N.%2C%0D%0ALarionova%2C+E.+G.%2C%0D%0AJorstad%2C+S.+G.%2C%0D%0AMorozova%2C+D.+A.%2C%0D%0ABlinov%2C+D.+A.%2C%0D%0APolyakova%2C+T.+A.%2C%0D%0AShalyapina%2C+L.+V.%2C%0D%0AReshetnikov%2C+V.+P.%2C%0D%0AMerkulova%2C+O.+A.%2C%0D%0AYakovleva%2C+V.+A.%2C%0D%0AKarataeva%2C+G.+M.%2C%0D%0AKonstantinova%2C+T.+S.&object=&start_mon=&start_year="
url_midle = "&end_mon=&end_year="
url_end = "&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=500&start_nr=1&jou_pick=NO&ref_stems=&data_and=ALL&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&data_type=SHORT&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&obj_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1"
"""
"""
# only articles
url_start = "http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PRE&qform=AST&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&sim_query=YES&ned_query=YES&adsobj_query=YES&aut_logic=OR&obj_logic=OR&author=Hagen-thorn%2C+V.+A.%2C%0D%0ALarionov%2C+V.+M.%2C%0D%0AJorstad%2C+S.+G.%2C%0D%0AKopatskaya%2C+E.+N.%2C%0D%0ALarionova%2C+E.+G.%2C%0D%0AJorstad%2C+S.+G.%2C%0D%0AMorozova%2C+D.+A.%2C%0D%0ABlinov%2C+D.+A.%2C%0D%0APolyakova%2C+T.+A.%2C%0D%0AShalyapina%2C+L.+V.%2C%0D%0AReshetnikov%2C+V.+P.%2C%0D%0AMerkulova%2C+O.+A.%2C%0D%0AYakovleva%2C+V.+A.%2C%0D%0AKarataeva%2C+G.+M.%2C%0D%0AKonstantinova%2C+T.+S.&object=&start_mon=&start_year="
url_midle = "&end_mon=&end_year="
url_end = "&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=500&start_nr=1&article_sel=YES&jou_pick=NO&ref_stems=&data_and=ALL&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&data_type=SHORT&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&obj_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1"
"""
#all
url_start = "http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=AST&db_key=PRE&qform=AST&arxiv_sel=astro-ph&arxiv_sel=cond-mat&arxiv_sel=cs&arxiv_sel=gr-qc&arxiv_sel=hep-ex&arxiv_sel=hep-lat&arxiv_sel=hep-ph&arxiv_sel=hep-th&arxiv_sel=math&arxiv_sel=math-ph&arxiv_sel=nlin&arxiv_sel=nucl-ex&arxiv_sel=nucl-th&arxiv_sel=physics&arxiv_sel=quant-ph&arxiv_sel=q-bio&sim_query=YES&ned_query=YES&adsobj_query=YES&aut_logic=OR&obj_logic=OR&author=Hagen-thorn%2C+V.+A.%2C%0D%0ALarionov%2C+V.+M.%2C%0D%0AJorstad%2C+S.+G.%2C%0D%0AKopatskaya%2C+E.+N.%2C%0D%0ALarionova%2C+E.+G.%2C%0D%0AJorstad%2C+S.+G.%2C%0D%0AMorozova%2C+D.+A.%2C%0D%0ABlinov%2C+D.+A.%2C%0D%0APolyakova%2C+T.+A.%2C%0D%0AShalyapina%2C+L.+V.%2C%0D%0AReshetnikov%2C+V.+P.%2C%0D%0AMerkulova%2C+O.+A.%2C%0D%0AYakovleva%2C+V.+A.%2C%0D%0AKarataeva%2C+G.+M.%2C%0D%0AKonstantinova%2C+T.+S.&object=&start_mon=&start_year="
url_midle = "&end_mon=&end_year="
url_end = "&ttl_logic=OR&title=&txt_logic=OR&text=&nr_to_return=200&start_nr=1&jou_pick=ALL&ref_stems=&data_and=ALL&group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&data_type=SHORT&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&obj_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1"

"""
Hagen-thorn, V. A.,
Larionov, V. M.,
Jorstad, S. G.,
Kopatskaya, E. N.,
Larionova, E. G.,
Jorstad, S. G.,
Morozova, D. A.,
Blinov, D. A.,
Polyakova, T. A.,
Shalyapina, L. V.,
Reshetnikov, V. P.,
Merkulova, O. A.,
Yakovleva, V. A.,
Karataeva, G. M.,
Konstantinova, T. S.
"""

def SaveData(data):
    fop = open("ads.html",'w')
    fop.write(data)
    fop.close()

def GetData(year):
    url = url_start + year + url_midle + year + url_end
    try:
        f = urlopen(url)
        s = f.read()
        f.close()
    except URLError, e:
        print e
        SaveData(" ")
        return " "
    else:
        SaveData(s)
        return s

def GetData1(url):
    fop = open("ads.html",'r')
    s = fop.read()
    fop.close()
    return s

def Parse(data):
    n_pub = 0
    pars = lxml.html.etree.HTMLParser()
    tree = lxml.html.etree.parse(StringIO(data),pars)
    for parent in tree.getiterator():
      if parent.tag == "table":
	for i in range(len(parent)):
	  if parent[i].tag == "tr":
	    if len(parent[i]) > 2:
	      if parent[i][1].attrib.has_key("valign") and  parent[i][1].attrib["valign"] == "baseline":
		n_pub = n_pub + 1
    return n_pub

def main():
    for year in range(year_start,year_end+1):
      time.sleep(9)
      print year, Parse(GetData(str(year)))



if __name__ == '__main__':
    main()
