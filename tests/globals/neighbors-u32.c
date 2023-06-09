#include "taint-tests.h"

uint32_t global1;
unsigned char global2;

void test(unsigned tainted) {
    global1 = tainted;
    EXPECT_NOT_TAINTED(global2);
}