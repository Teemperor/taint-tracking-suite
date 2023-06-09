#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data = tainted & u32_2;
    unsigned data2 = data & u32_1;
    EXPECT_NOT_TAINTED(data2);
}