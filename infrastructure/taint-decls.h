#include "stdint.h"
#include "stdio.h"
#include "stdlib.h"

void taintData(void *ptr, size_t len);
int isTainted(void *ptr, size_t len);

#define EXPECT_TAINTED(TARGET) \
  if (!isTainted(&TARGET, sizeof(TARGET))) { \
    fprintf(stderr, "%s:%d: %s should have been tainted!\n", __FILE__, __LINE__, #TARGET); \
    exit(1); \
  }

#define EXPECT_NOT_TAINTED(TARGET) \
  if (isTainted(&TARGET, sizeof(TARGET))) { \
    fprintf(stderr, "%s:%d: %s should not have been tainted!\n", __FILE__, __LINE__, #TARGET); \
    exit(1); \
  }