close all
clear all

%Graph 1 - Trajectories

u_0 = 60
u_f = 120    
t_f = 5

a_0= u_0
a_3= (10/(t_f^3))*(u_f-u_0)
a_4= (-15/(t_f^4))*(u_f-u_0)
a_5= (6/(t_f^5))*(u_f-u_0)


t = 0:0.1:5
subplot(3,1,1);

traj = a_0 + a_3.*t.^3 + a_4.*t.^4 + a_5.*t.^5
plot(t,traj,'LineWidth',3)
hold on
u_0 = 120
u_f = 140    
t_f = 5

a_0= u_0
a_3= (10/(t_f^3))*(u_f-u_0)
a_4= (-15/(t_f^4))*(u_f-u_0)
a_5= (6/(t_f^5))*(u_f-u_0)


t = 5:0.1:10

traj2 = a_0 + a_3.*(t-5).^3 + a_4.*(t-5).^4 + a_5.*(t-5).^5

plot(t,traj2,'LineWidth',3)

u_0 = 140
u_f = 50    
t_f = 5

a_0= u_0
a_3= (10/(t_f^3))*(u_f-u_0)
a_4= (-15/(t_f^4))*(u_f-u_0)
a_5= (6/(t_f^5))*(u_f-u_0)


t = 10:0.1:15

traj3 = a_0 + a_3.*(t-10).^3 + a_4.*(t-10).^4 + a_5.*(t-10).^5

plot(t,traj3,'LineWidth',3)
title("Displacement, Velocity and Acceleration of trajectory")
ylabel("Displacement (m)")
grid on
subplot(3,1,2);

speed = diff(traj)
speed2 = diff(traj2)
speed3 = diff(traj3)

t = 0:(5/49):5
plot(t,speed,'LineWidth',3)
hold on
t = 5:(5/49):10
plot(t,speed2,'LineWidth',3)
t = 10:(5/49):15
plot(t,speed3,'LineWidth',3)
ylabel("Velocity (m/s)")
grid on
subplot(3,1,3);
accel = diff(speed3)
accel2 = diff(speed2)
accel3 = diff(speed3)
hold on
t = 0:(5/48):5

plot(t,accel,'LineWidth',3)
t = 5:(5/48):10

plot(t,accel2,'LineWidth',3)
t = 10:(5/48):15
plot(t,accel3,'LineWidth',3)


xlabel("Time (s)")
ylabel("Accelerations (m/s/s)")
grid on
figure()


%Graph 2 - Static Load Test
K=[0	0	0	0	0
0	0	0	0	0
0.05	0	0	0	0.05
0.1	0.1	0	0.1	0.1
0.2	0.1	0	0.1	0.2
0.2	0.2	0.05	0.2	0.2
0.3	0.2	0.1	0.2	0.3
0.3	0.2	0.15	0.2	0.3
0.4	0.2	0.2	0.2	0.4
0.4	0.3	0.27	0.3	0.4
0.4	0.3	0.4	0.3	0.4
0.5	0.4	0.5	0.4	0.5
0.6	0.5	0.6	0.5	0.6
]*10

Y = [0
50
100
150
200
250
300
350
400
450
500
550
600
]

X = [0 45 90 135 180]

X_new = 0:15:180
Y_new =  0:50:600

[xq,yq] = meshgrid(X_new, Y_new);
vq = griddata(X,Y,K,xq,yq);

surf(X_new,Y_new,vq)
grid off
caxis([0, 30])
colormap jet

title(["Displacement of parallel-serial hybrid ","robotic end effector from expected position"])
xlabel("Orientation of object from X axis (Degrees)")
ylabel("Applied Load (g)")
shading flat
a = colorbar
ylabel(a,"Displacemnt from expected position (mm)");
view(2)


figure()

K_2 = [0	0	0	0	0
1.2	1.179345223	0.695753675	1.898861248	1.374702951
1.6	1.351934946	1.454195575	2.481064194	1.407701792
2.1	2.370872545	1.922400671	2.277114818	2.181331338
2.5	1.983320686	2.788019631	3.107442341	2.749784908
3	2.683012106	2.502929337	3.837851858	3.069820332
3.3	2.871787634	3.665729537	3.928762539	3.5192289
3.8	3.271225147	4.039534035	4.012496223	3.949707855
4.1	3.653231088	4.012629399	3.991708627	4.233712709
4.6	4.533450888	4.625788484	5.075585195	4.580003646
5	5.090093421	4.731645767	5.239930346	5.687427651
5.3	4.780388244	5.59995119	5.534002283	6.035212285
5.7	5.588884982	5.550285096	6.483976135	5.668601842
]*10
vq_2 = griddata(X,Y,K_2,xq,yq);

