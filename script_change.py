#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, os
import re
sys.path.append("C:\update\wms_edi")
from wms.utils import wms_conf

HOME = r"C:\update\wms_use\wms"

def sort_text(a):
    tmp1 = a.find('(')
    tmp2 = a.find(')')
    if 0 <= tmp1 <tmp2:
        return a[:tmp1+1] + ', '.join([ '='.join([j.strip() for j in i.strip().split('=')]) for i in a[tmp1+1:tmp2].split(',')]) + a[tmp2:]
    else:
        return a

class Hello(object):
    def __init__(self):
        self.const = None

def get_org_and_storage(f_all):
    tmp_begin = f_all.find('set_org_and_storage')
    tmp_end = f_all.find(')',tmp_begin)+1

def _get_org():
    pass
def _get_storage():
    pass

if __name__ == "__main__":
        ""
        self = Hello()
        self.const = wms_conf.WMSBaseInfo()
        home = HOME
        os.chdir(home)
        List_home = [l for l in os.listdir(u'.\\') if os.path.isdir(home+'\\'+l) ]
        
#        word = 'W0218, W0219, W0237, W0238, W0239, W0240, W0241, W0242, W0243, W0244, W0245, W0246, W0247, W0248, W0249, W0250, W0251, W0252, W0253, W0254, W0255, W0256, W0257, W0258, W0259, W0260, W0261, W0262, W0263, W0264, W0265, W0266, W0267, W0268, W0269, W0270, W0271, W0272, W0273, W0274, W0275, W0276, W0277, W0278, W0279, W0280, W0281, W0282, W0283, W0284, W0285, W0286, W0287, W0288, W0310, '
#        #word2 = 'W0030,W0031,W0035,W0041,W0044,W0045,W0059,W0106,W0111,W0114,W0319,W0320,W0157,W0161,W0169,W0174,W0184,W0191,W0240,W0243,W0248,W0254,W0259,W0269,W0282,W0301,W0308,W0015,W0019,W0067,W0069,W0075,W0077,W0080,W0088,W0092,W0095,W0102,W0215'
#        not_word = ['W0192', 'W0193', 'W0077', 'W0078', 'W0079', 'W0003', 'W0094', 'W0095', 'W0096']
#        
#        new_word = 'W0081, W0082, W0083, W0084, W0085, W0086, W0087, W0088, W0089, W0090, W0091, W0092, W0093, W0097, W0098, W0099, W0100, W0101, W0102, W0103, W0116, W0117, W0118, W0119, W0120, W0121, W0122, W0123, W0124, W0125, W0126, W0127, W0128, W0129, W0130, W0131, W0132, W0133, W0134, W0136, W0137, W0138, W0139, W0140, W0141, W0143, W0145, W0146, W0147, W0148, W0149, W0150, W0151, W0152, W0153, W0154, W0155, W0220, W0221, W0222, W0223, W0224, W0225, W0226, W0227, W0228, W0229, W0230, W0231, W0232, W0233, W0234, W0235, W0236'
#        new_line = 'W0165,W0161,W0160,W0169,W0168,W0162,W0183,W0181,W0187,W0004,W0186,W0189,W0166,W0167,W0158,W0172,W0173,W0177,W0174,W0175,W0159,W0219,W0191'
#        new_line2 = ''
        out_data, out_data2 = [],[]
        count1, count2, count3, count44 = 0, 0, 0, 0
#        for dir1 in [i for i in List_home if i != '.svn']:
#            count4 = 0
#            _dir = u'.\\' + dir1
#            List_home2 = [l for l in os.listdir(_dir) if os.path.isfile(_dir+'\\'+l) ]
#            for dir2 in [i for i in List_home2 if i[:2]=='W0' and i[-3:]=='.py']:
        warehouse = 'Findyourself'
        not_line = 'W0104,W0106,W0004,W0077,W0088,W0092,W0095,W0102'
#        for dir1 in [i for i in List_home if i != '.svn']:
#            _dir = u'.\\' + dir1
#            List_home2 = [l for l in os.listdir(_dir) if os.path.isfile(_dir+'\\'+l) ]
#            for dir2 in [i for i in List_home2 if i[:2]=='W0' and i[:5] not in [j.strip() for j in word.split(',')]+not_word and i[-3:]=='.py']:
        for dir1 in [i for i in List_home if i == 'so']:
            _dir = u'.\\' + dir1
            List_home2 = [l for l in os.listdir(_dir) if os.path.isfile(_dir+'\\'+l) ]
            for dir2 in [i for i in List_home2 if i[:2]=='W0001' and i[-3:]=='.py']:
