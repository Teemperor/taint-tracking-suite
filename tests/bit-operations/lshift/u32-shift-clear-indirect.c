#include "taint-tests.h"

void test(unsigned tainted) {
    tainted <<= u32_16;
    tainted <<= u32_16;
    EXPECT_NOT_TAINTED(tainted);
}