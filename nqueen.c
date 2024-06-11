#include<stdio.h>
int count=0, all_set, col_set;
void solver(int row, int ld, int rd) {
	if (row == all_set) {
        count += 1;
        return;
	}
    int available_positions = (~(row | ld | rd)) & col_set, position;

    while(available_positions){
		position = -available_positions & available_positions;
		available_positions ^= position;
		solver(row | position, (ld | position) << 1, (rd | position) >> 1);
	}
}

void main(){
	int n = 12;
	all_set = (1 << n) - 1;
	col_set = all_set;
	solver(0,0,0);
	printf("%d number of solutions were found\n",count);
	}
