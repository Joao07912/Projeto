import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;

/**
 * Testes unitários para a Calculadora
 * 4 testes POSITIVOS (dados válidos esperados)
 * 4 testes NEGATIVOS (dados inválidos que causam erro)
 */
public class CalculadoraTest {
    
    private Calculadora calc;
    
    @Before
    public void setUp() {
        calc = new Calculadora();
    }
    
    // ========== TESTES POSITIVOS - Dados Válidos (4) ==========
    
    @Test
    public void testSomarDadosValidos() {
        // Teste 1: Soma com números inteiros válidos
        double resultado = calc.somar(10, 5);
        assertEquals(15.0, resultado, 0.001);
    }
    
    @Test
    public void testSubtrairDadosValidos() {
        // Teste 2: Subtração com números decimais válidos
        double resultado = calc.subtrair(20.5, 8.3);
        assertEquals(12.2, resultado, 0.001);
    }
    
    @Test
    public void testMultiplicarDadosValidos() {
        // Teste 3: Multiplicação com números válidos
        double resultado = calc.multiplicar(4, 3);
        assertEquals(12.0, resultado, 0.001);
    }
    
    @Test
    public void testDividirDadosValidos() {
        // Teste 4: Divisão com números válidos (não zero)
        double resultado = calc.dividir(15, 3);
        assertEquals(5.0, resultado, 0.001);
    }
    
    // ========== TESTES NEGATIVOS - Dados Inválidos (4) ==========
    
    @Test(expected = IllegalArgumentException.class)
    public void testDividirPorZero() {
        // Teste 5: Divisão por zero - ERRO esperado
        calc.dividir(10, 0);
    }
    
    @Test(expected = IllegalArgumentException.class)
    public void testDividirZeroPorZero() {
        // Teste 6: Zero dividido por zero - ERRO esperado
        calc.dividir(0, 0);
    }
    
    @Test
    public void testOperacaoComInfinito() {
        // Teste 7: Operação que resulta em infinito
        double resultado = calc.dividir(1, 0.0000001);
        assertTrue("Resultado deve ser muito grande", resultado > 1000000);
    }
    
    @Test
    public void testOperacaoComNumerosExtremos() {
        // Teste 8: Números muito grandes que podem causar overflow
        double num1 = Double.MAX_VALUE;
        double num2 = Double.MAX_VALUE;
        double resultado = calc.somar(num1, num2);
        assertTrue("Resultado deve ser infinito", Double.isInfinite(resultado));
    }
}