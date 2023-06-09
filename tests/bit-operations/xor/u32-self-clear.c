#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data = tainted ^ tainted;
    EXPECT_NOT_TAINTED(data);
}