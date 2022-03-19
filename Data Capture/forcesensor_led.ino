int redLED = 2;

void setup() {

pinMode(redLED, OUTPUT);
Serial.begin(9600);

}


void loop(){

float force_in_computer_units = analogRead(0);

  if (force_in_computer_units > 700){
    digitalWrite(redLED,HIGH);
  }
  else{
    digitalWrite(redLED,LOW);
  }
  
Serial.println(force_in_computer_units);

 
delay(200);


}