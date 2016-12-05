import base64
import os
import urllib.parse
from anaurl2 import ana
import logging
import zipfile
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

logger=logging.getLogger()
if __name__=='__main__':
    logging.basicConfig(level='INFO')
    resu=ana("http://www.vpngate.net/cn/","<tr>\r\n<td class='vg_table_row_([01])' style='text-align: center;'><img src='../images/flags/[A-Z]+.png' width='32' height='32' /><br>([a-zA-Z]+)</td>.*?<a href='([^']+)'><img height='33' src='../images/yes_33.png' width='33' /><br><b>OpenVPN<BR>.*?</td></tr>")
    #resu=ana("http://www.vpngate.net/cn/do_openvpn.aspx?fqdn=&ip=219.118.128.235&tcp=995&udp=1195&sid=1477224598655&hid=817201",'(/common/openvpn_download.aspx.*?\.ovpn)')
    #logging.debug(resu)
    if(len(resu)<2):
        logging.info('error in level1:')
        logging.debug(resu)
    for tempa in resu:
        logging.debug(tempa)
        #sample item:
        #=============================================
        #('0', 'Thailand', 'do_openvpn.aspx?fqdn=&ip=171.97.1.83&tcp=1226&udp=1362&sid=1480854871939&hid=6276931')
        #=============================================
        urlheader='http://www.vpngate.net/cn/'
        fullurl=urlheader+tempa[2]
        loca=tempa[1]
        logging.debug(fullurl)
        resu2=ana(fullurl,'(/common/openvpn_download.aspx.*?\.ovpn)')
        logging.debug(resu2)
        for tempb in resu2:
            tempb=tempb.replace('amp;','')
            tempname=loca+"_"+tempb.rsplit('/',1)[-1]
            if("_udp_" not in tempname):
                break
            print(tempname)
            fileurl='http://www.vpngate.net/'+tempb
            logging.debug(fileurl)
            logging.debug("***************************************")
            resu3=ana(fileurl,'.*')
            #logging.debug(resu3)
            dir='/tmp/ovpn'
            try:
                os.stat(dir)
            except:
                os.mkdir(dir)
            with open('/tmp/ovpn/'+tempname,'w') as out:
                out.write(resu3[0])
            print('generated')
    #    break
        logging.debug("=============================================")
    print('finished generated all ovpn files')
    zipf = zipfile.ZipFile('/tmp/ovpn.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/tmp/ovpn', zipf)
    zipf.close()
    filez=open('/tmp/ovpn.zip','rb')
    file_c=filez.read()
    base64text=base64.b64encode(file_c).decode('ascii')
    with open('/tmp/base64.txt','w') as out:
        out.write(base64text)
