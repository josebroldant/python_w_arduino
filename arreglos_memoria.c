#include <stdio.h>
#include <stdlib.h>
main(){
	int *a;
	a=(int*)malloc(sizeof(int)*5);
	for(int i=1;i<=5;i++){
	a[i]=i;
	}
	printf("%d\n", &a[1]);
	printf("%d\n", &a[4]);
	printf("%d\n", a[2]);
	printf("%d\n", a[3]);
	free(a);

}



