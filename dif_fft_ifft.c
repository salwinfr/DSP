#include <stdio.h>
#include <math.h>
#include <complex.h>
#define M_PI 3.14159265358979323846
void print_complex(double complex c) {
    if (cimag(c) >= 0) {
        printf("%.6f + %.6fi\n", creal(c), cimag(c));
    } else {
        printf("%.6f - %.6fi\n", creal(c), -cimag(c));
    }
}

double complex twiddle_factor(int N) {
    double angle = 2 * M_PI / N;
    return cos(angle) - I * sin(angle);
}

double complex twiddle_factor_2(int N) {
    double angle = 2 * M_PI / N;
    return cos(angle) + I * sin(angle);
}

void bit_reverse(double complex *x, int N) {
    int i, j, k;
    double complex temp;
    for (i = 1, j = 0; i < N; i++) {
        for (k = N >> 1; k > (j ^= k); k >>= 1);
        if (i < j) {
            temp = x[i];
            x[i] = x[j];
            x[j] = temp;
        }
    }
}

void dif_fft(double complex *x, int N) {
    
    int s = log2(N);

    for (s; s >= 1; s--) { // Outer loop: stages
        int m = 1 << s; // m = 2^s
        int m2 = m >> 1; // m2 = m / 2
        double complex w_m = twiddle_factor(m); // Twiddle factor for the current stage
        for (int k = 0; k < N; k += m) { // Middle loop: groups
            double complex w = 1.0 + 0.0 * I; // Initialize w to 1
            for (int j = 0; j < m2; j++) { // Inner loop: butterflies
                double complex u = x[k + j]; // First half
                double complex t = x[k + j + m2]; // Second half
                x[k + j] = u + t; // Combine first and second half
                x[k + j + m2] = (u - t) * w; // Apply twiddle factor to the second half
                w *= w_m; // Update w for the next butterfly
            }
        }
    }
    bit_reverse(x, N); // Bit-reverse the output
}

void dif_ifft(double complex *x, int N) {

    int s = log2(N);
    for (; s >= 1; s--) { // Outer loop: stages
        int m = 1 << s; // m = 2^s
        int m2 = m >> 1; // m2 = m / 2
        double complex w_m = twiddle_factor_2(m); // Twiddle factor for the current stage
        for (int k = 0; k < N; k += m) { // Middle loop: groups
            double complex w = 1.0 + 0.0 * I; // Initialize w to 1
            for (int j = 0; j < m2; j++) { // Inner loop: butterflies
                double complex u = x[k + j]; // First half
                double complex t = x[k + j + m2]; // Second half
                x[k + j] = u + t; // Combine first and second half
                x[k + j + m2] = (u - t) * w; // Apply twiddle factor to the second half
                w *= w_m; // Update w for the next butterfly
            }
        }
    }
    bit_reverse(x, N); // Bit-reverse the output

    for (int i = 0; i < N; i++) {
        x[i] /= N;
    }
}

int main() {
    int N = 8;
    double complex x[8] = {0.0 + 0.0 * I, 1.0 + 0.0 * I, 2.0 + 0.0 * I, 3.0 + 0.0 * I, 4.0 + 0.0 * I, 5.0 + 0.0 * I, 6.0 + 0.0 * I, 7.0 + 0.0 * I};
    
    // Perform FFT
    dif_fft(x, N);
    dif_ifft(x, N);
    for (int i = 0; i < N; i++) {
        print_complex(x[i]);
    }
    
    return 0;
}