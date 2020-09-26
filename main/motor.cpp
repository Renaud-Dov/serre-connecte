#include "motor.h"
motor::motor(int pinGPIO)
{
    m_pin=pinGPIO;
    pinMode(m_pin,OUTPUT);
}
int motor::Returnpin(){
    return m_pin;
}

void motor::High(){
    digitalWrite(m_pin, HIGH);
}

void motor::Low(){
    digitalWrite(m_pin, LOW);
}
