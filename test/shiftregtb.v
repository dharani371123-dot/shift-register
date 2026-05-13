`timescale 1ns/1ps

module tb_shift_register;

reg clk;
reg reset;
reg serial_in;
wire [3:0] q;

shift_register uut (
    .clk(clk),
    .reset(reset),
    .serial_in(serial_in),
    .q(q)
);

always #5 clk = ~clk;

initial
begin
    clk = 0;
    reset = 1;
    serial_in = 0;

    #10 reset = 0;

    #10 serial_in = 1;
    #10 serial_in = 0;
    #10 serial_in = 1;
    #10 serial_in = 1;

    #50 $finish;
end
initial begin
$fsdbDumpfile("shiftreg.fsdb");
$fsdbDumpvars(0,tb_shift_register);
end
endmodule

