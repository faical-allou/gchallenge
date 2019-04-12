#include <stdio.h>
#include <string.h>

int main() {
  int cases = 1;
  //scanf("%d", &cases);

  for (int current =1 ; current <= cases; ++current) {
    int size = 3; 
    //scanf("%d", &size);
    
    char wall[3]="616";
    //scanf("%s", &wall);

    int half_size = (size+1)/2;

    int beauty_max = 0;
    int beauty = 0;
    int wall_int = 0;
    for (int id = 0; id <= half_size; ++id) {
      beauty = 0;
      for (int it = id; it <= id + half_size-1; ++it) {
        wall_int = wall[it] - '0';
        beauty = beauty + wall_int;
      }
      if (beauty >= beauty_max) beauty_max = beauty;
    
    };

    printf("Case #");
    printf("%d", current);
    printf(": ");
    printf("%d", beauty_max);
    printf("\n");
    
    fflush(stdout);
  };
  return 0;
}

