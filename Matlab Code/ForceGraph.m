close all
clear all

%Data
weight = [0
    100
200
300
400
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
]
weight = weight/1000*9.81


Reading = [0
    911
928
937
946
948
955
967
972
976
979
982
983
985
986]


%plot
plot(Reading,weight)

 cf = fit(Reading,weight,'exp2')

 figure()
 plot(cf,Reading,weight)

 title("Calibration Curve of the Force Sensitive Resistor")
 ylabel("Applied force (N)")
 xlabel("Arduino Reading")



 %% ------------
data = csvread("Book3.csv",2,0);

SPHM1 = data(:,1)
SPHM1 = cf(SPHM1)

SPHM2 = data(:,2)
SPHM2 = cf(SPHM2)
SR1 =  data(:,3)
SR1 = cf(SR1)

SR2 = data(:,4)
SR2 = cf(SR2)
figure()
sgtitle("Applied force of serial-parallel hybrid manipulator")

time = 0:10/104:10

subplot(1,2,1)
 
plot(time,SPHM1)
xlabel("Time (s)")
ylabel("Force (N)")

subplot(1,2,2)
plot(time,SPHM2)
xlabel("Time (s)")

figure()
sgtitle("Applied force of serial manipulator")

subplot(1,2,1)
plot(time,SR1)
xlabel("Time (s)")
ylabel("Force (N)")

subplot(1,2,2)
plot(time,SR2)
xlabel("Time (s)")