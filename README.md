# EyeOpener

**EyeOpener** is an experimental binocular vision research platform for standalone VR headsets such as the Meta Quest.

The project uses independent per-eye rendering to explore binocular vision, visual suppression, image alignment and stereoscopic visual stimuli in a highly configurable environment.

---

# Why EyeOpener?

I have amblyopia ("lazy eye") and, like many others, have spent years wondering how much of the problem is due to the eyes themselves and how much is due to the brain suppressing the weaker eye.

After researching modern binocular vision therapies, I realised that virtual reality headsets provide something that has historically been difficult to achieve outside specialist equipment: complete, real-time control over what each eye sees.

Rather than simply building an application for myself, I decided to create an open-source platform that anyone can study, modify and improve.

My hope is that EyeOpener becomes a useful engineering and research platform for developers, researchers, clinicians and anyone interested in binocular vision, virtual reality or visual perception.

---

# Current Status

EyeOpener is currently an early proof-of-concept.

The current prototype already supports:

* Independent left and right eye rendering
* Live adjustment of image position
* Independent brightness control for each eye
* Real-time binocular calibration
* USB development workflow using Python and WebXR

Development is progressing towards a fully standalone Quest application.

---

# Planned Features

## Calibration

* Independent X/Y adjustment
* Independent image scaling
* Brightness balancing
* Contrast balancing
* Blur adjustment
* Calibration profiles
* Save and load calibration

## Exercises

* Fusion targets
* Suppression testing
* Tracking exercises
* Letter and symbol recognition
* Stereo image exercises
* Daily guided training sessions

## Logging

* Calibration history
* Daily session logging
* Progress tracking
* Configuration profiles

## Platform

* Native Meta Quest application
* Controller support
* Hand tracking
* Standalone operation
* Cross-platform support

---

# Technology

Current prototype:

* Python
* Flask
* HTML5
* JavaScript
* WebGL
* WebXR

Future versions may migrate to a native OpenXR-based application once the research platform has matured.

---

# Contributing

Contributions are always welcome.

Whether you are a software developer, researcher, clinician, orthoptist, optometrist or simply someone interested in binocular vision, ideas and improvements are greatly appreciated.

Please feel free to open issues, suggest improvements or submit pull requests.

---

# Disclaimer

EyeOpener is experimental software.

It is **NOT** a medical device.

It has **NOT** been clinically validated.

It is intended solely as a research, educational and software development platform.

Nothing contained within this project should be interpreted as medical advice or as evidence that any exercise or technique is effective for the diagnosis, treatment or prevention of any medical condition.

Please read the accompanying **LICENSE** and **DISCLAIMER.md** files before using this software.

---

# Licence

Licensed under the Apache License, Version 2.0.

See the accompanying **LICENSE** file for full details.

---

## Author

Simon Macdonald-Smith

GitHub: https://github.com/m0ivq
