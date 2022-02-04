/* binarymacro.ino
   Single button macro for typing ones and zeros
   Single click types 0 and double click for 1

   Author: Mingye Chen 2022-02-04
*/
#include <Keyboard.h>

//#define TESTING
#define TIMEOUT 300
#define COOLDOWN 70

const int button = 14;
bool currentState = LOW;
bool firstclick = true;
long starttime;

void setup() {
  pinMode(14, INPUT_PULLUP); // sets pin 14 to input & pulls it high w/ internal resistor
#ifdef TESTING
  Serial.begin(115200);       // begin serial comms for debugging
#endif
}


void loop() {
  // button press
  if (digitalRead(button) == HIGH && currentState == LOW) {
    // save current time if this is the first click
    if (firstclick == true) {
      starttime = millis();
      firstclick = false;
    }
    // if this is the second click, check if it is within the timeout time span
    else if (millis() - starttime < TIMEOUT) {
#ifdef TESTING
      Serial.println("1");
#else
      Keyboard.begin();
      Keyboard.print("1");
      Keyboard.end();
#endif
      firstclick = true;
    }
#ifdef TESTING
    Serial.println("l-h");
#endif
    currentState = HIGH;
    delay(COOLDOWN);

  }
  // button release
  if (digitalRead(button) == LOW && currentState == HIGH) {
    currentState = LOW;
#ifdef TESTING
    Serial.println("h-1");
#endif
  }
  // check if button timed out, if so then type zero
  if (!firstclick && millis() - starttime > TIMEOUT) {

#ifdef TESTING
    Serial.println("0");
#else
    Keyboard.begin();
    Keyboard.print("0");
    Keyboard.end();
#endif
    firstclick = true;
  }

  //Keyboard.end();                 //stops keybord
}
