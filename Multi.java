import java.util.Scanner;

public class Multi.java{
    
public static void multiplicar(){
    System.out.println("Opcion Multiplicar:\n");
    Scanner read = new Scanner(System.in);
    double num1;
    double num2;
    double calculo = 0;
try {
        System.out.println("Ingresa el primer valor a multiplicar");
        num1 = read.nextDouble();
        System.out.println("Ahora ingresame el segundo valor a multiplicar");
        num2 = read.nextDouble();
        calculo = num1 * num2;
        System.out.println("El resultado de la multiplicacion es: "+calculo);
        }
        catch (Exception e){
            System.out.println("Error, el valor ingresado no es valido o no estas ingresando un numero correctamente");
        }

    }
public static void main(String[] args) {
    
}
}