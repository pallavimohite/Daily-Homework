class A:
    def m1(self):
        print("Inherit A ")
        l = ["python","c++","java"]
        print(l)

class B(A):
    def m2(self):
        print("Inherit B")
        l = ["c","c++","python"]
        print(l)

class C(A):
    def m3(self):
        print("Inherit C")
        d = {"python":50,"c++":45,"java":40}
        print(d)

class D:
    def m4(self):
        print("Inherit D")
        l = ["html","css","javascript"]
        print(l)

class E(B):
    def m5(self):
        print("Print E")
        l = [50,45,49]
        print(l)

class F(C,D):
    def m6(self):
        print("Print F")
        print("I already learn all the languages")

jay = E()
viru = F()

print("Method inherited by jay")
jay.m5()
jay.m2()
jay.m1()

print("Method inherited by viru")
viru.m6()
viru.m4()
viru.m3()
viru.m1()



#By using same method name
class A:
    def m1(self):
        print("Inherit A ")
        l = ["python","c++","java"]
        print(l)

class B(A):
    def m1(self):
        print("Inherit B")
        l = ["c","c++","python"]
        print(l)

class C(A):
    def m1(self):
        print("Inherit C")
        d = {"python":50,"c++":45,"java":40}
        print(d)

class D:
    def m1(self):
        print("Inherit D")
        l = ["html","css","javascript"]
        print(l)

class E(B):
    def m5(self):
        print("Print E")
        l = [50,45,49]
        print(l)

class F(C,D):
    def m6(self):
        print("Print F")
        print("I already learn all the languages")

jay = E()
viru = F()
jay.m1()   #It inherit method from class B .It gives first priority to C --> A --> D
viru.m1()  #It inherit method from class C

