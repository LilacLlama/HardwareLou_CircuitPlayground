// Demo program for testing library and board - flip the switch to turn on/off the snap sensor

#include <Adafruit_CircuitPlayground.h>
#include <Wire.h>
#include <SPI.h>

#define COLOR_MAX 6

void setup() {
  //while (!Serial);
  Serial.begin(9600);
  Serial.println("Circuit playground snap sensor!");

  CircuitPlayground.begin();
}

bool snapped = false;

int colorShift = 0;

void loop() {

  // Turn off the neopixels and just skip the rest
  // if the slide is switched negative
  if (!CircuitPlayground.slideSwitch()) {
    CircuitPlayground.clearPixels();
    return;
  }

  // otherwise, if you hear a loud noise
  if(CircuitPlayground.soundSensor() > 1000){
    Serial.println("YOU SNAPPED!");
    // flip the snap boolean!
    snapped = !snapped;
    if(snapped){
      Serial.println("SNAP ON!");
      // then paint the neopixels (but shift the colors for next time!)
      paintPixels(colorShift++);
      // Make sure you reset the color shift tho, once you hit the max.
      if(colorShift >= COLOR_MAX){
        colorShift = 0;
      }
      
    }else{ // If it's snap off time, turn it off!
      Serial.println("SNAP OFF!");
      CircuitPlayground.clearPixels();
    }

    // wait a bit, so that we don't flip too soon.
    delay(250);
    
  }
}

void paintPixels(int color){
  switch(color){
    case 0: // RAINBOW
      CircuitPlayground.setPixelColor(0, 255,   0,   0);
      CircuitPlayground.setPixelColor(1, 180,   60,   0);
      CircuitPlayground.setPixelColor(2, 60,   180,   0);
      CircuitPlayground.setPixelColor(3, 0,   255,   0);
      CircuitPlayground.setPixelColor(4, 0,   180,   60);
      CircuitPlayground.setPixelColor(5, 0,   60,   180);
      CircuitPlayground.setPixelColor(6, 0,   0,   255);
      CircuitPlayground.setPixelColor(7, 60,   0,   180);
      CircuitPlayground.setPixelColor(8, 180,   0,   60);
      CircuitPlayground.setPixelColor(9, 255,   0,   0);
      
    return;
    
    case 1: // ALL RED!
      for(int i = 0; i < 10; i++){
        CircuitPlayground.setPixelColor(i, 255,   0,   0);
      }
    return;

    case 2: // ALL BLUE!
      for(int i = 0; i < 10; i++){
        CircuitPlayground.setPixelColor(i, 0,   255,   0);
      }
    return;

    case 3: // ALL GREEN!
      for(int i = 0; i < 10; i++){
        CircuitPlayground.setPixelColor(i, 0,   0,   255);
      }
    return;

    case 4: // BI COLOR - YELLOW & TEAL
      for(int i = 0; i < 10; i++){
        if(i < 5){
          CircuitPlayground.setPixelColor(i, 0xFFFF00);
        }else{
          CircuitPlayground.setPixelColor(i, 0x008080);
        }
      }
    return;

    case 5: // BI COLOR - PURPLE & MAGENTA
      for(int i = 0; i < 10; i++){
        if(i%2 == 0){
          CircuitPlayground.setPixelColor(i, 0x440080);
        }else{
          CircuitPlayground.setPixelColor(i, 0xff00ff);
        }
      }
    return;

    case 6: // MORE BICOLOR - GREEN & ORANGE
      for(int i = 0; i < 10; i++){
        if(i%3 == 0){
          CircuitPlayground.setPixelColor(i, 0x20bb2a);
        }else{
          CircuitPlayground.setPixelColor(i, 0xfb7126);
        }
      }
    return;
  }

}
