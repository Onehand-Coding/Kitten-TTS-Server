# Kitten TTS Server: Lightweight TTS with API and Web UI

**Self-host the ultra-lightweight [KittenTTS model](https://github.com/KittenML/KittenTTS) with this enhanced API server. Features an intuitive Web UI, a flexible API, and large-text processing for audiobooks. Optional GPU acceleration is available.**

This server provides a robust, user-friendly, and powerful interface for the kitten-tts engine, an open-source, realistic text-to-speech model with just 15 million parameters. This project enhances the original model by adding a full-featured server, an easy-to-use UI, and optimized CPU-first inference, with optional GPU support via extras.

[![Project Link](https://img.shields.io/badge/GitHub-devnen/Kitten--TTS--Server-blue?style=for-the-badge&logo=github)](https://github.com/devnen/Kitten-TTS-Server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![Model Source](https://img.shields.io/badge/Model-KittenML/KittenTTS-orange.svg?style=for-the-badge)](https://github.com/KittenML/KittenTTS)
[![Web UI](https://img.shields.io/badge/Web_UI-Included-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](#)
[![API](https://img.shields.io/badge/OpenAI_Compatible_API-Ready-000000?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/docs/api-reference)

<div align="center">
  <img src="static/screenshot-d.png" alt="Kitten TTS Server Web UI - Dark Mode" width="33%" />
  <img src="static/screenshot-l.png" alt="Kitten TTS Server Web UI - Light Mode" width="33%" />
</div>

---

## 🗣️ Overview: Enhanced KittenTTS Generation

The [KittenTTS model by KittenML](https://github.com/KittenML/KittenTTS) provides a foundation for generating high-quality speech from a model smaller than 25MB. This project elevates that foundation into a production-ready service by providing a robust [FastAPI](https://fastapi.tiangolo.com/) server that makes KittenTTS significantly easier to use, more powerful, and drastically faster.

We solve the complexity of setting up and running the model by offering:

*   A **modern Web UI** for easy experimentation, preset loading, and speed adjustment.
*   Optional **GPU Acceleration** for NVIDIA GPUs via extras (see installation).
*   **Large Text Handling & Audiobook Generation:** Intelligently splits long texts into manageable chunks, processes them sequentially, and seamlessly concatenates the audio. Perfect for creating complete audiobooks.
*   **A flexible, dual-API system** including a simple endpoint and an OpenAI-compatible endpoint for easy integration.
*   **Built-in Voices:** A fixed list of 8 ready-to-use voices for consistent and reliable output.
*   **Cross-platform support** for Windows and Linux, with clear setup instructions.
*   Simple local install (no Docker files in this repo).

## 🍓 Raspberry Pi & Edge Device Support

The ultra-lightweight nature of the KittenTTS model and the efficiency of this server make it a perfect candidate for running on single-board computers (SBCs) and other edge devices.

*   ✅ **Raspberry Pi 5 (RP5):** Confirmed to run with **excellent performance**. The server is fast and responsive, easily handling requests from other devices on the same local network (LAN). This makes it ideal for local network services, home automation, and other DIY projects.

*   ⏳ **Raspberry Pi 4 (RP4):** Testing is currently in progress. Not working on the 32-bit Raspberry Pi OS.

To install, simply follow the standard **Linux installation guide** provided in this README.

## 🔥 Optional GPU Acceleration

By default the server runs on CPU-only dependencies for broad compatibility. If you have an NVIDIA GPU and want acceleration, install the optional GPU extras described below.

## 🔄 Alternative to Piper TTS

The [KittenTTS model](https://github.com/KittenML/KittenTTS) serves as an excellent alternative to [Piper TTS](https://github.com/rhasspy/piper) for fast generation on limited compute and edge devices like Raspberry Pi 5.

**KittenTTS Model Advantages:**
- **Extreme Efficiency**: Just 15 million parameters and under 25MB, significantly smaller than most Piper models
- **Universal Compatibility**: CPU-optimized to run without GPU on any device and "works literally everywhere"
- **Real-time Performance**: Optimized for real-time speech synthesis even on resource-constrained hardware

**This Server Project's Enhancement:**
While KittenTTS provides the ultra-lightweight foundation, this server transforms it into a production-ready Piper replacement by adding GPU acceleration (unavailable in the base model), modern REST/OpenAI APIs, audiobook processing capabilities, and an intuitive web interface—all while maintaining the model's edge device compatibility.

Perfect for users seeking Piper's offline capabilities with better performance on limited hardware and modern server infrastructure.

## ✨ Key Features of This Server

*   **🚀 Ultra-Lightweight Model:** Powered by the `KittenTTS` ONNX model, which is under 25MB.
*   ⚡ **Optional GPU Acceleration:** Enable NVIDIA (CUDA) support via `onnxruntime-gpu` by installing the GPU extra.
*   **📚 Large Text & Audiobook Generation:**
    *   Automatically handles long texts by intelligently splitting them based on sentence boundaries.
    *   Processes each chunk individually and seamlessly concatenates the resulting audio.
    *   **Ideal for audiobooks** - paste entire books and get professional-quality audio.
*   **🖥️ Modern Web Interface:**
    *   Intuitive UI for text input, voice selection, and parameter adjustment.
    *   Real-time waveform visualization of generated audio.
*   **🎤 8 Built-in Voices:**
    *   Utilizes the 8 built-in voices from the KittenTTS model (4 male, 4 female).
    *   Easily selectable via a UI dropdown menu.
*   **⚙️ Dual API Endpoints:**
    *   A primary `/tts` endpoint offering full control over all generation parameters.
    *   An OpenAI-compatible `/v1/audio/speech` endpoint for seamless integration into existing workflows.
*   **🔧 Easy Configuration:**
*   All settings are managed through a single `configs/config.yaml` file.
    *   The server automatically creates a default config on the first run.
*   **💾 UI State Persistence:** The web interface remembers your last-used text, voice, and settings to streamline your workflow.
*   

---

## 🔩 System Prerequisites

*   **Operating System:** Windows 10/11 (64-bit) or Linux (Debian/Ubuntu recommended).
*   **Python:** Version 3.9–3.12
*   **Git:** For cloning the repository.
*   **eSpeak NG:** This is a **required** dependency for text phonemization.
    *   **Windows:** See installation guide below.
    *   **Linux:** `sudo apt install espeak-ng`
*   **Raspberry Pi:**
    *   Raspberry Pi 5
    *   Raspberry Pi 4      
*   **(For GPU Acceleration, optional):**
    *   An **NVIDIA GPU** with CUDA support.
*   **(For Linux Only):**
    *   `libsndfile1`: Audio library needed by `soundfile`. Install via `sudo apt install libsndfile1`.
    *   `ffmpeg`: For robust audio operations. Install via `sudo apt install ffmpeg`.

## 💻 Running the Server

## ▶️ Running the Server

**Important: First-Run Model Download**
The first time you start the server, it will automatically download the KittenTTS model (~25MB) from Hugging Face. This is a one-time process. Subsequent launches will be instant.

1.  **Activate the virtual environment** (if not already active).
    *   Windows: `.\venv\Scripts\activate`
    *   Linux: `source venv/bin/activate`

2.  **Run the server:**
    ```bash
    # If installed in editable mode: use module entry point
    python -m kitten_tts_server

    # Or the CLI script (installed via console script)
    meow
    ```

3.  The server will start and automatically open the Web UI in your default browser.
    *   **Web UI:** `http://localhost:8005`
    *   **API Docs:** `http://localhost:8005/docs`

4.  **To stop the server:** Press `CTRL+C` in the terminal.

### **Raspberry Pi 4 & 5 Installation (CPU-Only)**

KittenTTS runs excellently on Raspberry Pi devices, making it ideal for local network services and DIY projects. However, installation requirements vary significantly between Pi models due to CPU architecture differences.

#### **Raspberry Pi 5 - Full Support ✅**

**Raspberry Pi 5 works out-of-the-box** with the standard Linux installation guide above. No special steps required!

**Tested Configuration:**
- **Hardware:** Raspberry Pi 5 Model B Rev 1.0
- **OS:** Debian GNU/Linux 12 (bookworm) 64-bit
- **Architecture:** aarch64 (ARM64)
- **Python:** 3.11
- **Memory:** 4GB RAM
- **Installation:** Follow the standard [Linux Installation](#linux-installation) guide exactly

**Installation Steps:**
```bash
# Step 1: Install system dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y espeak-ng libsndfile1 ffmpeg python3-pip python3-venv git

# Step 2: Set up Python environment
python -m venv venv
source venv/bin/activate

# Step 3: Install Python dependencies
pip install -r requirements.txt

# Step 4: Start the server
python server.py
```

> **⏱️ Important:** During the `pip install -r requirements.txt` step, some Python packages (especially audio processing libraries like `librosa`, `praat-parselmouth`, and others) may need to be compiled from source on ARM architecture. This process can take **15-30 minutes** depending on your SD card speed and system load. This is normal - let it complete without interruption.

#### **Raspberry Pi 4 - Limited Support ⚠️**

**Raspberry Pi 4 support is currently in development** due to complex dependency compilation issues on 32-bit ARM architecture.

**Known Technical Challenges:**
- **ONNX Runtime:** No official ARM wheels available on PyPI
- **PyTorch Ecosystem:** Limited pre-built wheel availability for armv7l
- **NLP Dependencies:** SpaCy and related libraries fail to compile due to architecture detection issues
- **Audio Processing:** Some native audio libraries require manual compilation

**Current Status:**
- ✅ **64-bit Raspberry Pi OS:** May work with standard installation (limited testing)  
- ⚠️ **32-bit Raspberry Pi OS:** Requires complex manual dependency resolution
- 🔧 **Alternative Solutions:** Being developed for core functionality

**For Raspberry Pi 4 Users:**
We recommend upgrading to **64-bit Raspberry Pi OS** if possible, as this significantly improves compatibility with modern Python packages. For users requiring 32-bit support, please check our [GitHub Issues](link-to-issues) for the latest progress updates and community-contributed solutions.

**Alternative Recommendation:**
For the best Raspberry Pi TTS experience, we strongly recommend using a **Raspberry Pi 5** with the standard 64-bit OS, which provides excellent performance and full compatibility.

## 🧰 Installation

We recommend using `uv` for fast, reliable installs. Pip also works.

### 1) Clone the repository

```bash
git clone https://github.com/devnen/Kitten-TTS-Server.git
cd Kitten-TTS-Server
```

### 2) Create and activate a virtual environment

Using uv (recommended):

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

Or with Python venv:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3) Install eSpeak NG (Required)

- Windows: Install from releases; restart your terminal.
- Linux (Debian/Ubuntu): `sudo apt update && sudo apt install -y espeak-ng libsndfile1 ffmpeg`

### 4) Install the package

CPU-only (default):

```bash
uv pip install -e .        # or: pip install -e .
# Alternatively, explicitly: uv pip install -e .[cpu]
```

Optional GPU support (CUDA):

```bash
# First install CUDA-enabled PyTorch wheels appropriate for your CUDA version
pip install --index-url https://download.pytorch.org/whl/cu121 torch torchvision torchaudio

# Then install GPU extras for ONNX Runtime
uv pip install -e .[gpu]   # or: pip install -e .[gpu]
```

## 💡 Usage Guide

### Generate Your First Audio

1.  Start the server and open the Web UI (`http://localhost:8005`).
2.  Type or paste your text into the input box.
3.  Select a voice from the dropdown menu.
4.  Adjust the speech speed if desired.
5.  Click **"Generate Speech"**.
6.  The audio will play automatically and be available for download.

### Generate an Audiobook

1.  Copy the entire plain text of your book or chapter.
2.  Paste it into the text area.
3.  Ensure **"Split text into chunks"** is enabled.
4.  Set a **Chunk Size** between 300 and 500 characters for natural pauses.
5.  Click **"Generate Speech"**. The server will process the entire text and stitch the audio together seamlessly.
6.  Download your complete audiobook file.

## 📖 API Documentation

The server exposes two main endpoints for TTS. See `http://localhost:8005/docs` for an interactive playground.

### Primary Endpoint: `/tts`

This endpoint offers the most control.

*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "text": "Hello from the KittenTTS API!",
      "voice": "expr-voice-5-m",
      "speed": 1.0,
      "output_format": "mp3",
      "split_text": true,
      "chunk_size": 300
    }
    ```
*   **Response:** Streaming audio file (`audio/wav`, `audio/mp3`, etc.).

### OpenAI-Compatible Endpoint: `/v1/audio/speech`

Use this for drop-in compatibility with scripts expecting OpenAI's TTS API structure.

*   **Method:** `POST`
*   **Body:**
    ```json
    {
      "model": "kitten-tts",
      "input": "This is an OpenAI-compatible request.",
      "voice": "expr-voice-4-f",
      "response_format": "wav",
      "speed": 0.9
    }
    ```

## ⚙️ Configuration

All server settings are managed in the `configs/config.yaml` file. It's created automatically on first launch if it doesn't exist.

**Key Settings:**
*   `server.host`, `server.port`: Network settings.
*   `tts_engine.device`: Set to `auto`, `cuda`, or `cpu`. The server will use your GPU if set to `auto` or `cuda` and a compatible environment is found.
*   `generation_defaults.speed`: Default speech speed (1.0 is normal).
*   `audio_output.format`: Default audio format (`wav`, `mp3`, `opus`).

## 🛠️ Troubleshooting

*   **Phonemizer / eSpeak Errors:**
    *   This is the most common issue. Ensure you have installed **eSpeak NG** correctly for your OS and **restarted your terminal** afterward. The server includes auto-detection logic for common install paths.
*   **GPU Not Used (if you installed GPU extras):**
    *   Ensure you installed CUDA-enabled PyTorch wheels and the `[gpu]` extra.
    *   Verify with `python -c "import torch; print(torch.cuda.is_available())"`.
*   **"No module named 'soundfile'" or Audio Errors on Linux:**
    *   The underlying system library is likely missing. Run `sudo apt install libsndfile1`.
*   **"Port already in use" Error:**
*   Another application is using port 8005. Stop that application or change the port in `configs/config.yaml` (e.g., `port: 8006`) and restart the server.

## 🙏 Acknowledgements & Credits

*   **Core Model:** This project is powered by the **[KittenTTS model](https://github.com/KittenML/KittenTTS)** created by **[KittenML](https://github.com/KittenML)**. Our work adds a high-performance server and UI layer on top of their excellent lightweight model.
*   **Core Libraries:** FastAPI, Uvicorn, ONNX Runtime, PyTorch, Hugging Face Hub, Phonemizer.
*   **UI Inspiration:** The UI/server architecture is inspired by our previous work on the [Chatterbox-TTS-Server](https://github.com/devnen/Chatterbox-TTS-Server).

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please feel free to open an issue or submit a pull request.



