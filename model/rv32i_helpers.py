"""Small architectural helpers for RV32I reference tests."""
MASK32 = 0xFFFFFFFF

def u32(value: int) -> int:
    return value & MASK32

def s32(value: int) -> int:
    value &= MASK32
    return value - (1 << 32) if value & (1 << 31) else value

def sign_extend(value: int, bits: int) -> int:
    sign = 1 << (bits - 1)
    return (value & (sign - 1)) - (value & sign)

def add(a: int, b: int) -> int:
    return u32(a + b)

def sra(a: int, shamt: int) -> int:
    return u32(s32(a) >> (shamt & 0x1F))

def slt(a: int, b: int) -> int:
    return int(s32(a) < s32(b))

def sltu(a: int, b: int) -> int:
    return int(u32(a) < u32(b))

if __name__ == "__main__":
    assert add(0xFFFFFFFF, 1) == 0
    assert s32(0xFFFFFFFF) == -1
    assert sra(0x80000000, 1) == 0xC0000000
    assert slt(0xFFFFFFFF, 0) == 1
    assert sltu(0xFFFFFFFF, 0) == 0
    print("RV32I helper checks passed")
