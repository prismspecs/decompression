# Decompression Analysis Tools

A forensic tool designed to expose the "invisible forms" of digital compression.

## Tools

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

## Installation

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

## Background & Feasibility

### The Invisible Image
Video compression is not merely a reduction in file size; it is a complex re-construction of time and space. By visualizing motion vectors and macroblocks, we move from the *represented* image to the *operational* image—the mathematical scaffolding that makes digital video possible.

## License
This project is released under the MIT License.
