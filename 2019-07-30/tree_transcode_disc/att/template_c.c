/**
 *  Template per soluzione in c per il problema tree_transcode_disc
 *
 *  Romeo Rizzi, 2019-07-28
 *
 */

#include <assert.h>
#include <stdio.h>

#define MAX_N 1000000

int n, seq[MAX_N], input_type;

void print_array(int *v, int len) {
  for(int i = 0; i < len; i++)
      printf("%d ", v[i]);
  printf("\n");
}

int main() {
    scanf("%d", &input_type);

    // leggere la sequenza che codifica l'albero in formato input_type

    // ottenere la codifica nell'altro formato
    
    printf("%d\n", 3-input_type);

    // scrivere la nuova codifica dell'albero

    return 0;
}

