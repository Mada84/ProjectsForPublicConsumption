#define LED_PIN 11 //Setup pin11 as output
#define POTENTIOMETER_PIN A0 //setup as analog input
void setup()
{
  pinMode(LED_PIN, OUTPUT); //Select LED as my output
}
void loop()
{
  int potentiometerVal = analogRead(POTENTIOMETER_PIN); //getting poteniometer value
  int bright = potentiometerVal / 4; //changing value for brightness
  analogWrite(LED_PIN, bright); //outputting various brightnesses to LED
}