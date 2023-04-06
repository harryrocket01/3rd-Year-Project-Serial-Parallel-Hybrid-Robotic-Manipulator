%Array of given positions
Positions = [[120 0 0 0];[140 0 0 0];[120 0 0 0];[120 0 50 0];[0 0 0 0]]

%times and intervels
t_f = 5
intervel=100
X_CART = [];
Y_CART = [];
Z_CART = [];

%Creates trajectories through the points
for i = 1:length(Positions)-1
    
    [X,Y,Z,Gamma] = traj_move(Positions(i,:),Positions(i+1,:),t_f,intervel);
    
    X_CART=[X_CART X];
    Y_CART=[Y_CART Y];
    Z_CART=[Z_CART Z];
     
end

%Plot
scatter3(X_CART,Y_CART,Z_CART)


%To caclulate trajectory between two position vectors
function [X,Y,Z,Gamma] = traj_move(Start,End,t_f,intervel)
    X =traj(Start(1),End(1),t_f,intervel);
    Y =traj(Start(2),End(2),t_f,intervel);
    Z =traj(Start(3),End(3),t_f,intervel);
    Gamma =traj(Start(4),End(4),t_f,intervel);
end


%Calculate trajectory of single DOF
function C = traj(u_0,u_f,t_f,intervel)

a_0= u_0;
a_3= (10/(t_f^3))*(u_f-u_0);
a_4= (-15/(t_f^4))*(u_f-u_0);
a_5= (6/(t_f^5))*(u_f-u_0);


t = 0:t_f/intervel:t_f;

C = a_0 + a_3.*(t).^3 + a_4.*(t).^4 + a_5.*(t).^5;

end