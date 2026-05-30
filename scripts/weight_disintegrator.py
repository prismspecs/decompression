import torch
import torch.nn as nn
import time
import copy

class SimpleGenerator(nn.Module):
    def __init__(self, input_size=10, hidden_size=20, output_size=10):
        super(SimpleGenerator, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

def disintegrate_weights(model, decay_rate=0.01):
    """
    Slightly deteriorate model weights and biases.
    """
    with torch.no_grad():
        for param in model.parameters():
            # Add small random noise and scale towards zero
            noise = torch.randn_like(param) * decay_rate
            param.mul_(1.0 - (decay_rate * 0.1)) # Slow decay
            param.add_(noise)

def live_generation_loop(iterations=50, decay_rate=0.05):
    print(f"Starting live disintegration loop for {iterations} iterations...")
    
    model = SimpleGenerator()
    input_data = torch.randn(1, 10)
    
    for i in range(iterations):
        # Generate output
        output = model(input_data)
        
        # Calculate some metric (e.g., mean of output) to show deterioration
        metric = output.abs().mean().item()
        print(f"Iteration {i+1:03d} | Output Mean: {metric:.6f}")
        
        # Disintegrate weights
        disintegrate_weights(model, decay_rate)
        
        # Wait a bit to simulate "live" process
        time.sleep(0.1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Weight Disintegrator - Deteriorate model weights live.")
    parser.add_argument("--iterations", type=int, default=50, help="Number of generation steps")
    parser.add_argument("--decay", type=float, default=0.05, help="Rate of weight deterioration")
    
    args = parser.parse_args()
    
    live_generation_loop(args.iterations, args.decay)
