within ;
model CoupledClutches "Drive train with 3 dynamically coupled clutches"
  extends Modelica.Icons.Example;
  parameter Modelica.Units.SI.Frequency f=0.2
    "Frequency of sine function to invoke clutch1";
  parameter Modelica.Units.SI.Time T2=0.4 "Time when clutch2 is invoked";
  parameter Modelica.Units.SI.Time T3=0.9 "Time when clutch3 is invoked";

  Modelica.Mechanics.Rotational.Components.Inertia J1(
    J=1,
    phi(fixed=true, start=0),
    w(start=10, fixed=true))
    annotation (Placement(transformation(extent={{-70,-70},{-50,-50}})));
  Modelica.Mechanics.Rotational.Sources.Torque torque(useSupport=true)
    annotation (Placement(transformation(extent={{-100,-70},{-80,-50}})));
  Modelica.Mechanics.Rotational.Components.Clutch clutch1(peak=1.1, fn_max=20)
    annotation (Placement(transformation(extent={{-40,-70},{-20,-50}})));
  Modelica.Blocks.Sources.Step step1(startTime=T2) annotation (Placement(
        transformation(
        origin={25,-25},
        extent={{-5,-5},{15,15}},
        rotation=270)));
  Modelica.Mechanics.Rotational.Components.Inertia J2(
    J=1,
    phi(fixed=true, start=0),
    w(fixed=true, start=0))
    annotation (Placement(transformation(extent={{-10,-70},{10,-50}})));
  Modelica.Mechanics.Rotational.Components.Clutch clutch2(peak=1.1, fn_max=20)
    annotation (Placement(transformation(extent={{20,-70},{40,-50}})));
  Modelica.Mechanics.Rotational.Components.Inertia J3(
    J=1,
    phi(fixed=true, start=0),
    w(fixed=true, start=0))
    annotation (Placement(transformation(extent={{50,-70},{70,-50}})));
  Modelica.Mechanics.Rotational.Components.Clutch clutch3(peak=1.1, fn_max=20)
    annotation (Placement(transformation(extent={{80,-70},{100,-50}})));
  Modelica.Mechanics.Rotational.Components.Inertia J4(
    J=1,
    phi(fixed=true, start=0),
    w(fixed=true, start=0))
    annotation (Placement(transformation(extent={{110,-70},{130,-50}})));
  Modelica.Blocks.Sources.Sine sin2(
    amplitude=1,
    f=f,
    phase=1.570796326794897) annotation (Placement(transformation(
        origin={-35,-25},
        extent={{-5,-5},{15,15}},
        rotation=270)));
  Modelica.Mechanics.Rotational.Components.Fixed fixed
    annotation (Placement(transformation(extent={{-100,-90},{-80,-70}})));
  Modelica.Mechanics.Rotational.Sensors.SpeedSensor speedSensor1
    annotation (Placement(transformation(extent={{110,50},{130,70}})));
  Modelica.Blocks.Interfaces.RealOutput J1_w
    "Absolute angular velocity of flange as output signal"
    annotation (Placement(transformation(extent={{140,50},{160,70}})));
  Modelica.Mechanics.Rotational.Sensors.SpeedSensor speedSensor2
    annotation (Placement(transformation(extent={{110,10},{130,30}})));
  Modelica.Blocks.Interfaces.RealOutput J2_w
    "Absolute angular velocity of flange as output signal"
    annotation (Placement(transformation(extent={{140,10},{160,30}})));
  Modelica.Mechanics.Rotational.Sensors.SpeedSensor speedSensor3
    annotation (Placement(transformation(extent={{110,-30},{130,-10}})));
  Modelica.Blocks.Interfaces.RealOutput J3_w
    "Absolute angular velocity of flange as output signal"
    annotation (Placement(transformation(extent={{140,-30},{160,-10}})));
  Modelica.Mechanics.Rotational.Sensors.SpeedSensor speedSensor4
    annotation (Placement(transformation(extent={{110,-50},{130,-30}})));
  Modelica.Blocks.Interfaces.RealOutput J4_w
    "Absolute angular velocity of flange as output signal"
    annotation (Placement(transformation(extent={{140,-70},{160,-50}})));
  Modelica.Blocks.Sources.Sine sin1(amplitude=10, f=5) annotation (
      Placement(transformation(extent={{-130,-70},{-110,-50}})));
  Modelica.Blocks.Interfaces.RealInput step2
    "Normalized force signal 0..1 (normal force = fn_max*f_normalized; clutch is engaged if > 0)"
    annotation (Placement(transformation(extent={{-180,-20},{-140,20}})));
