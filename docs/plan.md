# RV32I verification plan

- Decode legality and illegal-instruction behavior.
- ALU: add/sub, shifts, signed/unsigned comparisons, bitwise operations.
- Immediate formats: sign extension and boundary values.
- Branches: taken/not-taken, forward/backward offsets, alignment.
- JAL/JALR: link address and target calculation.
- Loads/stores: byte/half/word sign and zero extension, strobes, alignment policy.
- Dependencies: RAW hazards, forwarding, load-use stalls.
- Reset, exceptions, interrupts, and privilege behavior as implemented.
- Compare retirement trace against Spike or another trusted ISA model.
- Save seeds, tool versions, logs, and coverage database.
