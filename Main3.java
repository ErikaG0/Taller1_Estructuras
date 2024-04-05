
package main;

import java.util.Random;

public class Main3 {
    public static double operacionIntensivaMemoria(int n) throws InterruptedException {
        /* Operación que genera un gran uso de memoria temporalmente. */
        double[] granLista = new double[n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            granLista[i] = random.nextDouble();
        }
        Thread.sleep(1000); // Simulamos un procesamiento
        double suma = 0;
        for (double valor : granLista) {
            suma += valor;
        }
        return suma;
    }

    @SuppressWarnings("unused")
    public static void operacionIntensivaCPU(int n) throws InterruptedException {
        /* Operación que consume tiempo de CPU. */
        double contador = 0;
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            contador += random.nextDouble();
            Thread.sleep(10); // Añade un pequeño retardo para simular procesamiento
        }
    }

    public static void main(String[] args) throws InterruptedException {
        int n = 500000;
        for (int i = 0; i < 5; i++) {
            System.out.println("Pico " + (i + 1) + ": Operación intensiva en memoria");
            operacionIntensivaMemoria(n);
            System.out.println("Pico " + (i + 1) + ": Operación intensiva en CPU");
            operacionIntensivaCPU(100);
        }
    }
}
