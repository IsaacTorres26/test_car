from machine import Pin, PWM  
import time

#WE DEFINE THE PIN TO SERVO MOTOR FOR PWM WITH THE VARIABLE "p_servo"
p_servo = Pin(23, Pin.OUT)
servo1 = PWM(p_servo)
servo1.freq(50)

# CONVERTS x FROM THE RANGE [in_min, in_max] TO THE RANGE [out_min, out_max]
def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# MOVES THE SERVO MOTOR BEHIND 0° AND 180°
def servo(angulo):
    servo1.duty(map(angulo, 0, 180, 20, 120))

#FUNCTION TO SET SERVO TO 95° (CENTER POSITION)
def centro():
    servo(95)

#FUNCTION TO SET SERVO TO 45° (LEFT POSITION)
def izquierda():
    servo(45)     

#FUNCTION TO SET SERVO TO 45° (RIGHT POSITION)
def derecha():
    servo(125)    

#WE DEFINE THE OUTPUT PINS FOR MOTOR 1

IN1 = Pin(27, Pin.OUT)
IN2 = Pin(26, Pin.OUT)

#WE DEFINE THE OUTPUT PINS FOR MOTOR 1

IN3 = Pin(25, Pin.OUT)
IN4 = Pin(33, Pin.OUT)

#WE DEFINE ENABLE FOR PWM

ENA = PWM(Pin(14), freq=1000)
ENA1 = PWM(Pin(12), freq=1000)

#WE DEFINE VELOCITY VARIABLE

velocidad = 60000

#FUNCTION FOR FORWARD MOVEMENT
def adelante():
    #m1
    IN1.value(1)
    IN2.value(0)
    #m2
    IN3.value(1)
    IN4.value(0)
    ENA.duty_u16(velocidad)
    ENA1.duty_u16(velocidad)

#FUNCTION FOR BACKWARD MOVEMENT
def atras():
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)
    ENA.duty_u16(velocidad)
    ENA1.duty_u16(velocidad)

#FUNCTION STOP 

def parar():
    ENA.duty_u16(0)
    ENA1.duty_u16(0)
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

#STOP THE CAR TO START THE PROGRAM

centro()
parar()

#CICLE WHILE WHICH ASK FOR A STRING TO THE MOTOR MOVEMENT AND SERVOMOTOR MOVEMENT
while True:
    tecla = input("Escribe aqui")
    if tecla == "w":
        adelante()
    elif tecla == "s":
        atras()
    elif tecla == "a":
        izquierda()
    elif tecla == "d":
        derecha()
    elif tecla == "c":
        centro()
    elif tecla == "x":
        parar()
    elif tecla == "t":
        break

