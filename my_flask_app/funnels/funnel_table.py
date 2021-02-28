from flask import send_file
from my_flask_app.user.models import Funnel, Cost
from my_flask_app.funnels.view_commands import get_funnel_stats
import json
import os


def get_funnel_table():
    ajax_table = {"data": []}
    funnels = Funnel.query.filter_by().all()
    for funnel in funnels:
        funnel_json = get_funnel_stats(funnel.id)
        funnel_dict={"funnelname": None, "net_epc": None, "net_aov": None,"epc": None,"aov": None, "funnel_id":None}
        funnel_dict["funnelname"]=funnel_json['name']
        funnel_dict["net_epc"]=funnel_json['net_epc']
        funnel_dict["net_aov"]=funnel_json['net_aov']
        funnel_dict["epc"]=funnel_json['epc']
        funnel_dict["aov"]=funnel_json['aov']
        funnel_dict["funnel_id"]=funnel.id
        ajax_table['data'].append(funnel_dict.copy())
    print(ajax_table)
    
    return ajax_table

def get_csv(funnel_id):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    funnel_dict = get_funnel_stats(funnel_id)

    with open(dir_path + '\\test.csv', 'w+') as f:
        for key in funnel_dict.keys():
            f.write("%s,%s\n"%(key,funnel_dict[key]))
    return send_file(dir_path + '\\test.csv',
                     mimetype='text/csv',
                     attachment_filename='Stats.csv',
                     as_attachment=True)