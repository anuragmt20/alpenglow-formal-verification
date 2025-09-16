# Formal Verification of Solana's Alpenglow Consensus Protocol

This repository contains a formal verification of Solana's Alpenglow consensus protocol using TLA+.

## Overview

Alpenglow is Solana's consensus protocol upgrade that achieves:
- 100-150ms finalization (100x faster than current TowerBFT)
- Dual-path consensus (Votor) with fast (80% stake) and conservative (60% stake) finalization
- Optimized block propagation (Rotor) with erasure coding
- "20+20" resilience (tolerates 20% Byzantine + 20% crashed nodes)

## Project Structure

- `/spec` - TLA+ specifications of the protocol
- `/properties` - Safety, liveness, and resilience properties
- `/models` - TLC model configurations and results
- `/scripts` - Automation scripts for verification
- `/docs` - Technical report and documentation

## Getting Started

### Prerequisites
- Java Runtime Environment (for TLC model checker)
- TLA+ Toolbox (optional)

### Running Verification
1. Clone this repository
2. Run the verification script:
   ```bash
   python scripts/run_tlc.py --model models/small_model.cfg