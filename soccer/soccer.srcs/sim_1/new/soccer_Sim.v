`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/09/08 19:10:11
// Design Name: 
// Module Name: soccer_Sim
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module soccer_Sim(
    input SW0,SW15,
    output LED0,LED8,LED15);
    
    assign LED8=SW0&SW15;
    assign LED0=~SW15;
    assign LED15=~SW0; 
endmodule
