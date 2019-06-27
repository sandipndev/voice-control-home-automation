int lightPin = 23;
int fanPin = 22;

void setup() {
    pinMode(fanPin, OUTPUT);
    pinMode(lightPin, OUTPUT);
    digitalWrite(fanPin, HIGH);
    digitalWrite(lightPin, HIGH);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        int data = (int) Serial.read();

        if (data == 49) // data sent = 1
            digitalWrite(lightPin, LOW);
        else if (data == 50) // data sent = 2
            digitalWrite(lightPin, HIGH);
        else if (data == 51) // data sent = 3
            digitalWrite(fanPin, LOW);
        else if (data == 52) // data sent = 4
            digitalWrite(fanPin, HIGH);
    }
}
