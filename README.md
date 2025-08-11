# Hand Gesture Control Suite

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/opencv-4.7.0.72-green)
![MediaPipe](https://img.shields.io/badge/mediapipe-0.10.0-orange)

A Python-powered computer vision system that enables touchless interaction with your digital environment through advanced hand gesture recognition.

## Features

- **Virtual Touchless Keyboard** - Type with hand gestures
- **Application Control** - Launch programs with finger gestures (Word, Excel, Firefox)
- **Air Drawing Canvas** - Create digital art with hand movements
- **Smart Gesture Recognition** - 10+ customizable gesture patterns
- **Real-Time Processing** - 30+ FPS performance

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/hand-gesture-control.git
cd hand-gesture-control
```

2. **Set up virtual environment (recommended)**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Basic controls
- Raise right hand fingers to show instructions
- Use right index finger to type on virtual keyboard
- Right pinky alone to erase text

**Left hand gestures**:

- ☝️ 1 finger: Open Word
- ✌️ 2 fingers: Open Excel
- 🤟 3 fingers: Open Firefox
- ✊ All down: Close Firefox

**Two-hand mode for drawing**:
- Left hand sets color (1-4 fingers)
- Right hand draws (index finger)

## Requirements
- Python 3.8+
- Webcam
- Windows/macOS/Linux
