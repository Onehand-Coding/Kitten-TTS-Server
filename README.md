# Kitten TTS Server: High-Performance, Lightweight TTS with GPU Acceleration

**Self-host the ultra-lightweight [KittenTTS model](https://github.com/KittenML/KittenTTS) with this enhanced API server. Features an intuitive Web UI, a flexible API, large text processing for audiobooks, and uniquely, high-performance GPU acceleration.**

This server provides a robust, user-friendly, and powerful interface for the `kitten-tts` engine, an open-source, realistic text-to-speech model with just 15 million parameters. This project significantly enhances the original model by adding a full-featured server, an easy-to-use UI, and an optimized inference pipeline for both CPU and NVIDIA GPUs.

[![Project Link](https://img.shields.io/badge/GitHub-devnen/Kitten--TTS--Server-blue?style=for-the-badge&logo=github)](https://github.com/devnen/Kitten-TTS-Server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![Model Source](https://img.shields.io/badge/Model-KittenML/KittenTTS-orange.svg?style=for-the-badge)](https://github.com/KittenML/KittenTTS)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg?style=for-the-badge)](https://www.docker.com/)
[![Web UI](https://img.shields.io/badge/Web_UI-Included-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](#)
[![CUDA Compatible](https://img.shields.io/badge/NVIDIA_CUDA-Compatible-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-zone)
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
*   **True GPU Acceleration** for NVIDIA GPUs, a feature not present in the original implementation.
*   **Large Text Handling & Audiobook Generation:** Intelligently splits long texts into manageable chunks, processes them sequentially, and seamlessly concatenates the audio. Perfect for creating complete audiobooks.
*   **A flexible, dual-API system** including a simple endpoint and an OpenAI-compatible endpoint for easy integration.
*   **Curated High-Quality Voices:** A fixed list of 8 ready-to-use synthetic voices for consistent and reliable output.
*   **Cross-platform support** for Windows and Linux, with clear setup instructions.
*   **Docker support** for easy, reproducible containerized deployment.

## 🔥 Groundbreaking GPU Acceleration

A standout feature of this server is the implementation of **high-performance GPU acceleration**, a capability not available in the original KittenTTS project. While the base model is CPU-only, this server unlocks the full potential of your hardware.

*   **Optimized ONNX Runtime Pipeline:** We leverage `onnxruntime-gpu` to move the entire inference process to your NVIDIA graphics card.
*   **Eliminated I/O Bottlenecks:** The server uses advanced **I/O Binding**. This technique pre-allocates memory directly on the GPU for both model inputs and outputs, drastically reducing the latency caused by copying data between system RAM and the GPU's VRAM.
*   **True Performance Gains:** This isn't just running the model on the GPU; it's an optimized pipeline designed to minimize latency and maximize throughput, making real-time generation significantly faster than on CPU.

This enhancement transforms KittenTTS from a lightweight-but-modest engine into a high-speed synthesis powerhouse.

## ✨ Key Features of This Server

*   **🚀 Ultra-Lightweight Model:** Powered by the `KittenTTS` ONNX model, which is under 25MB.
*   ⚡ **True GPU Acceleration:** Full support for **NVIDIA (CUDA)** via an optimized `onnxruntime-gpu` pipeline with I/O Binding for maximum performance.
*   **📚 Large Text & Audiobook Generation:**
    *   Automatically handles long texts by intelligently splitting them based on sentence boundaries.
    *   Processes each chunk individually and seamlessly concatenates the resulting audio.
    *   **Ideal for audiobooks** - paste entire books and get professional-quality audio.
*   **🖥️ Modern Web Interface:**
    *   Intuitive UI for text input, voice selection, and parameter adjustment.
    *   Real-time waveform visualization of generated audio.
*   **🎤 8 High-Quality Voices:**
    *   Utilizes the 8 curated, built-in voices from the KittenTTS model (4 male, 4 female).
    *   Easily selectable via a UI dropdown menu.
*   **⚙️ Dual API Endpoints:**
    *   A primary `/tts` endpoint offering full control over all generation parameters.
    *   An OpenAI-compatible `/v1/audio/speech` endpoint for seamless integration into existing workflows.
*   **🔧 Easy Configuration:**
    *   All settings are managed through a single `config.yaml` file.
    *   The server automatically creates a default config on the first run.
*   **💾 UI State Persistence:** The web interface remembers your last-used text, voice, and settings to streamline your workflow.
*   **🐳 Docker Support:** Easy, reproducible deployment for both CPU and GPU via Docker Compose.

## 🔩 System Prerequisites

*   **Operating System:** Windows 10/11 (64-bit) or Linux (Debian/Ubuntu recommended).
*   **Python:** Version 3.10 or later.
*   **Git:** For cloning the repository.
*   **eSpeak NG:** This is a **required** dependency for text phonemization.
    *   **Windows:** See installation guide below.
    *   **Linux:** `sudo apt install espeak-ng`
*   **(For GPU Acceleration):**
    *   An **NVIDIA GPU** with CUDA support.
*   **(For Linux Only):**
    *   `libsndfile1`: Audio library needed by `soundfile`. Install via `sudo apt install libsndfile1`.
    *   `ffmpeg`: For robust audio operations. Install via `sudo apt install ffmpeg`.

## 💻 Installation and Setup

This project uses specific dependency files and a clear process to ensure a smooth, one-command installation for your hardware.

**1. Clone the Repository**
```bash
git clone https://github.com/devnen/Kitten-TTS-Server.git
cd Kitten-TTS-Server
```

**2. Create and Activate a Python Virtual Environment**
This is crucial to avoid conflicts with other Python projects.

*   **Windows (PowerShell):**
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
    If you see an error about execution policies, run:
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` and try activating again.

*   **Linux (Bash):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    Your command prompt should now start with `(venv)`.

**3. Install eSpeak NG (Required)**

*   **Windows:**
    1.  Download the installer from the [eSpeak NG Releases page](https://github.com/espeak-ng/espeak-ng/releases/latest). Look for the file named `espeak-ng-X.XX-x64.msi`.
    2.  Run the installer with default settings.
    3.  **Important:** Restart your terminal (PowerShell/CMD) after installation for the changes to take effect.

*   **Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update && sudo apt install -y espeak-ng
    ```

**4. Install Python Dependencies**

Choose one of the following paths based on your hardware.

---

### **Option 1: CPU-Only Installation**
This is the simplest path and works on any machine.

```bash
# Make sure your (venv) is active
pip install --upgrade pip
pip install -r requirements.txt
```

---

### **Option 2: NVIDIA GPU Installation (Recommended for Performance)**
This method ensures all necessary CUDA libraries are correctly installed within your virtual environment for a hassle-free setup.

```bash
# Make sure your (venv) is active
pip install --upgrade pip

# Step 1: Install the GPU-enabled ONNX Runtime
pip install onnxruntime-gpu

# Step 2: Install PyTorch with CUDA support. This command also brings the
# necessary CUDA and cuDNN .dll files that onnxruntime-gpu needs.
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121

# Step 3: Install the remaining dependencies from the requirements file
pip install -r requirements-nvidia.txt
```

**After installation, verify that PyTorch can see your GPU:**
```bash
python -c "import torch; print(f'PyTorch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'Device name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else None}')"
```
If `CUDA available:` shows `True`, your setup is correct!

---

## ▶️ Running the Server

**Important: First-Run Model Download**
The first time you start the server, it will automatically download the KittenTTS model (~25MB) from Hugging Face. This is a one-time process. Subsequent launches will be instant.

1.  **Activate the virtual environment** (if not already active).
    *   Windows: `.\venv\Scripts\activate`
    *   Linux: `source venv/bin/activate`

2.  **Run the server:**
    ```bash
    python server.py
    ```

3.  The server will start and automatically open the Web UI in your default browser.
    *   **Web UI:** `http://localhost:8005`
    *   **API Docs:** `http://localhost:8005/docs`

4.  **To stop the server:** Press `CTRL+C` in the terminal.

## 🐳 Docker Installation

Run Kitten-TTS-Server easily using Docker. The recommended method uses Docker Compose, which is pre-configured for both CPU and NVIDIA GPU deployment.

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/) installed.
*   [Docker Compose](https://docs.docker.com/compose/install/) installed (usually included with Docker Desktop).
*   **(For GPU acceleration)**
    *   An NVIDIA GPU.
    *   Up-to-date NVIDIA drivers for your host operating system.
    *   The [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed.

### Using Docker Compose (Recommended)

This method uses the provided `docker-compose.yml` files to automatically build the correct image and manage the container, volumes, and configuration.

**1. Clone the Repository**
```bash
git clone https://github.com/devnen/Kitten-TTS-Server.git
cd Kitten-TTS-Server
```

**2. Start the Container Based on Your Hardware**

Choose one of the following commands:

#### **For NVIDIA GPU (Recommended for Performance):**
The default `docker-compose.yml` is configured for NVIDIA GPUs. It will build the image with full CUDA support.

```bash
docker compose up -d --build
```

#### **For CPU-only:**
This uses a dedicated compose file that builds the image without GPU dependencies.

```bash
docker compose -f docker-compose-cpu.yml up -d --build
```

⭐ **Note:** The first time you run this, Docker will build the image and the server will download the KittenTTS model, which can take a few minutes. Subsequent starts will be much faster.

### 3. Access and Manage the Application

*   **Access the Web UI:** Open your browser to `http://localhost:8005`
*   **Access the API Docs:** `http://localhost:8005/docs`

*   **View Logs:**
    ```bash
    # For GPU or CPU version
    docker compose logs -f
    ```

*   **Stop the Container:**
    ```bash
    # This stops and removes the container but keeps your data volumes
    docker compose down
    ```

### How It Works

*   **Build-time Argument:** The `Dockerfile` uses a `RUNTIME` argument (`nvidia` or `cpu`) to conditionally install the correct Python packages, creating an optimized image for your hardware.
*   **Persistent Data:** The `docker-compose` files use Docker volumes to persist your important data on your host machine, even if the container is removed:
    *   `./config.yaml`: Your main server configuration file.
    *   `./outputs`: All generated audio files are saved here.
    *   `./logs`: Server log files for troubleshooting.
    *   `hf_cache` (Named Volume): Persists the downloaded Hugging Face models, saving significant time on rebuilds.

### Verify GPU Access (for NVIDIA users)

After starting the GPU container, you can verify that Docker and the application can see your graphics card.

```bash
# Check if the container can see the NVIDIA GPU
docker compose exec kitten-tts-server nvidia-smi

# Check if PyTorch inside the container can access CUDA
docker compose exec kitten-tts-server python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```
If `CUDA available:` prints `True`, your GPU setup is working correctly

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

All server settings are managed in the `config.yaml` file. It's created automatically on first launch if it doesn't exist.

**Key Settings:**
*   `server.host`, `server.port`: Network settings.
*   `tts_engine.device`: Set to `auto`, `cuda`, or `cpu`. The server will use your GPU if set to `auto` or `cuda` and a compatible environment is found.
*   `generation_defaults.speed`: Default speech speed (1.0 is normal).
*   `audio_output.format`: Default audio format (`wav`, `mp3`, `opus`).

## 🛠️ Troubleshooting

*   **Phonemizer / eSpeak Errors:**
    *   This is the most common issue. Ensure you have installed **eSpeak NG** correctly for your OS and **restarted your terminal** afterward. The server includes auto-detection logic for common install paths.
*   **GPU Not Used / Falls Back to CPU:**
    *   Follow the **NVIDIA GPU Installation** steps exactly. The most common cause is `torch` being installed without CUDA support.
    *   Run the verification command from the installation guide to confirm `torch.cuda.is_available()` is `True`.
*   **"No module named 'soundfile'" or Audio Errors on Linux:**
    *   The underlying system library is likely missing. Run `sudo apt install libsndfile1`.
*   **"Port already in use" Error:**
    *   Another application is using port 8005. Stop that application or change the port in `config.yaml` (e.g., `port: 8006`) and restart the server.

## 🙏 Acknowledgements & Credits

*   **Core Model:** This project is powered by the **[KittenTTS model](https://github.com/KittenML/KittenTTS)** created by **[KittenML](https://github.com/KittenML)**. Our work adds a high-performance server and UI layer on top of their excellent lightweight model.
*   **Core Libraries:** FastAPI, Uvicorn, ONNX Runtime, PyTorch, Hugging Face Hub, Phonemizer.
*   **UI Inspiration:** The UI/server architecture is inspired by our previous work on the [Chatterbox-TTS-Server](https://github.com/devnen/Chatterbox-TTS-Server).

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please feel free to open an issue or submit a pull request.

---
## ⭐ Star History

If you find this project useful, please consider giving it a star on GitHub!


[![Star History Chart](https://api.star-history.com/svg?repos=devnen/Kitten-TTS-Server&type=Date)](https://star-history.com/#devnen/Kitten-TTS-Server&Date)


