
package main;

import java.util.ArrayList;
import java.util.List;

public class Main5 {
    public static List<List<Integer>> generarSubconjuntos(List<Integer> conjunto) {
        List<List<Integer>> subconjuntos = new ArrayList<>();
        subconjuntos.add(new ArrayList<>());  // Inicializa con el conjunto vacío

        for (int elemento : conjunto) {
            List<List<Integer>> nuevosSubconjuntos = new ArrayList<>();
            for (List<Integer> subconjunto : subconjuntos) {
                List<Integer> nuevoSubconjunto = new ArrayList<>(subconjunto);  // Crea una copia del subconjunto actual
                nuevoSubconjunto.add(elemento);  // Agrega el elemento actual al nuevo subconjunto
                nuevosSubconjuntos.add(nuevoSubconjunto);  // Agrega el nuevo subconjunto a la lista de nuevos subconjuntos
            }
            subconjuntos.addAll(nuevosSubconjuntos);  // Agrega todos los nuevos subconjuntos a la lista de subconjuntos
        }
        return subconjuntos;
    }

    public static void main(String[] args) {
        List<Integer> conjunto = List.of(1, 2, 3);
        List<List<Integer>> subconjuntos = generarSubconjuntos(conjunto);
        System.out.println("Subconjuntos: " + subconjuntos);
    }
}