#            for dir2 in [i for i in List_home2 if i[:2]=='W0' and i[:5] not in not_line.split(',') and i[-3:]=='.py']:
                
                count1 += 1
                flag1, flag2 = False, False
                to_text, to_text2 = '', ''
#                if dir2[:5] in not_word:
#                    print dir1+'\\'+dir2[:5]
                __dir = _dir + '\\' + dir2
                
                #######
                #数据读取
                #######
                with open(__dir,'r') as fp:
                    f_all = fp.read()
                    looking_for_sku_end = 0
                    looking_for_sku_beg = f_all.find('self.const.SKU', looking_for_sku_end)
                    sku_detail = []
#                    print dir1+'\\'+dir2[:5],
                    f_all = fp.read()
                    tmp_begin = f_all.find('set_org_and_storage')
                    tmp_end = f_all.find(')',tmp_begin)+1
#                    text = sort_text(f_all[tmp_begin: tmp_end] )
#                    print eval(text[text.find('storage='):][8:-1]),
#                    
                    while looking_for_sku_beg != -1:
                        looking_for_sku_end = f_all.find('\n', looking_for_sku_beg)
                        print f_all[looking_for_sku_beg:looking_for_sku_end]
#                        sku_detail.append(eval(f_all[looking_for_sku_beg:looking_for_sku_end]))
                        looking_for_sku_beg = f_all.find('self.const.SKU', looking_for_sku_end)

#                    print ', '.join(sku_detail)
#                    looking_for_loc_end = 0
#                    looking_for_loc_beg = f_all.find('self.const.LOC', looking_for_loc_end)
#                    loc_detail = []
#                    ii = 0
#                    while looking_for_loc_beg != -1 and ii < 10:
#                        looking_for_loc_end = f_all.find('\n', looking_for_loc_beg)
#                        loc_detail.append(eval(f_all[looking_for_loc_beg:looking_for_loc_end]))
#                        looking_for_loc_beg = f_all.find('self.const.LOC', looking_for_loc_end)
#                        ii += 1
#                    if sku_detail or loc_detail:
#                        count1 += 1
#                        print ','.join([(sku[:sku.find('#')].strip() if sku.find('#')>=0 else sku) for sku in sku_detail]),
#                        print ','.join([(loc[:loc.find('#')].strip() if loc.find('#')>=0 else loc) for loc in loc_detail])
#                    else:
#                        looking_for_sku_end2 = 0
#                        looking_for_sku_beg2 = f_all.find('SKU_', looking_for_sku_end2)
#                        while looking_for_sku_beg2 != -1:
#                            looking_for_sku_end2 = f_all.find('\n', looking_for_sku_beg2)
#                            sku_detail.append(','.join( [jj.strip() for jj in f_all[looking_for_sku_beg2:looking_for_sku_end2].replace("]",'').replace("'",'').replace('"','').split(',')]))
#                            looking_for_sku_beg2 = f_all.find('SKU_', looking_for_sku_end2)
#                            
#                        looking_for_loc_end2 = 0
#                        looking_for_loc_beg2 = f_all.find('LOC_', looking_for_loc_end2)
#                        while looking_for_loc_beg2 != -1:
#                            looking_for_loc_end2 = f_all.find('\n', looking_for_loc_beg2)
#                            loc_detail.append(','.join( [jj.strip() for jj in f_all[looking_for_loc_beg2:looking_for_loc_end2].replace("]",'').replace(")",'').replace("'",'').replace('"','').replace('uSENDSTAGE','').replace('SENDSTAGE','').split(',')]))
#                            looking_for_loc_beg2 = f_all.find('LOC_', looking_for_loc_end2)
#                        if sku_detail or loc_detail:
#                            count2 += 1
#                            print ','.join([(sku[:sku.find('#')].strip() if sku.find('#')>=0 else sku) for sku in sku_detail]),
#                            print ','.join([(loc[:loc.find('#')].strip() if loc.find('#')>=0 else loc) for loc in loc_detail])
#                        else:
#                            looking_for_loc_end3 = 0
#                            looking_for_loc_beg3 = f_all.find('LOC7_', looking_for_loc_end3)
#                            while looking_for_loc_beg3 != -1:
#                                looking_for_loc_end3 = f_all.find('\n', looking_for_loc_beg3)
#                                loc_detail.append(','.join( [jj.strip() for jj in f_all[looking_for_loc_beg3:looking_for_loc_end3].replace("'",'').replace("]",'').replace('"','').replace('uSENDSTAGE','').replace('SENDSTAGE','').split(',') if jj.strip()]))
#                                looking_for_loc_beg3 = f_all.find('LOC7_', looking_for_loc_end3)
#                                
#                            looking_for_sku_end3 = 0
#                            looking_for_sku_beg3 = f_all.find('SKU7_', looking_for_sku_end3)
#                            while looking_for_sku_beg3 != -1:
#                                looking_for_sku_end3 = f_all.find('\n', looking_for_sku_beg3)
#                                sku_detail.append(','.join( [jj.strip() for jj in f_all[looking_for_sku_beg3:looking_for_sku_end3].replace("'",'').replace("]",'').replace('"','').split(',')]))
#                                looking_for_sku_beg3 = f_all.find('SKU7_', looking_for_sku_end3)
#                            if sku_detail or loc_detail:
#                                count3 += 1
#                                print ','.join([(sku[:sku.find('#')].strip() if sku.find('#')>=0 else sku) for sku in sku_detail]),
#                                print ','.join([(sku[:sku.find('#')].strip() if sku.find('#')>=0 else sku) for sku in loc_detail])
                    
