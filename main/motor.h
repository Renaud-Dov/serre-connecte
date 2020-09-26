#ifndef MotorDov
#define MotorDov

class motor
{
private:
    int m_pin;
public:
    motor(int pinGPIO);
    int Returnpin();

    void High();
    void Low();


};



#endif