equation
  connect(torque.flange, J1.flange_a)
    annotation (Line(points={{-80,-60},{-70,-60}}));
  connect(J1.flange_b, clutch1.flange_a)
    annotation (Line(points={{-50,-60},{-40,-60}}));
  connect(clutch1.flange_b, J2.flange_a)
    annotation (Line(points={{-20,-60},{-10,-60}}));
  connect(J2.flange_b, clutch2.flange_a)
    annotation (Line(points={{10,-60},{20,-60}}));
  connect(clutch2.flange_b, J3.flange_a)
    annotation (Line(points={{40,-60},{50,-60}}));
  connect(J3.flange_b, clutch3.flange_a)
    annotation (Line(points={{70,-60},{80,-60}}));
  connect(clutch3.flange_b, J4.flange_a)
    annotation (Line(points={{100,-60},{110,-60}}));
  connect(sin2.y, clutch1.f_normalized) annotation (Line(points={{-30,-41},{-30,
          -49}},             color={0,0,127}));
  connect(step1.y, clutch2.f_normalized) annotation (Line(points={{30,-41},{30,
          -49}},                   color={0,0,127}));
  connect(fixed.flange, torque.support) annotation (Line(points={{-90,-80},{-90,
          -70}}));
  connect(speedSensor1.flange, clutch1.flange_a) annotation (Line(points={{110,60},
          {-50,60},{-50,-60},{-40,-60}},     color={0,0,0}));
  connect(speedSensor1.w, J1_w)
    annotation (Line(points={{131,60},{150,60}}, color={0,0,127}));
  connect(speedSensor2.flange, clutch2.flange_a) annotation (Line(points={{110,20},
          {14,20},{14,-60},{20,-60}},     color={0,0,0}));
  connect(speedSensor2.w, J2_w)
    annotation (Line(points={{131,20},{150,20}}, color={0,0,127}));
  connect(speedSensor3.flange, J3.flange_a)
    annotation (Line(points={{110,-20},{46,-20},{46,-60},{50,-60}},
                                                      color={0,0,0}));
  connect(speedSensor3.w, J3_w)
    annotation (Line(points={{131,-20},{150,-20}}, color={0,0,127}));
  connect(speedSensor4.flange, J4.flange_a) annotation (Line(points={{110,-40},
          {106,-40},{106,-60},{110,-60}}, color={0,0,0}));
  connect(speedSensor4.w, J4_w) annotation (Line(points={{131,-40},{134,-40},{
          134,-60},{150,-60}}, color={0,0,127}));
  connect(sin1.y, torque.tau)
    annotation (Line(points={{-109,-60},{-102,-60}}, color={0,0,127}));
  connect(clutch3.f_normalized, step2)
    annotation (Line(points={{90,-49},{90,0},{-160,0}}, color={0,0,127}));
  annotation (
    Documentation(info="<html>
<p>This example demonstrates how variable structure
drive trains are handled. The drive train consists
of 4 inertias and 3 clutches, where the clutches
are controlled by input signals. The system has
2^3=8 different configurations and 3^3 = 27
different states (every clutch may be in forward
sliding, backward sliding or locked mode when the
relative angular velocity is zero). By invoking the
clutches at different time instances, the switching
of the configurations can be studied.</p>
<p>Simulate the system for 1.2 seconds with the
following initial values:<br>
J1.w = 10.</p>
<p>Plot the following variables:<br>
angular velocities of inertias (J1.w, J2.w, J3.w,
J4.w), frictional torques of clutches (clutchX.tau),
frictional mode of clutches (clutchX.mode) where
mode = -1/0/+1 means backward sliding,
locked, forward sliding.</p>

</html>"),
    __Dymola_Commands(file=
          "modelica://Modelica/Resources/Scripts/Dymola/Mechanics/Rotational/CoupledClutches.mos"
        "Simulate and Plot"),
    experiment(StopTime=1.5, Interval=0.001),
    Diagram(coordinateSystem(preserveAspectRatio=false, extent={{-140,-100},
            {140,100}})),
    uses(Modelica(version="4.0.0")));
end CoupledClutches;
