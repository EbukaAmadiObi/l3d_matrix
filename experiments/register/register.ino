

//Pin connected to ST_CP of 74HC595
int latchPiny = 12;
int latchPinx = 8;
//Pin connected to SH_CP of 74HC595
int clockPin = 11;
////Pin connected to DS of 74HC595
int dataPiny = 13;

int dataPinx = 9;

void setup() {
  //set pins to output because they are addressed in the main loop
  pinMode(latchPiny, OUTPUT);
  pinMode(latchPinx, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPinx, OUTPUT);
  pinMode(dataPiny, OUTPUT);
}

byte x;
byte y;

void loop() {
  //data to be shifted out, each bit represents state of output puns
  light(0,0);
  light(1,0);
  light(2,0);
  light(3,0);
  light(4,0);
  light(5,0);
  light(6,0);
  light(7,0);
  light(7,1);  
  light(7,2);
  light(7,3);
  light(7,4);
  light(7,5);
  light(7,6);
  light(7,7);
  light(6,7);
  light(5,7);
  light(4,7);
  light(3,7);
  light(2,7);
  light(1,7);
  light(0,7);
  light(0,6);
  light(0,5);
  light(0,4);
  light(0,3);
  light(0,2);
  light(0,1);
  light(0,0);
  light(1,1);
  light(2,2);
  light(3,3);
  light(4,4);
  light(5,5);
  light(6,6);
  light(7,7);
  light(6,7);
  light(5,7);
  light(4,7);
  light(3,7);
  light(2,7);
  light(1,7);
  light(0,7);
  light(1,6);
  light(2,5);
  light(3,4);
  light(4,3);
  light(5,2);
  light(6,1);
  light(7,0);
  light(6,0);
  light(5,0);
  light(4,0);
  light(3,0);
  light(2,0);
  light(1,0);
  light(0,0);


}

void push(){
  digitalWrite(latchPiny, LOW);
  //transmit data
  shiftOut(dataPiny, clockPin, LSBFIRST, x);
  shiftOut(dataPiny, clockPin, MSBFIRST, y);

  //return the latch pin high to signal chip that it
  //no longer needs to listen for information
  digitalWrite(latchPiny, HIGH);
  delay(100);
}
void light(int x_c,int y_c){
  switch(x_c){
    case 0:
      x = ~0b10000000;
      break;
    case 1:
      x =~0b01000000;
      break;
    case 2:
      x = ~0b00100000;
      break;
    case 3:
      x = ~0b00010000;
      break;
    case 4:
      x = ~0b00001000;
      break;
    case 5:
      x = ~0b00000100;
      break;
    case 6:
      x = ~0b00000010;
      break;
    case 7:
      x = ~0b00000001;
      break;
  }

  switch(y_c){
    case 0:
      y = 0b10000000;
      break;
    case 1:
      y = 0b01000000;
      break;
    case 2:
      y = 0b00100000;
      break;
    case 3:
      y = 0b00010000;
      break;
    case 4:
      y = 0b00001000;
      break;
    case 5:
      y = 0b00000100;
      break;
    case 6:
      y = 0b00000010;
      break;
    case 7:
      y = 0b00000001;
      break;
  }
  push();
}
