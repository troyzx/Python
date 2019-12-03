#include<stdio.h>
#include<time.h>

int main(){
    clock_t start, end;
    float elapse;
    long long int n=0, sum=0;
    start=clock();
    while(n<100000000){
        n++;
        sum+=n;
    }
    printf("%lld\n", sum);
    end=clock();
    elapse = (float)(end-start)/CLOCKS_PER_SEC;
    printf("%f", elapse);
}