import subprocess
import argparse
import os

def visualize_video(input_path, output_path, mode='mv'):
    """
    Visualize internal video compression data using FFmpeg.
    
    Modes:
    - mv: Motion Vectors
    - block: Macroblock partitions
    - qp: Quantization Parameters
    """
    
    ffmpeg_cmd = [
        'ffmpeg',
        '-flags2', '+export_mvs', # Required for motion vectors
        '-i', input_path,
        '-vf', f'codecview={mode}=pf+bf+bb' if mode == 'mv' else f'codecview={mode}=1',
        '-y', # Overwrite output
        output_path
    ]
    
    print(f"Running command: {' '.join(ffmpeg_cmd)}")
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Successfully generated visualization: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running FFmpeg: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Please install FFmpeg to use this tool.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video Forensic Visualizer - Expose invisible compression data.")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("--output", default="output_visualization.mp4", help="Path to output video file")
    parser.add_argument("--mode", choices=['mv', 'block', 'qp'], default='mv', help="Visualization mode")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
    else:
        visualize_video(args.input, args.output, args.mode)