#                    tmp_begin = f_all.find('from wms.utils import wms_conf')
#                    
#                    if f_all.find('from wms.utils import wms_conf',tmp_begin+10)>0:
#                        print dir1+'\\'+dir2[:5]
#                    
#                    tmp_begin2 = f_all.find('self.const = wms_conf.WMSBaseInfo()')
#                    if f_all.find('self.const = wms_conf.WMSBaseInfo()',tmp_begin2+10)>0:
#                        print dir1+'\\'+dir2[:5]
#                        
#                    if f_all.find('testbed.const')>0:
#                        print dir1+'\\'+dir2[:5]
#                    tmp_begin = f_all.find('from autobench_init.wms_autobench import autobench')
#                    tmp_end = f_all.find('\n',tmp_begin)
#                    text = sort_text(f_all[tmp_begin: tmp_end])
#                    to_text = text + '\n' + 'from wms.utils import wms_conf'
#                    count3 += 1
                    
#                    tmp_begin2 = f_all.find('self.const = testbed.const')
#                    tmp_end2 = f_all.find('\n',tmp_begin2)
#                    text2 = sort_text(f_all[tmp_begin2: tmp_end2])
#                    to_text2 = 'self.const = wms_conf.WMSBaseInfo()'
#                    to_file = f_all[:tmp_begin] + to_text + f_all[tmp_end:tmp_begin2] + to_text2 + f_all[tmp_end2:]
                    
#                    out_data.append(to_text)
#                    out_data2.append(to_text2)
                    
#                    tmp_begin2 = f_all.find('login.login')
#                    tmp_end2 = f_all.find(')',tmp_begin2)+1
#                    text2 = sort_text(f_all[tmp_begin2: tmp_end2])
#                    out_data2.append(dir1+'\\'+dir2[:5]+': ' + text2)
#                    tmp_begin = f_all.find('set_org_and_storage')
#                    tmp_end = f_all.find(')',tmp_begin)+1
#                    text = sort_text(f_all[tmp_begin: tmp_end] )
                    
                    
#                        print dir1+'\\'+dir2[:5]+': ' + text, text[text.find('const.ORGWH',text.find('const.ORGWH')+10):tmp_end]
#                    if text != '' and tmp_begin!=-1:
#                        print dir1+'\\'+dir2[:5]+': ' + text
#                        count3 += 1
##                    out_data.append(dir1+'\\'+dir2[:5]+': ' + text)
                
                #######
                #数据变更
                #######
                
                
