# Decompression Analysis Tools

A suite of forensic and adversarial tools designed to expose the "invisible forms" of digital compression and the entropic decay of machine learning weights.

## 🛠 Tools

### 1. Video Forensic Visualizer
**Path:** `scripts/forensic_visualizer.py`

This tool utilizes the FFmpeg `codecview` filter to materialize the hidden decision-making process of video codecs. It extracts data directly from the bitstream to overlay structural metadata on the video frames.

*   **Motion Vectors (MV):** Visualizes the displacement arrows used for inter-frame prediction.
*   **Macroblocks (block):** Exposes the spatial partitioning of the frame (e.g., 16x16 or 8x8 blocks).
*   **Quantization Parameters (QP):** Tints the video based on the compression intensity applied to each block.

**Usage:**
```bash
python scripts/forensic_visualizer.py path/to/video.mp4 --mode mv --output forensic_mv.mp4
```

### 2. Weight Disintegrator
**Path:** `scripts/weight_disintegrator.py`

An adversarial simulation that intervenes in a model's internal state during generation. It mimics the "disintegration" of a neural network by iteratively applying Gaussian noise and scaling weights towards zero between inference steps.

*   **Entropic Decay:** Observe how the output mean and variance shift as the model loses its representative capacity.
*   **Live Intervention:** Designed to demonstrate the fragility of "weights and biases" as they are subjected to external deterioration.

**Usage:**
```bash
python scripts/weight_disintegrator.py --iterations 100 --decay 0.05
```

## 🏗 Installation

### Prerequisites
- **FFmpeg:** Required for video visualization. (e.g., `sudo apt install ffmpeg` or `brew install ffmpeg`)
- **Python 3.8+**

### Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd decompression
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Background & Feasibility

### The Invisible Image
Video compression is not merely a reduction in file size; it is a complex re-construction of time and space. By visualizing motion vectors and macroblocks, we move from the *represented* image to the *operational* image—the mathematical scaffolding that makes digital video possible.

### Adversarial Entropy
The "Weight Disintegrator" explores the concept of model "brain death" or entropic collapse. By deteriorating the weights live, we can witness the transition from structured logic to pure noise, highlighting the precarious nature of machine intelligence.

## 📜 License
This project is released under the MIT License.
