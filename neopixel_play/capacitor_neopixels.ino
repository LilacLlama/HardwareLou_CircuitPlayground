// Demo program for testing library and board - flip the switch to turn on/off buzzer

#include <Adafruit_CircuitPlayground.h>
#include <Wire.h>
#include <SPI.h>

// we light one pixel at a time, this is our counter
uint8_t pixeln = 0;

// These defines set the range of pixel color when mapping
// to the sensor value.
#define COLOR_RED_MIN    0  
#define COLOR_GREEN_MIN  0
#define COLOR_BLUE_MIN   0

#define COLOR_RED_MAX    255
#define COLOR_GREEN_MAX  255
#define COLOR_BLUE_MAX   255

#define PIXEL_MIN   0
#define PIXEL_MAX   10

void setup() {
  //while (!Serial);
  Serial.begin(9600);
  Serial.println("Circuit Playground test!");

  CircuitPlayground.begin();
}

int red = 100;
int green = 50;
int blue = 25;
int pixels = 10;

#define RED_UP      1  
#define BLUE_UP     0
#define GREEN_UP    2

#define RED_DOWN    12   
#define BLUE_DOWN   6
#define GREEN_DOWN  9 

#define PIXEL_UP    3  
#define PIXEL_DOWN  10

// Change these on ungrounded battery vs. wired to data 
#define THRESHOLD_HIGH 15
#define THRESHOLD 10
#define THRESHOLD_LOW 5

void loop() {
  if (!CircuitPlayground.slideSwitch()) {
    CircuitPlayground.clearPixels();
    return;
  }

  if(CircuitPlayground.readCap(PIXEL_UP) > THRESHOLD){
    pixels = pixels + 1;
  } else if(CircuitPlayground.readCap(PIXEL_DOWN) > THRESHOLD){
    pixels = pixels - 1;
  }

  pixels = constrain(pixels, PIXEL_MIN, PIXEL_MAX);


  // constrain red/green by their min or max...
  if(CircuitPlayground.readCap(RED_UP) > THRESHOLD){
    red = red + 25;
  } else if(CircuitPlayground.readCap(RED_DOWN) > THRESHOLD){
    red = red - 25;
  }
  

  if(CircuitPlayground.readCap(BLUE_UP) > THRESHOLD){
    blue = blue + 25;
  } else if(CircuitPlayground.readCap(BLUE_DOWN) > THRESHOLD){
    blue = blue - 25;
  }

  if(CircuitPlayground.readCap(GREEN_UP) > THRESHOLD){
    green = green + 25;
  } else if(CircuitPlayground.readCap(GREEN_DOWN) > THRESHOLD){
    green = green - 25;
  }

  red = constrain(red, COLOR_RED_MIN, COLOR_RED_MAX);
  blue = constrain(blue, COLOR_BLUE_MIN, COLOR_BLUE_MAX);
  green = constrain(green, COLOR_GREEN_MIN, COLOR_GREEN_MAX);

  CircuitPlayground.clearPixels();
  for(int i = 0; i < pixels; i++){
    CircuitPlayground.setPixelColor(i, red,   green,   blue);
  }

  delay(100);
 
 
}
