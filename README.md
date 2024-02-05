# The Cloud Party Lights
## Summary
The Cloud is a fun decorative light source that flows through a rainbow of colors in accordance to sounds it hears. This product could be used as a nightlight or in a party setting post-covid. We assembled a circuit using a Raspberrypi, breadboards, transistors, resistors, a USB microphone, and an LED strip. The code assembled contains a beat detector that records audio in 3 second intervals and uses a beat detector algorithm to determine its BPM. This BPM is then used as the increment for the LED lights to change color. The audio continuously records, so the beat to which the LEDs change color is updated for every 3 second chunk. The beat detector accurately determines the beat per minute of the audio, and the LEDs successfully go through a progression of colors at that rate.
## Design
For our project, we used a RaspberryPi 3, Arduino Breadboard, an LED light strip, 3 transistor and 3 resistors. We also used a microphone plugged into the RaspberryPi to pull in the audio. The image show how we set up our circuit, connecting the Arduino Breadboard to the RaspberryPi and the LED lightstrip. For future projects utilizing this setup and code, changes could be made using other functions to make the lights flash rather than having the lights flow through the rainbow.

![Wiring Diagram](https://github.com/joedvorak/BAE305-Project-2021---The-Cloud-Party-Lights/blob/main/116598108-74344000-a8f4-11eb-9a57-770367ecadfc.png)

For the physical design component, we used a large water jug and wrapped our LED strip around it. We added "fluff" on top of the LED strip to create the cloud effect.
## Code
See the repository
## Testing
Since there were many different components of this project, we had to test things separately.To ensure the LED strip was working we plugged it into the wall and watched the lights glow bright. To test and assemble the circuit, we put together a simple blinking code and treated the LED strip as an RGB LED. Once we were able to get all of the colors to flash, we knew that the circuit would function correctly. The code was tested in individual sections as well. We first assembled a code that would make the LED strip flash different colors. With this we found we had to download a variety of libraries and troubleshoot through examples found on GitHub and other resources. We then moved onto the beat detection section. Here we had to ensure the USB microphone could record sound to a wav.file and that we could continuously overwrite the wav.file. The beat detector algorithm from Librosa was able to access the wav.file and determine the bpm. Once these sections were in place, we had to combine them to make the lights change color in accordance to the beats detected. We then ensured that the LEDs were referencing the continuously updated bpm variable to determine the rate at which they changed color.
## Results
Combining the physical component, circuit, and code we were able to create a decorative cloud that flows through the rainbow in accordance to beats detected in a song or sound it can hear. This design could work in many different settings. We are using our product with music, but it could be used to detect different kinds of beats such as heart beats, metronomes, or the ticking of a clock. This project works efficiently and does exactly what we wanted it to. The limitations are that it picks up sound in 3 second increments, so there may be a delay in the LED lights if there are frequently changing beats within a song. Another limitation is that the sound has to be relatively close to the USB microphone in order for it to detect the beats and it starts at a predetermined BPM. Another limitation is that the sound has to be relatively close to the USB microphone in order for it to detect the beats. Some things it can not do are detect beats that are at a great distance away, detect beat changes that are faster than 3 seconds, and start and stop on its own. Overall this project required a lot of patience and critical thinking and resulted in our desired outcome.
