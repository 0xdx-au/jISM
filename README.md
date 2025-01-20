
```
                                                                                
   ▄▄▄██▀▀▀██▀▀██▀▀██▀▀███▀▀▀▀███▄▄▄                                         
 ▄▄█▓▓██▄▄▄██▀▀██▀▀██▀▀███▀▀▀▀███▓▓█▄▄                                       
▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌                                      
 ▀█████████████████████████████████████▀                                       
    ▄▄███████▀▀▀▀▀▀▀▀▀▀▀▀▀███████▄▄                                          
  ▄██▀▀                          ▀▀██▄                                        
 ██▀     ▄▄█████▄▄   ▄▄█████▄▄     ▀██                                       
██     ▄██▀▀▀▀▀▀▀██▄██▀▀▀▀▀▀▀██▄     ██                                      
██     ██        ▀███▀        ██     ██     🍆💦 jISM - Making ISM Wet Again    
██     ▀██▄     ▄███▄     ▄██▀     ██                                      
 ██▄     ▀▀█████▀▀   ▀▀█████▀▀    ▄██                                       
  ▀██▄▄                          ▄▄██▀                                        
    ▀▀███████▄▄▄▄▄▄▄▄▄▄▄▄███████▀▀                                          
 ▄█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▄                                      
▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌                                      
 ▀▀█████████████████████████████████▀▀                                       
```

# jISM - OSCAL ISM Controls Viewer 

## What is this? 
A spicy front-end for viewing ACSC's ISM controls via OSCAL, built on CentOS CIS Level 2 because we like it secure AND saucy 🌶️

## Features
- 🔒 Hardened CentOS base (CIS Level 2)
- 💦 Wet and wild web interface
- 🌊 Real-time OSCAL feed integration
- 🎯 Visual control mapping
- 🛡️ Security-first (but fun-second) architecture

## Quick Start
```bash
git clone https://github.com/0xdx-au/jISM.git
cd jISM
docker-compose up -d
# Now go get wet at http://localhost:8080
```

## Architecture
- Web Application (www/): This is where the Flask application resides. It serves the web interface and API endpoints.
- OSCAL Feed Handler (feed/): This component fetches and processes the OSCAL feed data.
- Database (db/): This component sets up a PostgreSQL database to store processed OSCAL data.
- Docker Compose: Manages the orchestration of the three containers.

## Why CentOS CIS Level 2?
Why use protection? Because it's better to be safe than sorry! 🎯 (seriously just because)

## Acknowledgments
Big wet thanks to:
- Australian Cyber Security Centre (ACSC)
- Australian Signals Directorate (ASD)
- The ISM team (keeping Australia secure)
- NIST OSCAL Project (structured controls ftw)

*Not officially endorsed by ACSC/ASD - just making security more fun!*

## Based On
- [AustralianCyberSecurityCentre/ism-oscal](https://github.com/AustralianCyberSecurityCentre/ism-oscal)
- [0xdx-au/jISM](https://github.com/0xdx-au/jISM/)

## License
MIT - See [LICENSE](LICENSE)

```
     💦 GET WET WITH ISM 💦
    ┌────────────────────┐
    │  🍆 Controls      │
    │  📊 Compliance    │
    │  🎯 Security      │
    │  🌊 Automation    │
    └────────────────────┘
```

[![Build Status](https://img.shields.io/badge/build-wet-blue.svg)](https://github.com/0xdx-au/jISM)
[![Security](https://img.shields.io/badge/security-moist-blue.svg)](https://github.com/0xdx-au/jISM)
[![License](https://img.shields.io/badge/license-damp-blue.svg)](https://github.com/0xdx-au/jISM/blob/main/LICENSE)
