# Lab 5

## Team Members
- Faith Klein
- Tina Habibi

## Lab Question Answers

# Part 1 Questions

1) What is dBm? What values are considered good and bad for WiFi signal strength?
    dBm, also know as decibel-milliwatts is the unit of measurement used when working with WiFi signal strength. This is representative of the power level of a specfic signal on a log scale that is relative to 1 milliwatt. It is important to note that these values are typically negative, so the higher the value (less negative), the stronger the signal, and vice versa. Good signal stength will be between -30 dBm and -60 dBm, while a bad signal strength would be below -70 dBm. 

2) Why do we need to check the OS? What is the difference between the commands for each OS?
    Since different operating systems use different commands, we need to check the OS to ensure the script runs the the appropiate command. Linux uses iwconfig wlan0 and retrieves the signal strength directly in dBm. Windows uses netsh wlan and shows interfaced, proviidng signal quality as a percentage. Mac uses airport -I to get the RSSI value in dBm.  

3) In your own words, what is subprocess.check_output doing? What does it return?
    subprocess.check_output will run a shell command and then captures the output as a byte string while it waits for it to be completed. The command's output will be the returnb value, which will then need to be decoded into a string that is actually readable. 

4) In your own words, what is re.search doing? What does it return?
    re.search will search a string for a match to some given regaular expression pattern and if found, it returns a match object. If not found, it returns None. The match object will contain the extracted value and it can be accessed using .group(n). 

5) In the Windows case, why do we need to convert the signal quality to dBm?
    Since windows provides the signal quality as a percentage, we need to convert the percentage to dBm. We use signal_strength = -100 + signal_quality / 2 to map the percentage value to an estimated dBm range. 

6) What is the standard deviation? Why is it useful to calculate it?
    The standard deviation measures the variation of a datasetn and it is useful to calculate it because it helps assess consistency in WiFi signal strength at a given location. 

7) What is a dataframe? Why is it useful to use a dataframe to store the data?
    A dataframe is a 2D table like data structure in Pandas that sturctures data into specific columns and rows. It is useful to use a dataframe to store this data because it allows easy manipulation, visualization, and analysis of organized data (like a WiFi signal strength readinfs across locations). 

8) Why is it important to plot the error bars? What do they tell us?
    It is important to plot the error bars because they visually represent the variability/standard deviation in the data. In this lab, they tell us how much the WiFi signal strength fluctautes at each location and indicates whether we were seeing stability or interference at these locations. 

9) What did you observe from the plot? How does the signal strength change as you move between locations? Why do you think signal strength is weaker in certain locations?
    The plot pretty much came out as we expected - the further locations that we began with had lower strengths nearing -70 dBm, with one even having a strength near nearing -80 dBm (which was the lowest strength we encountered). The strength that was neaering -80 dBm made sense because it was taken in the stairs, where there were various walls and doors. The other low values were taken on higher floors, but there were less walls/doors in between the router and the locations, which is why they were higher than the one from the stairwell. As we got to the same floor that the router was on, the signals got stronger (around -45) which makes sense since there was a lot less in between the location and the router. 

# Part 2 Questions

1) How does distance affect TCP and UDP throughput?
    Both TCP and UDP experience throughput degradation as distance increases, but the reasons and extent of degradation differ for the two. TCP is affected by latency, packet loss, and congestion control algorithms. However, UDP does not have built-in congestion control, acknowledgments, or retransmissions, so throughput degradation mainly comes from packet loss and network congestion.

2) At what distance does significant packet loss occur for UDP?
    Our data showed that for UDP there was no packet loss. In general, this distance will depend on certain conditions, like network conditions, interference, and the medium of transmission. For a 2.4 GHz WiFi network, in general the distance can be up to 100-150 feet indoors and 300+ feet outdoors, with interference potentially casuing packet loss. For a 5 GHz network, attenuation is more likely, and there is an effective range of 50-100 feet indoors before signficiant degradation. 

3) Why does UDP experience more packet loss than TCP?
    UDP typically experiences more packet loss than TCP because of its lack of reliability mechanisms, such as no acknowledgements or congestion control. In UDP, there are no acknowledgements or retransmissions, so if a packet is lost then it is gone for good. UDP also keeps sending packets at a constant rate regardless of whether the network is overloaded or not. As a result, UDP experiences more packet loss but it is faster and more efficient for real-time applications when minor packet loss is okay.

4) What happens if we increase the UDP bandwidth (-b 100M)?
    Increasing the UDP bandwidth increases the sending rate, but it can also lead to higher packet loss if the network cannot handle the increased traffic properly. UDP will send packets at the specified rate regardless of network congestion, but if your network has enough capacity then it should work fine. Other things like network overloading and potential overflows or buffer drops play a role as well. 

5) Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?
    Yes, performance would be different on 5 GHz Wi-Fi vs. 2.4 GHz. Stability, interference, speed, and range are all parameters that would be different. 5 GHz is more stable in environments where there are multiple Wi-Fi networks, which makes it more ideal for high-bandwith applications. 2.4 GHz can be less stable in urban like areas as a result of iterference but it is better for devices that are far from the router. 5 Ghz is less congested, which means better performance in areas with a lot of wireless devices, whereas 2.4 GHz is more crowded since it shares spectrum with Bluetooth and oter devices, leading to potential interference. 5 Ghz offers higher speeds because it supports wider channels and less interference, whereas 2.4 GHz is slower due to narrower channel bandwith and congestion. 5 GHz has a shorter range and is more eaisly blokced by walls and such, but 2.4 GHz has a longer range because lower frequencies travel farther and penetrate walls better. Overall, this is all to show that there would be performance differentation between the two. 