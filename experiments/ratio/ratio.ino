/*
This sketch reads a voltage input from a potentiometer and uses the value to control
the ratio of two primary LED colours
*/
float ratio;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  ratio = analogRead(A0);
  Serial.println(ratio);
  
  ratio /= 1023;

  //blue
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(15 * ratio);
  
  //red
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  delay(15 * (1 - ratio));
}
