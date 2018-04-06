import matplotlib.pyplot as plt

data=open("test.txt")

t=[]
a=[]
v=[]
s=[]

for line in data:
    (_t, _a, _v, _s)=line.split()
    a.append(float(_a))
    t.append(float(_t))
    v.append(float(_v))
    s.append(float(_s))

data.close()

p1=plt.subplot(311)
p1.plot(t, s, label="position")
p1.set_xlabel("t(ms)")
p1.set_ylabel("Angle(°)")

p2=plt.subplot(312)
p2.plot(t, v, label="speed")
p2.set_xlabel("t(ms)")
p2.set_ylabel("Angular\nVelocity(°/ms)")

p3=plt.subplot(313)
p3.plot(t, a, label="acceleration")
p3.set_xlabel("t(ms)")
p3.set_ylabel("Angular\nAcceleration(°/(ms*ms))")

plt.show()
