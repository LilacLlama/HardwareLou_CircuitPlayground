// Demo program for testing library and board - flip the switch to turn on/off buzzer

#include <Adafruit_CircuitPlayground.h>
#include <Wire.h>
#include <SPI.h>


const int speaker = 5;       // The CP microcontroller pin for the speaker
const int leftButton = 4;    // The CP microcontroller pin for the left button
const int rightButton = 19;  // The CP microcontroller pin for the right button
 

void setup() {
  //while (!Serial);
  Serial.begin(9600);
  Serial.println("Circuit Playground test!");

  pinMode(speaker, OUTPUT);     // We will write out to the speaker
  pinMode(leftButton, INPUT);   // We'll read in from the buttons
  pinMode(rightButton,INPUT);
  
  CircuitPlayground.begin();
}

#define KEY_1 12
#define KEY_2 6
#define KEY_3 9
#define KEY_4 10
#define KEY_5 3
#define KEY_6 2
#define KEY_7 0
#define KEY_8 1


#define THRESHOLD_ON_BATTERY 15
#define THRESHOLD_ON_DATA 50

// Change this based on whether you're wired to computer
// or just on a battery pack!
int cap_threshold = THRESHOLD_ON_BATTERY;
//int cap_threshold = THRESHOLD_ON_DATA;

void loop() {

  if (CircuitPlayground.slideSwitch()) {
    CircuitPlayground.clearPixels();
    return;
  }

  CircuitPlayground.clearPixels();
  
  if(CircuitPlayground.readCap(KEY_1) > cap_threshold){
      CircuitPlayground.setPixelColor(5, 255, 0,   0);
      CircuitPlayground.setPixelColor(6, 255, 0,   0);
      makeTone(speaker,352,100);
  }else if(CircuitPlayground.readCap(KEY_2) > cap_threshold){
      CircuitPlayground.setPixelColor(6, 200, 128,   0);
      CircuitPlayground.setPixelColor(7, 200, 128,   0);
      makeTone(speaker,395,100);
  }else if(CircuitPlayground.readCap(KEY_3) > cap_threshold){
      CircuitPlayground.setPixelColor(7, 100, 180,   0);
      CircuitPlayground.setPixelColor(8, 100, 180,   0);
      makeTone(speaker,418,100);
  }else if(CircuitPlayground.readCap(KEY_4) > cap_threshold - 2){
      CircuitPlayground.setPixelColor(8, 0, 255,   0);
      CircuitPlayground.setPixelColor(9, 0, 255,   0);
      makeTone(speaker,469,100);
  }else if(CircuitPlayground.readCap(KEY_5) > cap_threshold){
      CircuitPlayground.setPixelColor(0, 0, 180,   128);
      CircuitPlayground.setPixelColor(1, 0, 180,   128);
      makeTone(speaker,527,100);
  }else if(CircuitPlayground.readCap(KEY_6) > cap_threshold){
      CircuitPlayground.setPixelColor(1, 0, 60, 200);
      CircuitPlayground.setPixelColor(2, 0, 60, 200);
      makeTone(speaker,558,100);
  }else if(CircuitPlayground.readCap(KEY_7) > cap_threshold){
      CircuitPlayground.setPixelColor(2, 0, 0,   255);
      CircuitPlayground.setPixelColor(3, 0, 0,   255);
      makeTone(speaker,627,100);
  }else if(CircuitPlayground.readCap(KEY_8) > cap_threshold){
      CircuitPlayground.setPixelColor(3, 150, 0,   180);
      CircuitPlayground.setPixelColor(4, 150, 0,   180);
      makeTone(speaker,704,100);
  }
 
}

// the sound producing function (a brute force way to do it)
void makeTone (unsigned char speakerPin, int frequencyInHertz, long timeInMilliseconds) {
  int x;   
  long delayAmount = (long)(1000000/frequencyInHertz);
  long loopTime = (long)((timeInMilliseconds*1000)/(delayAmount*2));
  for (x=0; x<loopTime; x++) {        // the wave will be symetrical (same time high & low)
     digitalWrite(speakerPin,HIGH);   // Set the pin high
     delayMicroseconds(delayAmount);  // and make the tall part of the wave
     digitalWrite(speakerPin,LOW);    // switch the pin back to low
     delayMicroseconds(delayAmount);  // and make the bottom part of the wave
  }  
}
