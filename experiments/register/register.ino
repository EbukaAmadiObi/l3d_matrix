

//Pin connected to ST_CP of 74HC595
int latchPin = 9;
//Pin connected to SH_CP of 74HC595
int clockPin = 10;
////Pin connected to DS of 74HC595
int dataPin = 11;

void setup() {
  //set pins to output because they are addressed in the main loop
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
}

byte data;

void loop() {
  //data to be shifted out, each bit represents state of output puns
  data = 0b11111111;
  //ground latchPin and hold low for as long as you are transmitting
  digitalWrite(latchPin, LOW);
  //transmit data
  shiftOut(dataPin, clockPin, MSBFIRST, data);
  //return the latch pin high to signal chip that it
  //no longer needs to listen for information
  digitalWrite(latchPin, HIGH);
  delay(1000);

}