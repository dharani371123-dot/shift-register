import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def shift_register_test(dut):

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset
    dut.reset.value = 1
    dut.serial_in.value = 0

    for _ in range(2):
        await RisingEdge(dut.clk)

    dut.reset.value = 0
    dut._log.info("Reset released ✅")

    # Input sequence
    test_bits = [1, 0, 1, 1]

    expected = 0

    for bit in test_bits:

        dut.serial_in.value = bit

        await RisingEdge(dut.clk)

        expected = ((expected << 1) | bit) & 0xF

        q_val = int(dut.q.value)

        dut._log.info(
            f"Input={bit}, Output={q_val:04b}, Expected={expected:04b}"
        )

        assert q_val == expected, (
            f"Mismatch! Expected {expected:04b}, Got {q_val:04b}"
        )

    dut._log.info("TEST PASSED ✅")
