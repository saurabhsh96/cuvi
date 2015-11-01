/* Computer-User Voice Interface Using App
  - Saurabh S Nerkar
  - Yashveer 
  This system is basically a communication module between the user
  and the computer.
*/
String test;
void setup()
{
  Serial.begin(9600);
}

void loop()
{ 
  if((Serial.available())>0)
  {
    test=Serial.readStringUntil('\n');
    Serial.println(test);
}
}
