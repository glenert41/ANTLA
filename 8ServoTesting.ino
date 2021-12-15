#include <Servo.h>

Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;



//change step to change speed
//change desiredHigh/Low to change region of rotation



float myPi = 3.1415926535897932384626433832795;

//step for servo rotation per loop
//change step to change speed
//.5 is very fast
// .1 is standard

float myStep = .1;

//inputs and outputs for angles; each input is a phase shift of pi/2 apart (one crest/trough of a normal frequency wave)
float input0 = 0;
float output0;

float input1= myPi/2;
float output1;

float input2 = myPi;
float output2;

float input3 = (3 * myPi)/2;
float output3;



void setup() {  

  servo0.attach(6);
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11);


  servo0.write(0);
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);

  delay(500);
  
  Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:
  //find the output of the Cosine
  output0 = cosineMap(input0 + myStep);
  output1 = cosineMap(input1 + myStep);
  output2 = cosineMap(input2 + myStep);
  output3 = cosineMap(input3 + myStep);

  input0 = input0 + myStep;
  input1 = input1 + myStep;
  input2 = input2 + myStep;
  input3 = input3 + myStep;


  float desiredLow = 45;
  float desiredHigh = 135;
  output0 =  myMapValues(output0, -1, 1, desiredLow,desiredHigh);
  output1 =  myMapValues(output1, -1, 1, desiredLow,desiredHigh);
  output2 =  myMapValues(output2, -1, 1, desiredLow,desiredHigh);
  output3 =  myMapValues(output3, -1, 1, desiredLow,desiredHigh);
  


  int intOutput0 = output0;
  int intOutput1 = output1;
  int intOutput2 = output2;
  int intOutput3 = output3;

  //servo0.write(intOutput0);
  //servo1.write(intOutput1);
  //servo2.write(intOutput2);
  //servo3.write(intOutput3);

  servo0.write(0);
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  
Serial.println(intOutput0);
Serial.print(",");
Serial.print(intOutput1);
Serial.print(",");
Serial.print(intOutput2);
Serial.print(",");
Serial.println(intOutput3);

  delay(25);

}

float cosineMap(float pos){
      float mappedPos = cos(pos);
      return mappedPos;
}

float myMapValues(float variable, float oldLow, float oldHigh, float newLow, float newHigh){

 variable = (variable - oldLow) / (oldHigh - oldLow) * (newHigh - newLow) + newLow;
 return variable;

  
  
}
