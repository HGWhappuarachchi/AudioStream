# Audio Streaming Project

This project allows for audio streaming from a Windows host PC to a Raspberry Pi receiver over a network. The host PC captures audio using a virtual audio cable and streams it to the Raspberry Pi, which plays the audio. Both the host and receiver programs are set to run as services for continuous operation.

## Prerequisites

- Python installed on both host PC and Raspberry Pi
- Network connection between host PC and Raspberry Pi
- Basic knowledge of command line interface

## Installation Guide

### Host PC (Windows) Setup

1. **Install Virtual Audio Cable**:
   - Download the Virtual Audio Cable from [here](https://download.vb-audio.com/Download_CABLE/VBCABLE_Driver_Pack43.zip).
   - Extract the ZIP file and run the installer (`VBCABLE_Setup_x64.exe` for 64-bit Windows or `VBCABLE_Setup.exe` for 32-bit Windows).
   - Follow the installation prompts to complete the setup.

2. **Install Python**:
   - Download and install Python from the official [Python website](https://www.python.org/downloads/).
   - Ensure you select the option to add Python to your PATH during installation.

3. **Install Required Python Libraries**:
   ```bash
   pip install pyaudio
