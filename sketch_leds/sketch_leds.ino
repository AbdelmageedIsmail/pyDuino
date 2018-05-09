#define LED 13
#define VALUE HIGH

int value;
byte mask = 1;
int ledOut;

void setup() {
    pinMode(LED, OUTPUT);
    
    Serial.begin(9600);
    
    value = HIGH;
    
    for (int i = 2; i < 10; i++) { //set pins from 2 to 9 as output
        pinMode(i, OUTPUT);
    }

    
}

void loop() {
    if (Serial.available()) {
              
        unsigned char readData = Serial.read(); // read the unsigned character received in the serial port

            ledOut = 2;
            mask = 00000001;
            
            for (ledOut = 2; ledOut<10; ledOut++) { //iterate through the pins, from LED at pin no 2 to LED on pin no 9   
        
              if (readData & mask){ // if bitwise AND resolves to true
                digitalWrite(ledOut,HIGH); // switch on the LED
              }
              else{ //if bitwise and resolves to false
                digitalWrite(ledOut,LOW); // switch off the LED
              }
              mask <<= 1; // shif the mask to the left.
              
            }

            // for debugging purpose, just toggle the output at pin 13, to switch the on-board led on and off each time a data received from the serial port
            digitalWrite(LED, value);            
            value = !value;                        
       
    }
}
