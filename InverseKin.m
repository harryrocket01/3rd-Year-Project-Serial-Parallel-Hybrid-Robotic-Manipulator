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


%Last position
Endeffector =  [    
  338.4304
         0
  -46.5171]

Gamma=    9;

Theta = InvKenCalcMain(Endeffector(1),Endeffector(2),Endeffector(3),Gamma,L1,L2,L3,L4)

function C = InvKenCalcMain(X,Y,Z,Gamma,L1,L2,L3,L4)

     %Caclulates Theta 1
    Theta1 = atan2d(Y,X)

    X_val=X-(cosd(Theta1)*L4*cosd(Gamma));

    Y_val=Y-(sind(Theta1)*L4*cosd(Gamma));

    Z_val=Z-(L4*sind(Gamma));
    

    %Caclulates Theta 2
    Beta = atan2d(Z_val, sqrt(Y_val^2+X_val^2));

    Phi = acosd((L2^2+Z_val^2+Y_val^2+X_val^2-L3^2)/(2*L2*sqrt(Z_val^2+Y_val^2+X_val^2)));

    Theta2 = Phi-Beta;

    %Caclulates Theta 3
    cTheta3= (X_val^2+Y_val^2+Z_val^2-L2^2-L3^2)/(2*L2*L3);
    sTheta3= sqrt(1-cTheta3^2);

    Theta3 = atan2d(sTheta3,cTheta3);
    

    Theta4 = Gamma-(-Theta2)-Theta3;

    C=[Theta1,Theta2,Theta3,Theta4];
end


function C = InvKenCalcSecondary(X1,Y1,Z1,X2,Y2,Z2,Gamma,Theta1,MidPoint,L1,L2)

    %Caclulates Theta 5
    Theta5 = atan2d(Y,X)
    
    PRJ = [X1 - MidPoint*cosd(Theta1)*cosd(Gamma) ;Y1 - MidPoint*sind(Theta1)*cosd(Gamma)  ;Z1 - MidPoint*sind(Gamma)  ]
    PR = [X2;Y2;Z2]-PRJ


    PSER = PR*[cosd(Theta1) -sind(Theta1) 0; sin(Theta1) cos(Theta1) 0; 0 0 1]*[cosd(Gamma) 0 sind(Gamma); 0 1 0 -sind(Gamma) 0 cosd(Gamma)]
    Z_val=PSER(3)
    X_val=PSER(1)
    Y_val=PSER(2)
    %Caclulates Theta 6
    Beta2 = atan2d(Z_val, sqrt(Y_val^2+X_val^2));

    Phi2 = acosd((L1^2+Z_val^2+Y_val^2+X_val^2-L2^2)/(2*L1*sqrt(Z_val^2+Y_val^2+X_val^2)));

    Theta6 = Phi-Beta;

    %Caclulates Theta 7
    cTheta7= (X_val^2+Y_val^2+Z_val^2-L1^2-L2^2)/(2*L1*L2);
    sTheta7= sqrt(1-cTheta7^2);

    Theta7 = atan2d(sTheta7,cTheta7);
    


    C=[Theta5,Theta6,Theta7];
end


