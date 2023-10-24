/*
This sketch cycles through all colours at a specified rate to determine 
*/
int GREEN = 11;
int BLUE = 12;
int RED = 13;
int wait = 256;
int min;
int ratio [3];
void setup() {
  // put your setup code here, to run once:
  pinMode(RED, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(GREEN,OUTPUT);
  Serial.begin(9600);

  
  int rgb [3] = {200,30,0};
  rgb[0] = rgb[0]/1;
  rgb[1] = rgb[1]/40;
  rgb[2] = rgb[2]/1;
  
  int i = 0;

  min = rgb[i];
  while (i<=2){
    if (rgb[i]<min && rgb[i]!=0){
      min = rgb[i];
    }
    i++;
  }
  ratio[0] = rgb[0]/min;
  ratio[1] = rgb[1]/min;
  ratio[2] = rgb[2]/min;
  Serial.println(ratio[0]);
  Serial.println(ratio[1]);
  Serial.println(ratio[2]);
}

void loop() {
  if (ratio[0]>0){
    digitalWrite(GREEN, LOW);  
    digitalWrite(BLUE, LOW);   
    digitalWrite(RED, HIGH);
    //delayMicroseconds(ratio[0]);                    //timing for Red
    delayMicroseconds(200);
  }
  if (ratio[1]>0){
    digitalWrite(BLUE, LOW); 
    digitalWrite(RED, LOW);    
    digitalWrite(GREEN, HIGH);
    //delayMicroseconds(ratio[1]/2);                    //timing for Green
    delayMicroseconds(30);
  }

  if (ratio[2]>0){
    digitalWrite(RED, LOW);
    digitalWrite(GREEN, LOW);    
    digitalWrite(BLUE, HIGH);
    //delayMicroseconds(ratio[2]);                    //timing for Blue
    delayMicroseconds(0);
  }
}
