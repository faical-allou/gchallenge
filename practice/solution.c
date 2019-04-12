#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main() {
  clock_t start, end;
  double cpu_time_used;

  start = clock();

  int cases = 1;
  scanf("%d", &cases);
  
  char *wall = malloc(sizeof(char)*5000000);
  int *wall_int = malloc(sizeof(int)*5000000);
  int beauty_max = 0;
  int beauty = 0;

  for (int current =1 ; current <= cases; ++current) {
    int size = 3; 
    scanf("%d", &size);
    
    scanf("%s", wall);

    for (int id = 0; id <= size-1; ++id) {
      wall_int[id] = wall[id] - '0';
    };

    int half_size = (size+1)/2;

    beauty_max =0;
    for (int id = 0; id <=size- half_size; ++id) {
      beauty = 0;
      for (int it = id; it <= id + half_size-1; ++it) {
        beauty = beauty + wall_int[it];
      };
      if (beauty >= beauty_max) beauty_max = beauty;
    
    };

    printf("Case #");
    printf("%d", current);
    printf(": ");
    printf("%d", beauty_max);
    printf("\n");
    
    fflush(stdout);
    
  };
    //end = clock();
    //cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    //printf("%f", cpu_time_used);
    //scanf("%s", cases);
  return 0;
}

