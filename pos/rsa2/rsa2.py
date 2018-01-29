#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 用于支付宝私钥rsa2签名，放在ipos/includes/aop/目录下和AopClient.php同级，在AopClient.php中调用

import sys
import base64   #加密模块
import rsa  #加密模块

#msg = 'sign_type=RSA2';
#key = '''-----BEGIN RSA PRIVATE KEY-----
#MIIEpAIBAAKCAQEAuxNDdpQtLS441peIR5U3SNDHkoqtQArAjifH1kcrtBZOTn9s8jaW7FnHGRI5T0DNNqQhoAjpG1z8QBL5X5QKB19gLjjIdXq6Gcxl7wegFB57/Wo+MoCZP+eTErLrVqVkTmD6nTnLkhjRc3rA1dxr1RbaHy8o9wZu+Vi+zo6wIDF9lDoSgRjBoRtmDfiDHELDN6PC06rBaLAEilYpiwTWaE4Ul3OgVllpTl1Y55/J9jTtUABxlkQPLRd2hbBvtosuMc99MDTlN1pdXL0xGmTGsmb7aNANgXvRCnjVA9DfYSRM9ggbQeq2UVZls5ror9yWeskqSKBfcO2XDGoEBodEnwIDAQABAoIBAHFFrrmj6t7Kd/vncMr3HKxoTg77DQAUApeQmr2yBlJalzuMiGj4iNW/XoBdunm0YQ1OwFVoT80TtmENnBU1TAU+yLv0AdywXPK2ApqC4XiNJMJCjDqEB0bcbv8JetnR9zRGIDkG/64MfPYRQ6W6e0hhN91d7s30BUnRZGcpmpdClubfPva6QPB8mLNA7Wn9+SRYiT8s0WuB2RCSeLEWs/r87vjqxw/vhDscHoG5Z0aY24117nrwR65o7QdK8Xo9IwNWgHkvFO7kT9ad+MJDkizFTYnazNGQeFgwCe3OSDHdKEUdwIWctScZ/IsBvLy8THuA9SVkuR7BJyIqZPZ5gNECgYEA5GqIRjn7w/IWlD3BrzE7yoJBl0j+9rDZO1Mb3dYDnCcSTXTOPPG4UDj/c4w9U7FrfI36hUsLUHzZwUK2zcuSt+Qo/kYZ3C0FT9rJE65lxbw7jWlbszpiq0tok7Mb/0EFsh97Der4bjk8zbC90ckDzSsvqGaELcHKpyztMY75sgMCgYEA0aquPOeP03YvnBnTZXC2+yu9qjVICcin4aaHQF5Xk919nrZob8ZjbC9WYE5+2qaWaOk8xbJVihfU9/QgrwGfnqwjmbB5AQctDNFbdKeXSj77dLZvx+H8PwtGyyeLxJPY0F5+DHqxB0KKxwjf2i3earyAQLkUrnSVM/ON2/HdzjUCgYARepF5BkDcyq6to1gp5tOTeIo6YGyaRggpgP+V5yWZkmfVI4YQpdKb2PC7T9T1jZMTEe5EuuxfuV4Uat2AO/67MattYcHi1lMcvDo81lCVZAUOmixZN7OLNhcHjmIrEzezXLNW6k8eaCTd/JNZ9U7kKVTZRxcARV8Tkd2IuE8lLwKBgQCWu+qABsoz8KfRxg9gwmQKtyuoDp43ynZHl/1snWbA+1+wltsGYM5hnLawjj5M268OxX/XcZplqTSG/o/wwW4MGR2PBHw57PrKWEkz2Li/u//zrKU4QpOij2zZ6RhmvxQE2aotNpfG7GPxK8Qjiw54FgTugyEHOvF5ZAP8uCoKcQKBgQCiPji7ZEsS9Kq41DptoxFZEi4RgWBQblRBuudOX6YQyveZ8VQW7Td5PnoitBlnjpDdUoocXdteL+qvOMlikBoyiu7cvsODOVzmiX4seCVSa9dsKfJGzAmCRzl6ud903BOW2M7CxNy66Oiffx5/1pK12gfC2S5a43DaEkgBAoGH0A==
#-----END RSA PRIVATE KEY-----'''

#print(sys.argv)

msg = sys.argv[1] #接收需要签名的数据
key = sys.argv[2] #接收私钥

private_key = rsa.PrivateKey.load_pkcs1(key)
strdata = rsa.sign(msg.encode(), private_key, 'SHA-256')
sign = base64.encodestring(strdata)
sign = sign.decode() #数据转string

print(sign)

'''
f = open("text.txt",'wb')
f.write(sign)
f.close()
'''
