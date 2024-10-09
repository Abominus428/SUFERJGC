module soccer(
    input SW0,
    output LED0,
    input SW15,
    output LED15,
    output LED8
    );  
    assign LED0 = SW0;
    assign LED15 = SW15;
    assign LED8 = (SW0 & SW15);
endmodule