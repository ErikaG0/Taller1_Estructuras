
package main;

public class Main4 {
    public static int busqueda(int[] arr, int elementoBuscado) {
        int izquierda = 0;
        int derecha = arr.length - 1;

        while (izquierda <= derecha) {
            int medio = (izquierda + derecha) / 2;
            int medioValor = arr[medio];

            if (medioValor == elementoBuscado) {
                return medio;
            } else if (elementoBuscado < medioValor) {
                derecha = medio - 1;
            } else {
                izquierda = medio + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int indice = busqueda(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9}, 7);
        System.out.println(indice);
    }
}
