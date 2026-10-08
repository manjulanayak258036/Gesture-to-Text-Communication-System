# Gesture-to-Text Communication System

This project currently contains a PC-side webcam hand-detection prototype. It uses MediaPipe Hand Landmarker to detect one hand, draw its landmark points and connections on a live camera feed, and report when a hand is detected.

> Gesture recognition, text conversion, and ESP32 communication are not implemented in this prototype yet.

## Requirements

- Python 3.10 or newer
- A webcam
- Windows, macOS, or Linux with a graphical display for the OpenCV camera window

The hand landmark model is included at `pc_side/hand_landmarker.task`; no separate model download is needed.

## Setup

From the project root, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```sh
source .venv/bin/activate
```

## Run

From the project root:

```sh
python pc_side/m1_hand_detect.py
```

The live webcam window is mirrored for convenience. Press **Esc** to exit. The script uses camera index `0` by default; if your webcam uses a different index, change `cv2.VideoCapture(0)` in `pc_side/m1_hand_detect.py`.

If the camera cannot be opened, check that it is connected, available to other applications, and permitted by your operating system's camera privacy settings.

## Project layout

```text
pc_side/
  hand_landmarker.task   MediaPipe hand landmark model
  m1_hand_detect.py      Webcam hand detection and landmark drawing
requirements.txt         Python dependencies
```
