/* 
 * receiver.ino
 * Program for the reciever to decipher the binary and interpret it into
 * characters and display that to a lcd screen.
 *
 * Sahibjot Singh
 * Septemeber 2023
 */


#include <rgb_lcd.h>

const byte inputPin1 = A2;
const byte inputPin2 = A3;
String binaryMessage = "";
int currentToken;
int pastToken;
rgb_lcd lcd;


// Executes once, at the start
void setup() {
  lcd.begin(16, 2);
  lcd.setRGB(255, 0, 0);

  Serial.begin(9600);
}


// Loops infinitely
void loop() {
  int value1 = analogRead(inputPin1);
  int value2 = analogRead(inputPin2);
  currentToken = constrain(value1 - value2, -1000, 1000);

  if (currentToken != pastToken) {
    if (currentToken == 1000) binaryMessage += "1";
    else if (currentToken == -1000) binaryMessage += "0";
  }

  lcd.clear();
  for (size_t i = 0; i < binaryMessage.length() / 8; ++i) {
    String strByte = binaryMessage.substring(i, i + 8);
    char* endptr;
    char ch = static_cast<char>(strtol(strByte.c_str(), &endptr, 2));
    lcd.print(ch);
  }

  pastToken = currentToken;

  delay(10);
}
