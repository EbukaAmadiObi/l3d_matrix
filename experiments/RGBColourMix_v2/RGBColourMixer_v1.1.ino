/*
 *  University College Dublin
 *  School of Electronic and Electrical Engineering
 *  
 *  ElecSoc
 *  
 *  Robotics Officer: Chukwuebuka Amadi-Obi
 *  
 *  Script Name  : RGB Colour Mixer
 *  Author       : Joe Biju, David Remenyik
 *  Date         : 07 February 2024
 *  
 *  ### SCRIPT OVERVIEW
 *  
 *  ## Objective
 *  - Program should take in RGB values for a colour (0-255), and use PWM to
 *    achieve an appropriate colour in 4-pin RGB LED with common anode
 *  - It should be programmed so it acts with minimal/no delay, as this is to be
 *    scaled up to 512 LEDs together
 *  
 *  ## Script Details
 *  - The script avoids the use of the delay() function, instead opting for millis()
 *    and if condition to check if a block of code should run/wait
 *      - The delay() functions causes the whole script to halt, preventin scripts 
 *        from runnning in parallel
 *  - It is currently intended for one LED only
 *  - It should use Serial Port to communicate with computer/other software to 
 *    update the colours rather than manually
 *
 *  ### LIMITATIONS
 *  - Must convert RGB values in 255 form into 0-25 range
 *  - To force a colour to stay permanetly on, -1 must be used [FIXED?]
 *  - Reading in from Serial Port, conversions from String - Char - Int is inefficient,
 *    and also require converting ASCII to Integer
 *  - There's defo some other stuff but can't think of any rn
 *  
 *  ### VERSIONS
 *  V0.1 (Done) -  31 January 2024
 *  - LED connected to Arduino
 *  - Basic PWM using delay()
 *  - Trial using millis() with mod (%). Unable to test if worked
 *
 *  V1.1 (Done) -  07 January 2024
 *  - Switch to use of millis()
 *  - Can read in inputs from Serial Monitor Window ('New Line' selected)
 *    in the form ##,##,## and convert RGB values into colour on LED
 *      - Note: Colour doesn't always match perfectly due to brightness of LED
 *  - Attempted Unity integration where spacebar would toggle the LED on/off
 * 
 *  V1.2 (Planned)
 *  - Address limitations listed above
 *      - Try introduce a mapping function convert 0-255 range to 0-25
 *  - Add !redStatus etc. to invert bool operator in digitalWrite() and use 
 *    'TRUE' and 'FALSE' to make it easier to understand if light selected ON or OFF
 *
 */




//------------------------------------
#define RED 2
#define GREEN 3
#define BLUE 4




//------------------------------------
bool redStatus = 1;  //Off
bool greenStatus = 1;
bool blueStatus = 1;
int redTick = 0;
int greenTick = 0;
int blueTick = 0;

//Set colour (map 0-255 -> 0-25)
//Example: Teal = rgb(88, 159, 164) -> 9, 16, 16
int redIntensity = 25;  //100% (Full) brightness
int greenIntensity = 0; //0% (No) brightness
int blueIntensity = 10; //40% brightness


char receivedCharData[10] = "00,00,00"; //For Serial.readStringUnitl() to be converted to Char array
char serialMsg[20]; //Degugging: For outputting messages to console, in combination with sprintf()




//------------------------------------
void setup() {
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);

  //Turn off all LEDS
  // digitalWrite(RED, HIGH);
  // digitalWrite(GREEN, HIGH);
  // digitalWrite(BLUE, HIGH);

}




//------------------------------------
void loop() {
  //Edit colours using Serial Communication
  if (Serial.available() > 0) { //Check if Serial Connection is open before trying to read
    // int a = Serial.read()); //Will read integers and convert to ASCII. Each integer is outputted individually
    // Serial.println(a, DEC); //Attempt to convert into decimal format
    String receivedData = Serial.readStringUntil('\n'); //When using 'Arduino Serial Monitor', select 'New Line'
    receivedData.toCharArray(receivedCharData, 10);

    //Change intensities to selected values
    //As input must (should) be in form '##,##,##', we can just take indexes 0,1,3,4,6,7
    redIntensity = (receivedData[0] - 48) * 10 + receivedData[1] - 48;  //ASCII value of '0' is '48'
    greenIntensity = (receivedData[3] - 48) * 10 + receivedData[4] - 48;
    blueIntensity = (receivedData[6] - 48) * 10 + receivedData[7] - 48;

    //EXAMPLE:
    //[User Input]  10,10,10
    //['receivedCharData' would contain]  '49','48','44','49','48','44','49','48','44' [49=1, 48=0, 44=,]

    //DEBUG: Confirm input with Serial output
    sprintf(serialMsg, "%d %d %d", redIntensity, greenIntensity, blueIntensity);
    Serial.println(serialMsg);

    //Code for Unity Integration
    // if (receivedData == "ON") {
    //   redIntensity = 25;  // Always On
    // // } else if (receivedData == "LED_OFF") {
    // //   digitalWrite(LED_BUILTIN, LOW);
    // } else if (receivedData == "OFF") {
    //   redIntensity = -1; //Always off
    // }
  }

  //Refresh colours every 1ms
  if ((millis() % 1) == 0) { digitalWrite(RED, redStatus); }
  if ((millis() % 1) == 0) { digitalWrite(GREEN, greenStatus); }
  if ((millis() % 1) == 0) { digitalWrite(BLUE, blueStatus); }

  //redTick and check redStatus
  if (redTick < redIntensity) { redStatus = 0; redTick++; }  //Keep light ON
  else if (redTick < 25) { redStatus = 1; redTick++; } //Keep light OFF 
  else if (redTick >= 25) { redTick = 0; }  //Reset tick (25 max Intensity)

  //greenTick and check greenStatus
  if (greenTick < greenIntensity) { greenStatus = 0; greenTick++; } //Keep light ON
  else if (greenTick < 25) { greenStatus = 1; greenTick++; } //Keep light OFF
  else if (greenTick >= 25) { greenTick = 0; }  //Reset tick (25 max Intensity)

  //blueTick and check blueStatus
  if (blueTick < blueIntensity) { blueStatus = 0; blueTick++; } //Keep light ON
  else if (blueTick < 25) { blueStatus = 1; blueTick++; } //Keep light OFF
  else if (blueTick >= 25) { blueTick = 0; }  //Reset tick (25 max Intensity)

}

//OBSOLETE
//void loop() {
  // if ((millis() % 1000) == 0) { colourOn(RED, 0, 0);} else {colourOn(RED, 1, 1);}
  // if ((millis() % 1000) == 0) { colourOn(GREEN, 0, 0);}  else {colourOn(GREEN, 1, 1);}
  // if ((millis() % 1000) == 0) { colourOn(BLUE, 0, 0);}  else {colourOn(BLUE, 1, 1);}
  // colourOn(GREEN, 4, 1);
  // colourOn(BLUE, 1, 1);
  // digitalWrite(RED, LOW);
  //Always digitalWRite(currentSetting);
  //Update each tic of loop until specificed number is reached
  //Change status
//}
// void colourOn(char colour, int t1, int t2) {

//   digitalWrite(colour, t1);
// delay(t1);
// digitalWrite(colour, HIGH);
// delay(t2);
// }
