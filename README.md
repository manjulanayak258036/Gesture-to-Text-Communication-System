<div align="center">

# Gesture-to-Text Communication System

**A webcam-based hand-tracking prototype and the starting point for gesture-driven communication.**

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Landmarker-0097A7)

</div>

---

## Overview

The current PC-side prototype uses your webcam and MediaPipe Hand Landmarker to detect a hand, draw its landmarks and connections over the live video, and report when a hand is detected.

> **Current scope:** This repository currently implements hand detection only. Gesture classification, text conversion, and ESP32 communication are planned extensions, not implemented features.

## Features

- Live webcam video with a mirrored preview
- Detection of up to one hand
- On-screen hand landmark and connection drawing
- Included MediaPipe hand landmark model—no separate model download required
- Press **Esc** to close the preview

## Quick start

### Prerequisites

- Python 3.10 or later
- A webcam
- A graphical desktop session for the OpenCV preview window

### Install

Run these commands from the project root.

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**macOS / Linux**

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Start hand detection

```sh
python pc_side/m1_hand_detect.py
```

The live preview opens in a window. Press **Esc** to exit.

## Troubleshooting

| Issue | What to check |
| --- | --- |
| Camera cannot be accessed | Connect the camera, close other applications using it, and check your operating system's camera permissions. |
| Wrong camera is selected | The script uses camera index `0`. If needed, change `cv2.VideoCapture(0)` in `pc_side/m1_hand_detect.py` to the index for your camera. |
| No preview appears | Run the program in a desktop session that supports OpenCV windows; a headless terminal will not display the preview. |

## Project structure

```text
.
├── pc_side/
│   ├── hand_landmarker.task   # MediaPipe model asset
│   └── m1_hand_detect.py      # Webcam capture and hand detection
└── requirements.txt           # Python package dependencies
```

## Dependencies

The Python packages are listed in [`requirements.txt`](requirements.txt) and can be installed with:

```sh
python -m pip install -r requirements.txt
```
