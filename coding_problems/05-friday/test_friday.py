import pytest

from friday import is_valid_IP


def test_basic_test_1():
    assert is_valid_IP('12.255.56.1') == True


def test_basic_test_2():
    assert is_valid_IP('') == False


def test_basic_test_3():
    assert is_valid_IP('abc.def.ghi.jkl') == False


def test_basic_test_4():
    assert is_valid_IP('123.456.789.0') == False


def test_basic_test_5():
    assert is_valid_IP('12.34.56') == False


def test_basic_test_6():
    assert is_valid_IP('12.34.56 .1') == False


def test_basic_test_7():
    assert is_valid_IP('12.34.56.-1') == False


def test_basic_test_8():
    assert is_valid_IP('123.045.067.089') == False


def test_basic_test_9():
    assert is_valid_IP('127.1.1.0') == True


def test_basic_test_10():
    assert is_valid_IP('0.0.0.0') == True


def test_basic_test_11():
    assert is_valid_IP('0.34.82.53') == True


def test_basic_test_12():
    assert is_valid_IP('192.168.1.300') == False


def test_invalid_ip_1():
    assert is_valid_IP('') == False


def test_invalid_ip_2():
    assert is_valid_IP('abc.def.ghi.jkl') == False


def test_invalid_ip_3():
    assert is_valid_IP('123.456.789.0') == False


def test_invalid_ip_4():
    assert is_valid_IP('12.34.56') == False


def test_invalid_ip_5():
    assert is_valid_IP('01.02.03.04') == False


def test_invalid_ip_6():
    assert is_valid_IP('256.1.2.3') == False


def test_invalid_ip_7():
    assert is_valid_IP('1.2.3.4.5') == False


def test_invalid_ip_8():
    assert is_valid_IP('123,45,67,89') == False


def test_invalid_ip_9():
    assert is_valid_IP('1e0.1e1.1e2.2e2') == False


def test_invalid_ip_10():
    assert is_valid_IP(' 1.2.3.4') == False


def test_invalid_ip_11():
    assert is_valid_IP('1.2.3.4 ') == False


def test_invalid_ip_12():
    assert is_valid_IP('12.34.56.-7') == False


def test_invalid_ip_12():
    assert is_valid_IP('1.2.3.4\n') == False


def test_invalid_ip_13():
    assert is_valid_IP('\n1.2.3.4') == False


def test_invalid_ip_14():
    assert is_valid_IP('123.045.067.089') == False


def test_valid_ip_1():
    assert is_valid_IP('0.0.0.0') == True


def test_valid_ip_2():
    assert is_valid_IP('123.45.67.89') == True


def test_valid_ip_3():
    assert is_valid_IP('255.255.255.255') == True


def test_valid_ip_4():
    assert is_valid_IP('1.2.3.4') == True


def test_valid_ip_5():
    assert is_valid_IP('31.41.59.26') == True


def test_valid_ip_6():
    assert is_valid_IP('53.58.97.93') == True


def test_valid_ip_7():
    assert is_valid_IP('238.46.26.43') == True


def test_valid_ip_8():
    assert is_valid_IP('38.32.79.50') == True


def test_valid_ip_9():
    assert is_valid_IP('28.84.197.169') == True


def test_valid_ip_10():
    assert is_valid_IP('39.93.75.105') == True


def test_valid_ip_11():
    assert is_valid_IP('82.0.97.49') == True


def test_valid_ip_12():
    assert is_valid_IP('44.59.230.78') == True


def test_valid_ip_13():
    assert is_valid_IP('164.0.62.86') == True


def test_valid_ip_14():
    assert is_valid_IP('208.99.86.28') == True


def test_valid_ip_15():
    assert is_valid_IP('0.34.82.53') == True


def test_valid_ip_16():
    assert is_valid_IP('42.117.0.67') == True


def test_valid_ip_17():
    assert is_valid_IP('98.214.80.86') == True


def test_valid_ip_18():
    assert is_valid_IP('51.32.82.30') == True


