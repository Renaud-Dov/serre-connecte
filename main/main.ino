#include <Arduino_JSON.h>
#include <JSON.h>
#include <JSONVar.h>
#include <Stepper.h>
 
Stepper motor(64, 9, 11, 10, 8);  
 

void setup() {
  Serial.begin(9600);
}


JSONVar jsontext(String data){
  JSONVar myArray = JSON.parse(data);
  return myArray;
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    JSONVar myArray = jsontext(data);
    Serial.print(myArray);
    Serial.println(myArray["type"]);
    if ((int) myArray["type"]>=10)
    {
      Serial.println(true);
    }

    // jsontext(data);
    if ((String) myArray["type"]=="moteur")
    {
      /* code */
    }
    else if (data=="")
    {
      /* code */ 
    }
    
    
  }
  
}


bool moteur(bool open){
  Serial.println("moteur");
}