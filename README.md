# Project Haro

## Robot Prototype

![Robot Prototype](robot-prototype.png)

### Prototype Details

- **Prototype**: N° 003
- **Disciplines**: Mechanical / Electrical
- **Year**: 2026

## Current Progress

Project Haro is a robot prototype with the following implemented modules:

### Code Structure

```
project-haro/
├── main.py          # Entry point — manages tmux session for the robot
├── pyproject.toml   # Project config (uv) with dependencies
├── core/
│   ├── audio.py     # Audio server wrapper — plays sounds via simple-audio-server
│   ├── indicator.py # Relay control — manages USB relay for hardware actuation
│   ├── reaction.py  # 🔄 Reaction system — sensor → response pipeline
│   ├── vision.py    # 🔄 Vision system — camera input, object detection
│   └── agent.py     # 🔄 AI agent system — decision making, task planning
├── sounds/
│   ├── oh_hello.mp3 # Greeting sound
│   └── new_type.mp3 # New type / event sound
└── README.md
```

### Dependencies

| Package | Source | Purpose |
|---|---|---|
| `libtmux` | PyPI | Manages tmux sessions for the robot |
| `simple-audio-server` | GitHub | Audio playback server |
| `usb-relay-diustou` | GitHub | USB relay control for hardware |

### Status

- ✅ Project scaffolded with `uv`
- ✅ Audio module implemented
- ✅ Relay/indicator module implemented
- ✅ Sounds directory with sample audio
- 🔄 **Reaction system** — pending (sensor input → response output)
- 🔄 **Vision system** — pending (camera capture, processing, recognition)
- 🔄 **AI agent system** — pending (decision making, task planning, memory)

## Planned Systems

### Reaction System (`core/reaction.py`)

Maps sensor inputs to physical responses:
- Input: camera, microphone, buttons, encoders
- Output: relay, audio, display
- Pipeline: `detect → classify → actuate`

### Vision System (`core/vision.py`)

Handles all camera-related functionality:
- Image capture and preprocessing
- Object/face detection
- Gesture or color recognition
- Frame analysis for environmental awareness

### AI Agent System (`core/agent.py`)

The brain of the robot:
- Task planning and execution
- Memory/context management
- Integration with LLM APIs
- Decision making based on vision + sensor data
