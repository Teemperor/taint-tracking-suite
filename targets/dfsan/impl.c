#include <sanitizer/dfsan_interface.h>


void taintData(void *ptr, size_t len) {
    dfsan_set_label(1, ptr, len);
}

int isTainted(void *ptr, size_t len) {
    for (size_t i = 0; i < len; ++i) {
        char data = *(char*)ptr;
        if (dfsan_get_label(data))
          return 1;
    }
    return 0;
}