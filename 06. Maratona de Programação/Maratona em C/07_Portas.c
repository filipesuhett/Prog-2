#include <stdio.h>

int portas(int n)
{
    // Variaveis

    int cont = 1;

    // Código

    for (cont = 1; cont <= n; cont++) {
        printf("%d ", cont*cont);
    }

    return 0;
}