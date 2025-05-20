{
    assert(N >= 2);
    float input[N];   
    klee_make_symbolic(&input, sizeof(input), "input");

    FT L[N];
    int i;

    // read input
    for (i = N-1 ; i >= 0; i--){
        L[i] = input[i] / FLT_MAX * 100;
    }

    // The synthesis script will replace the FLAG line with a summation variation:
// REPLACE
    for (i = N-1 ; i > 0 ; i--)
    {
        L[i-1] += L[i];
    }

    return 0;
}
