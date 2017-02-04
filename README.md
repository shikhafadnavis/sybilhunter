# sybilhunter

File nodedetails1.xml is a self created TOR consensus file with the following TOR relay parameters:
IP address,
Port,
Bandwidth and
Fingerprint

File modify2.py emulates the attacker side where a few malicious relays change their fingerprints.
To run: python modify2.py
output: Modified nodedetails1.xml file with each node getting a new fingerprint tag in addition to the ones that exist. Nodes with port=1443 get a new randomly generated fingerprint and the rest are assigned the same value as previous.

File fingerprintanalysis.py analyzes the malicious relays on the basis of fingerprints changed.
To run: python fingerprintanalysis.py
Output: List of malicious relays

File bwuptime.py uses the nodedetails1.xml file to form relays' strings by concatenating IP address, port and bandwidth. Finds Levenshtein distance between a 'seed' string and all the strings from nodedetails1.xml
To run: python bwuptime.py
Output: Levenshtein distance between seed and each relay from the consensus file.
