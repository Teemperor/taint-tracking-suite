#include "taint-decls.h"

void test(unsigned tainted);
int main(int argc, char **argv) {
    unsigned test_data = 0;
    taintData(&test_data, sizeof(test_data));
    test(test_data);
}