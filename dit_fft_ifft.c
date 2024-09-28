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

void fft(double complex *x, int N) {
    bit_reverse(x, N);
    int i = 1;
    int S = 0;
    while (i != N) {
        i = i * 2;
        S += 1;
    }
    for (int s = 1; s <= S; s++) {
        int m = 1 << s;
        int m2 = m >> 1;
        double complex w_m = twiddle_factor(m);
        for (int k = 0; k < N; k += m) {
            double complex w = 1.0 + 0.0 * I;
            for (int j = 0; j < m2; j++) {
                double complex t = w * x[k + j + m2];
                double complex u = x[k + j];
                x[k + j] = u + t;
                x[k + j + m2] = u - t;
                w *= w_m;
            }
        }
    }
}

void ifft(double complex *x, int N) {
    bit_reverse(x, N);
    int i = 1;
    int S = 0;
    while (i != N) {
        i = i * 2;
        S += 1;
    }
    for (int s = 1; s <= S; s++) {
        int m = 1 << s;
        int m2 = m >> 1;
        double complex w_m = twiddle_factor_2(m);
        for (int k = 0; k < N; k += m) {
            double complex w = 1.0 + 0.0 * I;
            for (int j = 0; j < m2; j++) {
                double complex t = w * x[k + j + m2];
                double complex u = x[k + j];
                x[k + j] = u + t;
                x[k + j + m2] = u - t;
                w *= w_m;
            }
        }
    }
    for (int i = 0; i < N; i++) {
        x[i] /= N;
    }
}

int main() {
    int N = 8;
    double complex x[8] = {0.0 + 0.0 * I, 1.0 + 0.0 * I, 2.0 + 0.0 * I, 3.0 + 0.0 * I, 4.0 + 0.0 * I, 5.0 + 0.0 * I, 6.0 + 0.0 * I, 7.0 + 0.0 * I};
    
    // Perform FFT
    fft(x, N);
    ifft(x, N);
    for (int i = 0; i < N; i++) {
        print_complex(x[i]);
    }
    
    
    return 0;
}