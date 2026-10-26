# RISC-V RV32I Core Verification with UVM

A verification plan and Python architectural helper functions for checking an RV32I processor against a reference model such as Spike.

## Scope
- Integer ALU and immediate instructions.
- Branches, jumps, loads/stores, sign extension, and boundary cases.
- Directed tests and randomized instruction streams.
- Retirement-level comparison of PC, instruction, register writes, and memory effects.

## Contents
- `model/rv32i_helpers.py`: small arithmetic/sign-extension helpers with assertions.
- `docs/plan.md`: verification checklist.

## Setup
Run the helper checks with `python model/rv32i_helpers.py`. Full UVM verification requires a DUT, simulator with UVM, RISC-V toolchain, and simulator-specific integration scripts.

## Metrics
Track opcode and corner-case coverage, hazards, exceptions, and retirement mismatches. Do not claim ISA compliance or coverage until verified against an implemented DUT.