surf(X_new,Y_new,vq_2*0.4)
caxis([0, 30]);
colormap jet
title(["Displacement of serial ","robotic end effector from expected position"])
xlabel("Orientation of object from X axis (Degrees)")
ylabel("Applied Load (g)")
a = colorbar
ylabel(a,"Displacemnt from expected position (mm)");
shading flat
colorbar
view(2)

grid off

%Graph 3 - Static load tests

Load = [0
50
100
150
200
250
300
350
400
450
500
550
600
]

Displacement_2 = [0
0
0
0
0
0.05
0.1
0.15
0.2
0.27
0.4
0.5
0.6
] *10
Displacement_1_under = [0
0.2
0.25
0.4
0.7
0.82
0.9
1
1.1
1.3
1.4
1.6
1.8
]*10
Displacement_1_over = [0
0.05
0.2
0.3
0.4
0.5
0.55
0.6
0.7
0.9
1.1
1.3
1.5
]*10
Displacement_0 = [0
1.2
1.6
2.1
2.5
3
3.3
3.8
4.1
4.6
5
5.3
5.7
]*10

figure()
plot(Load,Displacement_2,"*R")
hold on
plot(Load,Displacement_1_over,"*G")
plot(Load,Displacement_1_under,"*B")
plot(Load,Displacement_0,"*K")

set_val = 0:10:600
p1 = polyfit(Load,Displacement_2,1)
p2 = polyfit(Load,Displacement_1_over,1)
p3 = polyfit(Load,Displacement_1_under,1)
p4 = polyfit(Load,Displacement_0,1)


y1 = polyval(p1,set_val);
y2 = polyval(p2,set_val);
y3 = polyval(p3,set_val);
y4 = polyval(p4,set_val);

plot(set_val,y1,"R")
plot(set_val,y2,"G")
plot(set_val,y3,"B")
plot(set_val,y4,"K")

xlim([0,600])
ylim([-5,60])

title("Static load test of Serial-Paralel Hybrid (S-PH) Manipulator with object along Z axis")
legend("2 arm S-PH Manipulator","1 bottom mounted arm S-PH Manipulator","1 top mounted arm S-PH Manipulator","Serial Robotic Arm")
xlabel("Applied Load (g)")
ylabel("Displacemnt from expected position (mm)")


%3.2 something fun

figure()

Load = [0
50
100
150
200
250
300
350
400
450
500
550
600
]

Displacement_2 = [0
0
0.05
0.1
0.2
0.2
0.3
0.3
0.4
0.4
0.4
0.5
0.6
] *10
Displacement_1_under = [0
0.1
0.2
0.5
0.8
1.6
2
2.2
2.4
2.8
3.3
3.6
4.6
]*10
Displacement_1_over = [0
0
0.2
0.6
0.7
1.4
1.8
2.2
2.6
2.9
3.2
3.6
4.2
]*10
Displacement_0 = [0
0.8
1.2
2.1
2.7
3
3.1
3.9
4.6
4.6
4.8
5.3
5.7
]*10

plot(Load,Displacement_2,"*R")
hold on
plot(Load,Displacement_1_over,"*G")
plot(Load,Displacement_1_under,"*B")
plot(Load,Displacement_0,"*K")

set_val = 0:10:600
p1 = polyfit(Load,Displacement_2,1)
p2 = polyfit(Load,Displacement_1_over,1)
p3 = polyfit(Load,Displacement_1_under,1)
p4 = polyfit(Load,Displacement_0,1)


y1 = polyval(p1,set_val);
y2 = polyval(p2,set_val);
y3 = polyval(p3,set_val);
y4 = polyval(p4,set_val);

plot(set_val,y1,"R")
plot(set_val,y2,"G")
plot(set_val,y3,"B")
plot(set_val,y4,"K")

xlim([0,600])
ylim([-5,60])

title("Static load test of Serial-Paralel Hybrid (S-PH) Manipulator with object along Y axis")
legend("2 arm S-PH Manipulator","1 bottom mounted arm S-PH Manipulator","1 top mounted arm S-PH Manipulator","Serial Robotic Arm")
xlabel("Applied Load (g)")
ylabel("Displacemnt from expected position (mm)")