def test_valid_ip_19():
    assert is_valid_IP('66.47.0.93') == True


def test_valid_ip_20():
    assert is_valid_IP('84.46.0.95') == True


def test_valid_ip_21():
    assert is_valid_IP('50.58.22.31') == True


def test_valid_ip_22():
    assert is_valid_IP('72.53.59.40') == True


def test_valid_ip_23():
    assert is_valid_IP('81.28.48.1') == True


@pytest.mark.parametrize("a,b",
                         [('61.165.107.21c', False),
                          ('186..227.227', False),
                             ('4.136..75', False),
                             ('95.154.024.143', False),
                             ('110.118.100.162.55', False),
                             ('128.191.278.193', False),
                             ('128.207.062.238', False),
                             ('46.89.115.014', False),
                             ('174.65.192', False),
                             ('208.187.233.b', False),
                             ('46.238.00.222', False),
                             ('038.47.8.220', False),
                             ('12.35.115', False),
                             ('66.186.14.75', True),
                             ('207.105.-185.157', False),
                             ('ab117.183.111.145', False),
                             ('173.95.bc.205', False),
                             ('016.166.214.19', False),
                             ('234.78.163.107', True),
                             ('186.6.10.12ab', False),
                             ('a.40.32.225', False),
                             ('191.160.192.125', True),
                             ('163.-172.24.145', False),
                             ('11.184.231.', False),
                             ('154.117.249.144.216', False),
                             ('254.207.00.76', False),
                             ('170.290.172.72', False),
                             ('77..90.80', False),
                             ('133.85.c.220', False),
                             ('189.94.10.38d', False),
                             ('64.d.239.50', False),
                             ('73.-254.246.72', False),
                             ('150.131.254', False),
                             ('46.212.88.147', True),
                             ('b254.182.42.67', False),
                             ('107.185.103.184', True),
                             ('c.252.40.0', False),
                             ('237.110.158 .76', False),
                             ('78.234.200.169', True),
                             ('c76.203.248.76', False),
                             ('253.17.117.234', True),
                             ('de210.170.74.240', False),
                             ('59.15.01.33', False),
                             ('94.-211.46.227', False),
                             ('250.210.37.059', False),
                             ('58.137 .185.144', False),
                             ('214.121.8.234cd', False),
                             ('128.223.74.9.204', False),
                             ('248.50.74.292', False),
                             ('262.223.245.186', False),
                             ('97.47..154', False),
                             ('151.8.68.79a', False),
                             ('119.16.00.34', False),
                             ('117.219 .252.87', False),
                             ('b48.181.160.219', False),
                             ('51.96.40.089', False),
                             ('193.55.204 .65', False),
                             ('160.126.24', False),
                             ('182.205.129.094', False),
                             ('239.94.72.174.219', False),
                             ('166.49.121.42', True),
                             ('58.177.144.71', True),
                             ('c194.146.201.229', False),
                             ('115.141.255 .165', False),
                             ('030.52.155.42', False),
                             ('81.170.85.255d', False),
                             ('68.78.237.114', True),
                             ('207.174.281.77', False),
                             ('103.59.249.', False),
                             ('211.207 .133.187', False),
                             ('84.226 .55.75', False),
                             ('184.74.241.120ab', False),
                             ('5.51.156.164.58', False),
                             ('143.106.149.294', False),
                             ('166.-158.160.84', False),
                             ('b.92.168.238', False),
                             ('25.33.a.77', False),
                             ('00.123.103.234', False),
                             ('68.3.038.188', False),
                             ('193.118.144.35c', False),
                             ('201.186.105.42', True),
                             ('ab229.18.55.49', False),
                             ('100.182.104.15', True),
                             ('016.227.61.175', False),
                             ('57.132.4 .51', False),
                             ('212.137.16', False),
                             ('189.59.196', False),
                             ('2.149 .161.26', False),
                             ('251.103.-165.25', False),
                             ('171.038.78.33', False),
                             ('ab247.16.143.96', False),
                             ('65.4.14', False),
                             ('069.157.122.71', False),
                             ('c.188.184.233', False),
                             ('195.89.14', False),
                             ('135.11..53', False),
                             ('71.106.45.56.84', False),
                             ('22.30.74', False),
                             ('101.150 .131.168', False),
                             ('123.81.100.92', True),
                             ('174.95.64.065', False),
                             ('4.82.bc.163', False),
                             ('224.64.15.182de', False),
                             ('85.215.127.015', False),
                             ('00.206.101.61', False),
                             ('113.252.199.-30', False),
                             ('225.140.183', False),
                             ('176.153.77.040', False),
                             ('71.9.193.122cd', False),
                             ('133.264.79.171', False),
                             ('158.9.41.97b', False),
                             ('114.123.25.', False),
                             ('176.071.191.103', False),
                             ('125.174.181', False),
                             ('236.155.220.175.11', False),
                             ('17.140.212.00', False),
                             ('25..1.146', False),
                             ('206.27.127.-180', False),
                             ('136.67.65.162.111', False),
                             ('93.118.196.012', False),
                             ('227.277.96.154', False),
                             ('249.152.156.018', False),
                             ('.124.137.157', False),
                             ('153.d.48.162', False),
                             ('110.cd.249.60', False),
                             ('159.203.232.105cd', False),
                             ('112.-145.238.231', False),
                             ('172.88.15.62', True),
                             ('164.73.73.62.78', False),
                             ('272.76.65.244', False),
                             ('11.115.224.cd', False),
                             ('155.69.00.101', False),
                             ('92.231.187 .36', False),
                             ('61.00.25.74', False),
                             ('124.75 .106.249', False),
                             ('155.153.49', False),
                             ('183.de.248.67', False),
                             ('194.196.153.98bc', False),
                             ('50.206.299.65', False),
                             ('cd133.139.218.152', False),
                             ('121.21.84.125.7', False),
                             ('129.81.211.27.12', False),
                             ('a.184.68.228', False),
                             ('133.140.13.-31', False),
                             ('97.234.124.110', True),
                             ('21.00.193.30', False),
                             ('77.72.243.72.255', False),
                             ('195.171.193', False),
                             ('99.104.38.81.58', False),
                             ('162.025.93.160', False),
                             ('225.24.213.182.96', False),
                             ('94.78.85 .219', False),
                             ('161.204.273.99', False),
                             ('038.82.179.205', False),
                             ('243.209.79', False),
                             ('.73.66.210', False),
                             ('19.255.15.185cd', False),
                             ('17.129.278.48', False),
                             ('11.243.137', False),
                             ('16.193.224.96', True),
                             ('bc220.23.180.96', False),
                             ('275.27.163.108', False),
                             ('231.90.87 .169', False),
                             ('33..114.121', False),
                             ('193.73.-62.28', False),
                             ('42.226.213.229cd', False),
                             ('0.12.202', False),
                             ('215.278.70.43', False),
                             ('126..139.205', False),
                             ('8.255.00.14', False),
                             ('106.8.123.00', False),
                             ('158.97.073.151', False),
                             ('81.228.58.c', False),
                             ('cd92.141.136.21', False),
                             ('179.74.228.', False),
                             ('115.111.73.171', True),
                             ('.147.98.128', False),
                             ('203.84.132.53cd', False),
                             ('265.133.41.5', False),
                             ('166.131.151', False),
                             ('89.99.198.196.251', False),
                             ('19.42.52.045', False),
                             ('68.208.223.259', False),
                             ('157.68.293.106', False),
                             ('49.153.240.213', True),
                             ('249.197.214.072', False),
                             ('134.231.115 .21', False),
                             ('26.32.93 .45', False),
                             ('154.17.241 .199', False),
                             ('ab100.162.157.147', False),
                             ('b196.66.242.81', False),
                             ('171.c.160.96', False),
                             ('3.-70.197.141', False),
                             ('203.251..33', False),
                             ('202.265.145.249', False),
                             ('78.246.110', False),
                             ('133.00.192.153', False),
                             ('ab.154.175.77', False),
                             ('b.81.146.252', False),
                             ('101.49..65', False),
                             ('254.213.3.120', True),
                             ('117.192.249.081', False),
                             ('127.13.00.233', False),
                             ('141.101 .215.234', False),
                             ('249.147.243.22cd', False),
                             ('cd247.44.240.190', False),
                             ('262.8.57.74', False),
                             ('136.192.174.25.172', False),
                             ('32.51.194.279', False),
                             ('201.37.71', False),
                             ('00.195.26.61', False),
                             ('208.101..254', False),
                             ('199.122.10.120d', False),
                             ('113.41.116 .99', False),
                             ('.235.214.110', False),
                             ('206.de.166.168', False),
                             ('114.127.210.95.180', False),
                             ('06.193.196.167', False),
                             ('143.255.275.25', False),
                             ('104.10.249.253', True),
                             ('293.61.240.43', False),
                             ('145.00.49.82', False),
                             ('197.68.211 .158', False),
                             ('221.140.cd.74', False),
                             ('184.76.-68.184', False),
                             ('219.139.197.213cd', False),
                             ('188.c.177.82', False),
                             ('39.255.141.144.146', False),
                             ('71.110 .245.163', False),
                             ('29.159.022.37', False),
                             ('95.95.31.211.42', False),
                             ('60.-240.4.147', False),
                             ('73.251.21.66cd', False),
                             ('299.229.23.75', False),
                             ('37.113.158.201.92', False),
                             ('28.93.097.109', False),
                             ('276.139.74.152', False),
                             ('-241.210.180.59', False),
                             ('73..102.149', False),
                             ('d11.142.51.107', False),
                             ('73.36.138.140', True),
                             ('72.36.61', False),
                             ('a197.229.204.112', False),
                             ('144.77.243', False),
                             ('a.122.44.240', False),
                             ('0.207.26.c', False),
                             ('1.105.109.299', False),
                             ('6.93.189.76de', False),
                             ('90..54.91', False),
                             ('244.34.cd.166', False),
                             ('bc66.219.73.138', False),
                             ('147.4.62.71.148', False),
                             ('146.00.92.26', False),
                             ('14.246.70', False),
                             ('191.225.62.211', True),
                             ('123.77.188.', False),
                             ('229.38.186 .121', False),
                             ('26.95.156.b', False),
                             ('ab.220.227.136', False),
                             ('49.76.213.65.104', False),
                             ('91.124.37.261', False),
                             ('229.173.-182.106', False),
                             ('de104.226.139.229', False),
                             ('090.168.96.103', False),
                             ('57.115.190.88b', False),
                             ('192.-108.73.172', False),
                             ('250.126.214.69', True),
                             ('165.132.68.-98', False),
                             ('226.b.184.94', False),
                             ('184.207.45.00', False),
                             ('217.96 .206.5', False),
                             ('187.63.41', False),
                             ('103.202.43.240ab', False),
                             ('70.141.91.123d', False),
                             ('a17.237.90.6', False),
                             ('208.62.145 .123', False),
                             ('108.064.126.41', False),
                             ('159.215 .232.33', False),
                             ('246.228.9 .61', False),
                             ('104.-163.107.86', False),
                             ('97.13 .9.205', False),
                             ('52.132.162.85.107', False),
                             ('61.172.28.-48', False),
                             ('cd196.28.160.197', False),
                             ('207.62.82.00', False),
                             ('113.194.29.-198', False),
                             ('00.161.190.224', False),
                             ('190.172.33.168.4', False),
                             ('219.158.7.278', False),
                             ('236.191.187.72.183', False),
                             ('157.64.36.3', True),
                             ('45.201.250 .34', False),
                             ('208.2.194.', False),
                             ('85.39.60.00', False),
                             ('85.168.-104.127', False),
                             ('253.61..145', False),
                             ('218.255.155', False),
                             ('4.213.43', False),
                             ('8.119.176.', False),
                             ('91.40.b.247', False)])
def test_random_test_cases(a, b):
    assert is_valid_IP(a) == b
