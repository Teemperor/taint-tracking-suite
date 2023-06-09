#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data;
    memset(&data, tainted, sizeof(data));
    EXPECT_TAINTED(data);
}