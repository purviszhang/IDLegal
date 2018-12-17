from IDlegal import Idlegal

class TestClass(object):
    def test_one(self):
        id = "660821199306273694"
        t = Idlegal(id)
        t.check()
        x=t.msg
        print(t.msg)
        assert '身份证地区不合法' in x

    def test_two(self):
        id = "610821999306273694"
        t = Idlegal(id)
        t.check()
        x = t.msg
        print(t.msg)
        assert '身份证出生日期不合法' in x

    def test_three(self):
        id = "61082119930627369X"
        t = Idlegal(id)
        t.check()
        x = t.msg
        print(t.msg)
        assert '身份证校验位不合法' in x

    def test_four(self):
        id = "610821199306273694666666"
        t = Idlegal(id)
        t.check()
        x = t.msg
        print(t.msg)
        assert '身份证长度不合法' in x

    def test_five(self):
        id = "610821199306273694"
        t = Idlegal(id)
        t.check()
        x = t.msg
        print(t.msg)
        assert id in x

    def test_six(self):
        id = "999999770706001"
        t = Idlegal(id)
        t.check()
        x=t.msg
        print(t.msg)
        assert '身份证地区不合法' in x

    def test_seven(self):
        id = "320311779906001"
        t = Idlegal(id)
        t.check()
        x = t.msg
        print(t.msg)
        assert '身份证出生日期不合法' in x

    def test_eight(self):
        id = "320311770706002"
        t = Idlegal(id)
        t.check()
        x = t.msg
        print(t.msg)
        assert id in x