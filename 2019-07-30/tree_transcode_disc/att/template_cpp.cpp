/**
 *  Template per soluzione in c++ per il problema tree_transcode_disc
 *
 *  Romeo Rizzi, 2019-07-28
 *
 */

#include <cassert>
#include <iostream>

using namespace std;

const int MAX_N = 1000000;
const int MAX_VAL = 10;

int n = 0, B0, input_type;
int in_tree[MAX_N], out_tree[MAX_N];

template <class T>
void print_array(T *v, int len) {
  for(int i = 0; i < len; i++)
    cout <<  v[i] << " ";
  cout << endl;
}

/*
void one2two(...) {
}

void two2one(...) {
}
*/

int main() {
    cin >> input_type;
    // leggere la sequenza che codifica l'albero in formato input_type

    int val;
    while (cin >> val)
      in_tree[n++] = val;

    //print test
    //print_array<int>(in_tree, n);
    
    // ottenere la codifica nell'altro formato
    /*
    if (input_type == 1)
      one2two( ... );

    else
      two2one( ... );
    */
    cout << 3-input_type << ' ';

    for(int i=0; i<n; i++)
      cout << out_tree[i] << ' ';
    cout << endl;
    
    return 0;
}

