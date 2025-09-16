#!/usr/bin/env python3
"""
Script to run TLC model checking on Alpenglow specifications
"""

import argparse
import subprocess
import os
import sys

def run_tlc(model_config, tla_file="spec/Alpenglow_Main.tla"):
    """Run TLC model checker with the given configuration"""
    
    # Check if Java is available
    try:
        subprocess.run(["java", "-version"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Java is required to run TLC")
        return False
    
    # Build command
    cmd = [
        "java", 
        "-cp", "tla2tools.jar", 
        "tlc2.TLC", 
        "-config", model_config,
        tla_file
    ]
    
    print(f"Running TLC with config: {model_config}")
    print(" ".join(cmd))
    
    # Run TLC
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        print("STDOUT:")
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"Error running TLC: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Run TLC model checking for Alpenglow")
    parser.add_argument("--model", "-m", required=True, help="Path to model configuration file")
    parser.add_argument("--spec", "-s", default="spec/Alpenglow_Main.tla", 
                       help="Path to TLA+ specification file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.model):
        print(f"Error: Model config file {args.model} does not exist")
        sys.exit(1)
        
    if not os.path.exists(args.spec):
        print(f"Error: TLA+ spec file {args.spec} does not exist")
        sys.exit(1)
    
    success = run_tlc(args.model, args.spec)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()