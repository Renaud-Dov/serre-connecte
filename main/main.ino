#include <ArduinoJson.h>
#include <Stepper.h>
 
Stepper motor(64, 9, 11, 10, 8);  
bool finishAction=true;
void setup() {
  Serial.begin(9600);
  motor.setSpeed(100);
}

// {"type":"moteur","value":15}
void loop(){
  if (finishAction && Serial.available() > 0) {
      Serial.println(Serial.available())
      DynamicJsonDocument doc(300);
      String data = Serial.readStringUntil('\n');

      DeserializationError err = deserializeJson(doc, data);;
      
      if (err == DeserializationError::Ok) {
        if (doc["type"].as<String>()=="moteur"){
          Serial.println(doc["value"].as<int>());
        }
        else if (doc["type"].as<String>()=="fenetre"){
          finishAction = false;
          Serial.print(doc["val"].as<int>());
          motor.step(doc["val"].as<int>());
          Serial.println("finish");
          finishAction = true;
        }
      }
      else{
        // Print error to the "debug" serial port
        Serial.print("deserializeJson() returned ");
        Serial.println(err.c_str());
      }
  }
  
}


bool moteur(bool open){
  Serial.println("moteur");
}