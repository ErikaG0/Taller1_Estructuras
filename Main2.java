
package main;

import java.util.ArrayList;
import java.util.List;

public class Main2 {
    public static List<Pair> miAlgoritmo(int n) {
        List<Pair> pares = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                pares.add(new Pair(i, j));
            }
        }
        return pares;
    }

    public static void main(String[] args) {
        List<Pair> resultado = miAlgoritmo(1000);
        for (Pair par : resultado) {
            System.out.println(par.first + ", " + par.second);
        }
    }

    static class Pair {
        int first;
        int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
}
