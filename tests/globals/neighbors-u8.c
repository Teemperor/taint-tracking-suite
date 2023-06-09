#include "taint-tests.h"

unsigned char global1;
unsigned char global2;

void test(unsigned tainted) {
    global1 = tainted;
    EXPECT_NOT_TAINTED(global2);
}