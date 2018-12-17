import re
class Idlegal:

    def __init__(self,idnum):
        self.idnum=idnum
        self.msg=""

    def check(self):
        l = len(self.idnum)
        area = {"11": "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古",
                "21": "辽宁", "22": "吉林", "23": "黑龙江",
                "31": "上海", "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东",
                "41": "河南","42": "湖北", "43": "湖南", "44": "广东", "45": "广西", "46": "海南",
                "50": "重庆", "51": "四川", "52": "贵州","53": "云南", "54": "西藏",
                "61": "陕西", "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆",
                "71": "台湾",
                "81": "香港", "82": "澳门",
                "91": "国外"}
        def len15check(idnum):
            # 地区校验(校验前六位)
            if (idnum[0:2] not in area):
                self.msg="身份证地区不合法"
            else:
                # 出生日期校验(校验中间6位)
                if ((int(idnum[6:8]) + 1900) % 4 == 0 or ((int(idnum[6:8]) + 1900) % 100 == 0 and (int(idnum[6:8]) + 1900) % 4 == 0)):
                    ereg = re.compile(
                        '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
                else:
                    ereg = re.compile(
                        '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
                if (re.match(ereg, idnum)):
                    self.msg = str(self.idnum)+"合法"
                else:
                    self.msg = "身份证出生日期不合法"

        def len18check(idnum):
            # 地区校验(校验前六位)
            if (idnum[0:2] not in area):
                self.msg = "身份证地区不合法"
            else:
                # 出生日期校验(校验中间8位)
                if (int(idnum[6:10]) % 4 == 0 or (int(idnum[6:10]) % 100 == 0 and int(idnum[6:10]) % 4 == 0)):
                    ereg = re.compile(
                        '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')  # //闰年出生日期的合法性正则表达式
                else:
                    ereg = re.compile(
                        '[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')  # //平年出生日期的合法性正则表达式
                if (re.match(ereg, idnum)):
                    idnum = str(idnum)
                    idnum = idnum.strip()
                    idnum_list = list(idnum)
                    # //计算校验位
                    S = (int(idnum_list[0]) + int(idnum_list[10])) * 7 + (int(idnum_list[1]) + int(idnum_list[11])) * 9 + (int(idnum_list[2]) + int(idnum_list[12])) * 10 + (int(
                        idnum_list[3]) + int(idnum_list[13])) * 5 + (int(idnum_list[4]) + int(idnum_list[14])) * 8 + (int(idnum_list[5]) + int(idnum_list[15])) * 4 + (int(
                        idnum_list[6]) + int(idnum_list[16])) * 2 + int(idnum_list[7]) * 1 + int(idnum_list[8]) * 6 + int(idnum_list[9]) * 3
                    Y = S % 11
                    JYM = "10X98765432"
                    M = JYM[Y]  # 判断校验位
                    if (M == idnum_list[17]):  # 检测ID的校验位
                        self.msg = str(self.idnum)+"合法"
                    else:
                        self.msg = "身份证校验位不合法"
                else:
                    self.msg = "身份证出生日期不合法"

        if l==18:
            len18check(self.idnum)
        elif l==15:
            len15check(self.idnum)
        else:
            self.msg = "身份证长度不合法"