#                if 'const.USER' not in text2 and text2!='':
#                    flag2 = True
#                    to_text2 = text2.replace('username="autotest"','username=self.const.USER.NAME'
#                                  ).replace('passwd="abc123"','passwd=self.const.USER.PASSWORD')
##                    out_data2.append(dir1+'\\'+dir2[:5]+': ' + to_text2)
#                    count2 += 1
#                    
#                if 'const.ORGWH' not in text and text!='':
#                    flag1 = True
#                if text != '' and text.find('const.ORGWH',text.find('const.ORGWH')+10)==-1:
#                    to_text = text.replace('org=u"自动化-ORG"','org=self.const.ORGWH.AUTO_ORG'
#                                 ).replace("org=u'自动化-ORG'",'org=self.const.ORGWH.AUTO_ORG'
#                                 ).replace('storage=u"EC3.0测试仓"','storage=self.const.ORGWH.AUTO_EC3_OFC'
#                                 ).replace("storage=u'EC3.0测试仓'",'storage=self.const.ORGWH.AUTO_EC3_OFC'
#                                 ).replace('storage=u"ST1.0测试仓"','storage=self.const.ORGWH.AUTO_ST1_OFC'
#                                 ).replace("storage=u'ST1.0测试仓'",'storage=self.const.ORGWH.AUTO_ST1_OFC'
#                                 ).replace('storage=u"ST2.0测试仓"','storage=self.const.ORGWH.AUTO_ST2_OFC'
#                                 ).replace("storage=u'ST2.0测试仓'",'storage=self.const.ORGWH.AUTO_ST2_OFC'
#                                 ).replace('storage=u"LPN3.0测试仓"','storage=self.const.ORGWH.AUTO_LPN3_OFC'
#                                 ).replace("storage=u'LPN3.0测试仓'",'storage=self.const.ORGWH.AUTO_LPN3_OFC'
#                                 ).replace('storage=u"工单2.0测试仓"','storage=self.const.ORGWH.AUTO_GD2_OFC'
#                                 ).replace("storage=u'工单2.0测试仓'",'storage=self.const.ORGWH.AUTO_GD2_OFC'
#                                 ).replace('storage=u"GZL2.0测试仓"','storage=self.const.ORGWH.AUTO_GZL2_OFC'
#                                 ).replace("storage=u'GZL2.0测试仓'",'storage=self.const.ORGWH.AUTO_GZL2_OFC'
#                                 ).replace('storage=u"GZL1.0测试仓"','storage=self.const.ORGWH.AUTO_GZL1_OFC'
#                                 ).replace("storage=u'GZL1.0测试仓'",'storage=self.const.ORGWH.AUTO_GZL1_OFC'
#                                 ).replace('storage=u"KA测试仓"','storage=self.const.ORGWH.AUTO_KA_OFC'
#                                 ).replace("storage=u'KA测试仓'",'storage=self.const.ORGWH.AUTO_KA_OFC'
#                                 )
##                    out_data.append(dir1+'\\'+dir2[:5]+': ' +to_text)
#                    count1 += 1
                
                #######
                #数据保存
                #######
#                to_file = ''
#                if text != '' and to_text:
#                    to_file = f_all[:tmp_begin] + to_text + f_all[tmp_end:]
#                else:
#                    print dir1+'\\'+dir2[:5]+': ' + text
#                if flag1 and flag2:
#                    to_file = f_all[:tmp_begin2] + to_text2 + f_all[tmp_end2:tmp_begin] + to_text + f_all[tmp_end:]
#                elif flag1 and not flag2:
#                    to_file = f_all[:tmp_begin] + to_text + f_all[tmp_end:]
#                elif not flag1 and flag2:
#                    to_file = f_all[:tmp_begin2] + to_text2 + f_all[tmp_end2:]
#                
#                
#                if to_file!='':
#                    with open(__dir,'w') as to_fp:
#                        to_fp.writelines(r"﻿#!/usr/bin/env python"+'\n')
#                        to_fp.writelines(r"#-*- coding:utf-8 -*-"+'\n\n')
#                    
#                    with open(__dir,'a+') as to_fp2:
#                        to_fp2.seek(2)
#                        to_fp2.writelines(to_file[to_file.find('#####'):])
#                    
#                    print dir2[:5]+",", "Update"
                    
        print '\n',count1, count2, count3

        #
#        with open(r"C:\data1.txt",'w') as fp2:
#            for data in [i for i in out_data]: # if 'self.const' not in i]:
#                fp2.writelines(data + '\n')
#
#        with open(r"C:\data2.txt",'w') as fp2:
#            for data in [i for i in out_data2]: # if 'self.const' not in i]:
#                fp2.writelines(data + '\n')
                
                    
                    
