
clear all 
close all


%Set Values of link lengths(mm)
L1 = 0;
L2 = 120;
L3 = 120;
L4 = 110;

Mid_Joint = 75;

L_2_1 = Mid_Joint;
L_2_2 = 0;
L_2_3 = 60;
L_2_4 = 120;

%Desired Angles of each joint
Theta1 = 0;
Theta2 = 22;
Theta3 = 13 ;
Theta4 = 18;

Theta5 = 90;
Theta6 = 120;
Theta7 = 60;
Theta8 = Theta6;
Theta9 = -Theta7;

%%%-----------Main Arm -------
%Creates DH Tables from provided values
a_i =[0;0;L1;L2;L3];
alpha_i =[0;0;-90;180;0];
d_i = [0;0;0;0;0];
Theta_i = [0;Theta1;Theta2;Theta3;Theta4];

DHTable = horzcat(a_i,alpha_i,d_i,Theta_i);

%Vector for end effector
End_effector = [L4; 0;0; 1];


%Creates transformation matrixs  
T_01 = Ken_Transform(1,DHTable);
T_12 = Ken_Transform(2,DHTable);
T_23 = Ken_Transform(3,DHTable);
T_34 = Ken_Transform(4,DHTable);

%Creates single transform matrix T_03
T_03 = T_01*T_12*T_23*T_34;

%Finds cart position of end effector
P_0 = T_03*End_effector
Gamma = -Theta2+Theta3+Theta4;

%Finds the cart position for the other joins
P_1 = T_01*[L1; 0; 0; 1];
P_2 = T_01*T_12*[L2; 0; 0; 1];
P_3 = T_01*T_12*T_23*[L3; 0; 0; 1];




%%%-----------SubArm -------

%Solve arm joint 1 

a_i_extra =     [a_i      ;L_2_1    ;L_2_2    ;L_2_3];
alpha_i_extra = [alpha_i  ;Theta5       ;0      ;180];
d_i_extra =     [d_i;0        ;0        ;0];
Theta_i_extra = [Theta_i       ;0   ;Theta6   ;Theta7];



DHTable_Extra = horzcat(a_i_extra,alpha_i_extra,d_i_extra,Theta_i_extra)

TExtra_01 = Ken_Transform(1,DHTable_Extra);
TExtra_12 = Ken_Transform(2,DHTable_Extra);
TExtra_23 = Ken_Transform(3,DHTable_Extra);
TExtra_34 = Ken_Transform(4,DHTable_Extra);
TExtra_45 = Ken_Transform(5,DHTable_Extra);
TExtra_56 = Ken_Transform(6,DHTable_Extra);
TExtra_67 = Ken_Transform(7,DHTable_Extra);

P_0Extra = TExtra_01*TExtra_12*TExtra_23*TExtra_34*TExtra_45*TExtra_56*TExtra_67*[L_2_4;0;0;1];

P_Extra1 = TExtra_01*[a_i_extra(3);0;0;1];
P_Extra2 = TExtra_01*TExtra_12*[a_i_extra(4);0;0;1];
P_Extra3 = TExtra_01*TExtra_12*TExtra_23*[a_i_extra(5);0;0;1];
P_Extra4 = TExtra_01*TExtra_12*TExtra_23*TExtra_34*[a_i_extra(6);0;0;1];
P_Extra5 = TExtra_01*TExtra_12*TExtra_23*TExtra_34*TExtra_45*[a_i_extra(7);0;0;1];
P_Extra6 = TExtra_01*TExtra_12*TExtra_23*TExtra_34*TExtra_45*TExtra_56*[a_i_extra(8);0;0;1];

Loc = [P_Extra1 P_Extra2 P_Extra3 P_Extra4 P_Extra5 P_Extra6 P_0Extra]







%Solve arm joint 2 

a_i_extra =     [a_i      ;L_2_1    ;L_2_2    ;L_2_3];
alpha_i_extra = [alpha_i  ;180+Theta5       ;0      ;180];
d_i_extra =     [d_i;0        ;0        ;0];
Theta_i_extra = [Theta_i       ;0   ;Theta6   ;Theta7];



DHTable_Extra2 = horzcat(a_i_extra,alpha_i_extra,d_i_extra,Theta_i_extra)

