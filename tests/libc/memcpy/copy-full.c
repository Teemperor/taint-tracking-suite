#include "taint-tests.h"

void test(unsigned tainted) {
    unsigned data;
    memcpy(&data, &tainted, sizeof(data));
    EXPECT_TAINTED(data);
}