#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data;
    memcpy(&data, &tainted, sizeof(data) - 1U);
    EXPECT_TAINTED(data);
}