TA2_01 = Ken_Transform(1,DHTable_Extra2);
TA2_12 = Ken_Transform(2,DHTable_Extra2);
TA2_23 = Ken_Transform(3,DHTable_Extra2);
TA2_34 = Ken_Transform(4,DHTable_Extra2);
TA2_45 = Ken_Transform(5,DHTable_Extra2);
TA2_56 = Ken_Transform(6,DHTable_Extra2);
TA2_67 = Ken_Transform(7,DHTable_Extra2);

P_TA2_0 = TA2_01*TA2_12*TA2_23*TA2_34*TA2_45*TA2_56*TA2_67*[L_2_4;0;0;1];

P_TA2_1 = TA2_01*[a_i_extra(3);0;0;1];
P_TA2_2 = TA2_01*TA2_12*[a_i_extra(4);0;0;1];
P_TA2_3 = TA2_01*TA2_12*TA2_23*[a_i_extra(5);0;0;1];
P_TA2_4 = TA2_01*TA2_12*TA2_23*TA2_34*[a_i_extra(6);0;0;1];
P_TA2_5 = TA2_01*TA2_12*TA2_23*TA2_34*TA2_45*[a_i_extra(7);0;0;1];
P_TA2_6 = TA2_01*TA2_12*TA2_23*TA2_34*TA2_45*TA2_56*[a_i_extra(8);0;0;1];

Loc_A2 = [P_TA2_1 P_TA2_2 P_TA2_3 P_TA2_4 P_TA2_5 P_TA2_6 P_TA2_0]




%Converts all the points in to a 3d Matirx
figure()
X = [0; P_1(1) ; P_2(1); P_3(1);  P_0(1)];
Y = [0; P_1(2) ; P_2(2); P_3(2);  P_0(2)];
Z = [0; P_1(3) ; P_2(3);P_3(3);  P_0(3)];


X_2 = Loc(1,:)
Y_2 = Loc(2,:)
Z_2 = Loc(3,:)

X_3 = Loc_A2(1,:)
Y_3 = Loc_A2(2,:)
Z_3 = Loc_A2(3,:)

%Prints Cart position of end effector
P_0
Gamma
%Creates 3D plot of robot arm
plot3 (X,Y,Z,'-o','LineWidth',8,'MarkerSize', 5,'MarkerFaceColor','k','MarkerEdgeColor','k')
hold on
plot3 (P_0(1),P_0(2),P_0(3),'o','MarkerSize', 9,'MarkerFaceColor','r','MarkerEdgeColor','r')

plot3 (X_2,Y_2,Z_2,'-o','LineWidth',8,'MarkerSize', 7,'MarkerFaceColor','b','MarkerEdgeColor','b')
plot3 (X_3,Y_3,Z_3,'-o','LineWidth',8,'MarkerSize', 7,'MarkerFaceColor','b','MarkerEdgeColor','b')

title(["3D Plot of robotics arm mathmatical postition "," [X, Y, Z] = [120, 0, 0]"])
grid on
Lim_val = (L1+L2+L3+L4)*1;
ylim([-Lim_val;Lim_val])
xlim([-Lim_val;Lim_val])
zlim([-Lim_val;0])
xlabel("X Distance (mm)")
ylabel("Y Distance (mm)")
zlabel("Z Distance (mm)")
set(gca, 'ZDir','reverse')
legend("Joints","End Effector")

%Function that calculates transformation matrix from a given dh table and
%joint index


function T = Ken_Transform(i,DHTable)
    i = i+1;

    %takes correct values from provided DH tables
    theta_i = DHTable(i,4);
    alpha = DHTable(i,2);
    a_link = DHTable(i,1);
    d_i = DHTable(i,3);
    
    %creates and returns the correct transformation matrix using the
    %general formula
    T = [cosd(theta_i) -sind(theta_i) 0 a_link;
        cosd(alpha)*sind(theta_i) cosd(alpha)*cosd(theta_i) -sind(alpha) -sind(alpha)*d_i;
         sind(alpha)*sind(theta_i) sind(alpha)*cosd(theta_i) cosd(alpha) cosd(alpha)*d_i;
        0 0 0 1];
end
