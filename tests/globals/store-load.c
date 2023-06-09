#include "taint-tests.h"

uint32_t global;

void test(unsigned tainted) {
    global = tainted;
    printf("do some stuff to avoid optimizations %p", &global);
    uint32_t read = global;
    EXPECT_TAINTED(read);
}