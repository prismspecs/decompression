import subprocess
import argparse
import os
import tempfile

def visualize_video(input_path, output_path, mode='mv'):
    """
    Visualize internal video compression data using FFmpeg.
    
    Modes:
    - mv: Motion Vectors (Arrows)
    - mv_blobs: Motion Vectors + Prediction Residual Blobs
    """
    
    if mode == 'mv':
        vf_filter = 'codecview=mv=pf+bf+bb'
    elif mode == 'mv_blobs':
        vf_filter = 'tblend=all_mode=difference,codecview=mv=pf+bf+bb'
    else:
        vf_filter = 'codecview=mv=pf+bf+bb'
        
    ffmpeg_cmd = [
        'ffmpeg',
        '-flags2', '+export_mvs',
        '-i', input_path,
        '-vf', vf_filter,
        '-y', # Overwrite output
        output_path
    ]
    
    try:
        print(f"Running visualizer: {' '.join(ffmpeg_cmd)}")
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
    parser.add_argument("--mode", choices=['mv', 'mv_blobs'], default='mv_blobs', help="Visualization mode")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
    else:
        visualize_video(args.input, args.output, args.mode)
