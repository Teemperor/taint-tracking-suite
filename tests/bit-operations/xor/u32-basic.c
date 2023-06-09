#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data = tainted ^ 0x1U;
    EXPECT_TAINTED(data);
}