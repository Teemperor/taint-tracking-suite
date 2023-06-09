#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data = tainted & u32_0;
    EXPECT_NOT_TAINTED(data);
}