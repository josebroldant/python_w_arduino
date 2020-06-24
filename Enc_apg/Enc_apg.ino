int led=13;

void setup() {
  Serial.begin(9600);//inicia el serial
  pinMode(led,OUTPUT);//define al led como salida

}

void loop() {
  if(Serial.available()>>0){//si hay bytes disponibles
    char by=Serial.read();//lee el byte que le llega
    if(by=='1'){//si el byte esta en 1
      digitalWrite(led,HIGH);//Poner el pin en 1
    }
    else
      digitalWrite(led,LOW);//Poner el pin en 0
  }

}
