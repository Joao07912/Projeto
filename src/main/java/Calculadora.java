import java.util.Scanner;

/**
 * Calculadora interativa para demonstrar Java + Maven
 */
public class Calculadora {
    
    // Método para somar dois números
    public double somar(double a, double b) {
        return a + b;
    }
    
    // Método para subtrair dois números
    public double subtrair(double a, double b) {
        return a - b;
    }
    
    // Método para multiplicar dois números
    public double multiplicar(double a, double b) {
        return a * b;
    }
    
    // Método para dividir dois números
    public double dividir(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Não pode dividir por zero!");
        }
        return a / b;
    }
    
    // Método principal - executa quando roda o programa
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculadora calc = new Calculadora();
        
        System.out.println("🧮 Calculadora Interativa Java + Maven");
        System.out.println("======================================");
        
        while (true) {
            try {
                // Mostrar menu de operações
                System.out.println("\nEscolha uma operação:");
                System.out.println("1 - Somar (+)");
                System.out.println("2 - Subtrair (-)");
                System.out.println("3 - Multiplicar (*)");
                System.out.println("4 - Dividir (/)");
                System.out.println("0 - Sair");
                System.out.print("\nDigite sua opção: ");
                
                int opcao = scanner.nextInt();
                
                if (opcao == 0) {
                    System.out.println("\n👋 Obrigado por usar a calculadora!");
                    break;
                }
                
                if (opcao < 1 || opcao > 4) {
                    System.out.println("❌ Opção inválida! Tente novamente.");
                    continue;
                }
                
                // Pedir os números
                System.out.print("Digite o primeiro número: ");
                double num1 = scanner.nextDouble();
                
                System.out.print("Digite o segundo número: ");
                double num2 = scanner.nextDouble();
                
                // Executar operação escolhida
                double resultado = 0;
                String operacao = "";
                
                switch (opcao) {
                    case 1:
                        resultado = calc.somar(num1, num2);
                        operacao = "+";
                        break;
                    case 2:
                        resultado = calc.subtrair(num1, num2);
                        operacao = "-";
                        break;
                    case 3:
                        resultado = calc.multiplicar(num1, num2);
                        operacao = "*";
                        break;
                    case 4:
                        resultado = calc.dividir(num1, num2);
                        operacao = "/";
                        break;
                }
                
                // Mostrar resultado
                System.out.println("\n✅ Resultado: " + num1 + " " + operacao + " " + num2 + " = " + resultado);
                
            } catch (IllegalArgumentException e) {
                System.out.println("❌ Erro: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("❌ Entrada inválida! Digite apenas números.");
                scanner.nextLine(); // Limpar buffer
            }
        }
        
        scanner.close();
    }
}