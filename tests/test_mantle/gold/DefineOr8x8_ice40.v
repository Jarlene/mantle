module Or8 (input [7:0] I, output  O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst0 (.I0(1'b0), .I1(I[0]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst1 (.I0(inst0_O), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst2 (.I0(inst1_O), .I1(I[2]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst3 (.I0(inst2_O), .I1(I[3]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst4 (.I0(inst3_O), .I1(I[4]), .I2(1'b0), .I3(1'b0), .O(inst4_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst5 (.I0(inst4_O), .I1(I[5]), .I2(1'b0), .I3(1'b0), .O(inst5_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst6 (.I0(inst5_O), .I1(I[6]), .I2(1'b0), .I3(1'b0), .O(inst6_O));
SB_LUT4 #(.LUT_INIT(16'hEEEE)) inst7 (.I0(inst6_O), .I1(I[7]), .I2(1'b0), .I3(1'b0), .O(inst7_O));
assign O = inst7_O;
endmodule

module Or8x8 (input [7:0] I0, input [7:0] I1, input [7:0] I2, input [7:0] I3, input [7:0] I4, input [7:0] I5, input [7:0] I6, input [7:0] I7, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Or8 inst0 (.I({I7[0],I6[0],I5[0],I4[0],I3[0],I2[0],I1[0],I0[0]}), .O(inst0_O));
Or8 inst1 (.I({I7[1],I6[1],I5[1],I4[1],I3[1],I2[1],I1[1],I0[1]}), .O(inst1_O));
Or8 inst2 (.I({I7[2],I6[2],I5[2],I4[2],I3[2],I2[2],I1[2],I0[2]}), .O(inst2_O));
Or8 inst3 (.I({I7[3],I6[3],I5[3],I4[3],I3[3],I2[3],I1[3],I0[3]}), .O(inst3_O));
Or8 inst4 (.I({I7[4],I6[4],I5[4],I4[4],I3[4],I2[4],I1[4],I0[4]}), .O(inst4_O));
Or8 inst5 (.I({I7[5],I6[5],I5[5],I4[5],I3[5],I2[5],I1[5],I0[5]}), .O(inst5_O));
Or8 inst6 (.I({I7[6],I6[6],I5[6],I4[6],I3[6],I2[6],I1[6],I0[6]}), .O(inst6_O));
Or8 inst7 (.I({I7[7],I6[7],I5[7],I4[7],I3[7],I2[7],I1[7],I0[7]}), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

