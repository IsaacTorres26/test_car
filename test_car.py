from machine import Pin, PWM  # type: ignore[reportMissingImports]
import time

p_servo = Pin(23, Pin.OUT)
servo1 = PWM(p_servo)
servo1.freq(50)

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def servo(angulo):
    servo1.duty(map(angulo, 0, 180, 20, 120))

def centro():
    servo(95)

def izquierda():
    servo(45)     

def derecha():
    servo(125)    

#m1
IN1 = Pin(27, Pin.OUT)
IN2 = Pin(26, Pin.OUT)
#m2
IN3 = Pin(25, Pin.OUT)
IN4 = Pin(33, Pin.OUT)

ENA = PWM(Pin(14), freq=1000)
ENA1 = PWM(Pin(12), freq=1000)

velocidad = 60000

def adelante():
    #m1
    IN1.value(1)
    IN2.value(0)
    #m2
    IN3.value(1)
    IN4.value(0)
    ENA.duty_u16(velocidad)
    ENA1.duty_u16(velocidad)

def atras():
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)
    ENA.duty_u16(velocidad)
    ENA1.duty_u16(velocidad)

def parar():
    ENA.duty_u16(0)
    ENA1.duty_u16(0)
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)


centro()
parar()

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
