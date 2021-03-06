module Add8_cout (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
wire [8:0] inst0_out;
coreir_add9 inst0 (.in0({1'b0,I0[7],I0[6],I0[5],I0[4],I0[3],I0[2],I0[1],I0[0]}), .in1({1'b0,I1[7],I1[6],I1[5],I1[4],I1[3],I1[2],I1[1],I1[0]}), .out(inst0_out));
assign O = {inst0_out[7],inst0_out[6],inst0_out[5],inst0_out[4],inst0_out[3],inst0_out[2],inst0_out[1],inst0_out[0]};
assign COUT = inst0_out[8];
endmodule

module _Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_out;
coreir_bitmux inst0 (.in0(I[0]), .in1(I[1]), .sel(S), .out(inst0_out));
assign O = inst0_out;
endmodule

module Mux2x8 (input [7:0] I0, input [7:0] I1, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
_Mux2 inst0 (.I({I1[0],I0[0]}), .S(S), .O(inst0_O));
_Mux2 inst1 (.I({I1[1],I0[1]}), .S(S), .O(inst1_O));
_Mux2 inst2 (.I({I1[2],I0[2]}), .S(S), .O(inst2_O));
_Mux2 inst3 (.I({I1[3],I0[3]}), .S(S), .O(inst3_O));
_Mux2 inst4 (.I({I1[4],I0[4]}), .S(S), .O(inst4_O));
_Mux2 inst5 (.I({I1[5],I0[5]}), .S(S), .O(inst5_O));
_Mux2 inst6 (.I({I1[6],I0[6]}), .S(S), .O(inst6_O));
_Mux2 inst7 (.I({I1[7],I0[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse (input  I, output  O, input  CLK);
wire [0:0] inst0_out;
coreir_reg_P #(.init(0)) inst0 (.in({I}), .clk(CLK), .out(inst0_out));
assign O = inst0_out[0];
endmodule

module Register8 (input [7:0] I, output [7:0] O, input  CLK);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst0 (.I(I[0]), .O(inst0_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst1 (.I(I[1]), .O(inst1_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst2 (.I(I[2]), .O(inst2_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst3 (.I(I[3]), .O(inst3_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst4 (.I(I[4]), .O(inst4_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst5 (.I(I[5]), .O(inst5_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst6 (.I(I[6]), .O(inst6_O), .CLK(CLK));
DFF_init0_has_ceFalse_has_resetFalse_has_async_resetFalse inst7 (.I(I[7]), .O(inst7_O), .CLK(CLK));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module CounterLoad8_COUT (input [7:0] DATA, input  LOAD, output [7:0] O, output  COUT, input  CLK);
wire [7:0] inst0_O;
wire  inst0_COUT;
wire [7:0] inst1_O;
wire [7:0] inst2_O;
Add8_cout inst0 (.I0(inst2_O), .I1({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Mux2x8 inst1 (.I0(inst0_O), .I1(DATA), .S(LOAD), .O(inst1_O));
Register8 inst2 (.I(inst1_O), .O(inst2_O), .CLK(CLK));
assign O = inst2_O;
assign COUT = inst0_COUT;
endmodule

