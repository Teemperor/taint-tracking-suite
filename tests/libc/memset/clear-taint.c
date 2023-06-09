#include "taint-tests.h"

void test(unsigned tainted) {
    memset(&tainted, 0, sizeof(tainted));
    EXPECT_NOT_TAINTED(tainted);
}