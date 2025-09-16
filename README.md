# Formal Verification of Solana's Alpenglow Consensus Protocol

[![TLA+](https://img.shields.io/badge/spec-TLA%2B-blue)](https://lamport.azurewebsites.net/tla/tla.html)  
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)

This repository contains a **formal verification** of Solana’s next-generation consensus protocol, **Alpenglow**, using **TLA+** and the **TLC model checker**. The goal is to provide machine-checkable proofs for Alpenglow’s claimed **safety, liveness, and resilience** properties.

---

## 📖 Overview

**Alpenglow** is a proposed consensus upgrade for Solana designed to achieve:

- ⚡ **100x faster finalization** (100–150ms)  
- 🔀 **Dual-path consensus (Votor)**:  
  - *Fast path* with ≥80% stake  
  - *Conservative path* with ≥60% stake  
- 📡 **Optimized block propagation (Rotor)**: Erasure-coded, single-hop distribution  
- 🛡️ **“20+20” resilience**: Tolerates up to 20% Byzantine nodes plus 20% crashed/offline nodes  

While the whitepaper provides strong mathematical arguments, this project complements it with **formal, model-checked guarantees**.

---

## 🏗️ Project Structure

    alpenglow-formal-verification/
    ├── spec/                  # TLA+ specifications
    │   ├── Alpenglow_Common.tla    # Common types and constants
    │   ├── Votor.tla               # Dual-path voting logic
    │   ├── Rotor.tla               # Erasure-coded block propagation
    │   └── Alpenglow_Main.tla      # Main protocol specification
    │
    ├── properties/            # Property definitions
    │   ├── Safety.tla         # Safety invariants
    │   ├── Liveness.tla       # Liveness properties
    │   └── Resilience.cfg     # Resilience test configuration
    │
    ├── models/                # TLC model configurations
    │   ├── small_model.cfg    # 4-node exhaustive model
    │   ├── large_model.cfg    # 20-node statistical model
    │   └── results/           # Model checking results
    │
    ├── scripts/               # Automation utilities
    │   └── run_tlc.py         # Python wrapper for TLC
    │
    └── docs/                  # Documentation
        ├── Technical_Report.md     # Detailed verification report
        └── video-walkthrough.md   # Walkthrough script

---

## 🚀 Getting Started

### Prerequisites
- Java Runtime Environment (JRE) for **TLC**
- Python 3.x (for automation scripts)
- [TLA+ Toolbox](https://lamport.azurewebsites.net/tla/toolbox.html) *(optional, for editing)*

### Running Verification

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/alpenglow-formal-verification.git
   cd alpenglow-formal-verification
Download TLC

bash
Copy code
wget https://github.com/tlaplus/tlaplus/releases/download/v1.8.0/tla2tools.jar
Run verification (small model example)

bash
Copy code
python scripts/run_tlc.py --model models/small_model.cfg
🔬 Verification Results
| Property                            | Status     | Notes                                                     |
| ----------------------------------- | ---------- | --------------------------------------------------------- |
| Safety: No conflicting finalization | ✅ Verified | Holds under ≤20% Byzantine stake                          |
| Safety: Chain consistency           | ✅ Verified | Honest nodes agree on finalized chain                     |
| Safety: Certificate uniqueness      | ✅ Verified | No equivocation possible                                  |
| Liveness: Progress                  | ⚠️ Partial | Holds with >60% responsive stake, fails during partitions |
| Liveness: Fast path completion      | ✅ Verified | Completes in one round with >80% responsive stake         |
| Resilience: 20+20 tolerance         | ✅ Verified | Safety maintained under advertised conditions             |


📋 Key Theorems Verified
No two conflicting blocks can be finalized in the same slot

Chain consistency under ≤20% Byzantine stake

Certificate uniqueness (no equivocation)

Progress under partial synchrony with >60% honest stake

Fast-path finalization in one round with >80% stake

Bounded finalization time: min(δ₈₀%, 2δ₆₀%)

👥 Contributing
Contributions are welcome! You can:

Report issues or bugs

Suggest model improvements

Add new properties or specifications

Improve documentation

This project is licensed under Apache 2.0.

🔗 References
Solana Alpenglow Whitepaper

TLA+ Official Website

Practical TLA+ (Hillel Wayne)

📧 Contact
For questions or discussion, please open an issue.
