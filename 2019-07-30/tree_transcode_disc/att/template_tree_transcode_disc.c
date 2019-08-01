#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 1000000

int n=0, seq[MAX_N], input_type;
FILE *input;
FILE *output;

void print_array(int *v, int len) {
  for(int i = 0; i < len; i++)
      printf("%d ", v[i]);
  printf("\n");
}

void parse_array(int *v, int *len, char *str){
    char *num=strtok(str," ");
    do{
        //v[(*len)++]=strtol(num,NULL,10);
        v[(*len)++]=atoi(num);
    }while((num=strtok(NULL, " "))!=NULL);
}


int main() {
    char str[MAX_N];
    input=fopen("input.txt", "r");
    output=fopen("output.txt", "w");
    
    fscanf(input, "%d", &input_type);
    
    // leggo l'array e ignoro la sua codifica
    fgets(str,MAX_N,input);
    parse_array(seq,&n,str);

    // ottenere la codifica nell'altro formato
    
    printf("%d\n", 3-input_type);

    // scrivere la nuova codifica dell'albero

    return 0;
}

