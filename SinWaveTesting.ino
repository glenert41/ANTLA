#include <Servo.h>
#include <math.h>

Servo servo0;
Servo servo1;
Servo servo2;


float myPi = 3.1415926535897932384626433832795;

void setup() {
  servo0.attach(11);
  servo1.attach(10);
  servo2.attach(9);
  Serial.begin(9600);
}


float myStep = .1;
float input0 = 0;
float output0;


float input1 = myPi/2;
float output1;

float input2 = myPi;
float output2;

float input3 = (3 * myPi) / 2;
float output3; 

float input4 = (2 * myPi);
float output4;

void loop() {



output0 = cosineMap(input0 + myStep);
output1 = cosineMap(input1 + myStep);
output2 = cosineMap(input2 + myStep);
output3 = cosineMap(input3 + myStep);
output4 = cosineMap(input4 + myStep);

input0 = input0 + myStep;
input1 = input1 + myStep;
input2 = input2 + myStep;
input3 = input3 + myStep;
input4 = input4 + myStep;

//Serial.print("preMap: ");
//Serial.println(output0);
//output0 = map(output0,-1,1,0,180);
//output0 = (output0 + 1)/(1+1) * (180-0) + 0;
output0 = (output0 + 1)/2 * 180;
output1 = (output1 + 1)/2 * 180;
output2 = (output2 + 1)/2 * 180;
output3 = (output3 + 1)/2 * 180;
output4 = (output4 + 1)/2 * 180;

servo0.write(output0);
servo1.write(output1);
servo2.write(output2);
//servo3.write(output3);
//servo4.write(output4);

//Serial.print("postMap: ");
Serial.print(output0);
Serial.print(",");
Serial.print(output1);
Serial.print(",");
Serial.print(output2);
Serial.print(",");
Serial.print(output3);
Serial.print(",");
Serial.println(output4);


}

float cosineMap(float pos){
      float mappedPos = cos(pos);
      return mappedPos;
}
