#include <Arduino_JSON.h>
#include <JSON.h>
#include <JSONVar.h>
#

void setup() {
  Serial.begin(9600);
}


JSONVar jsontext(String data){
  JSONVar myArray = JSON.parse(data);
  return
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    JSONVar myArray = jsontext(data)
    Serial.print(myArray);
    Serial.println(myArray["type"]);
    if ((int) myArray["type"]>=10)
    {
      Serial.println(true);
    }

    // jsontext(data);
    if (data=="moteur")
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