# 🧮 Calculadora Java + Maven

> Projeto **simples e didático** para aprender Java com Maven e testes unitários

## 📋 Descrição do Projeto

A **Calculadora Java** é uma aplicação console interativa que demonstra conceitos fundamentais de desenvolvimento Java usando Maven como gerenciador de dependências. O projeto inclui operações matemáticas básicas, interface de usuário interativa e testes unitários completos.

### Principais Características:
- 🧮 **Calculadora Interativa**: Menu para escolher operações
- ➕ **Operações Básicas**: Soma, subtração, multiplicação e divisão
- 🔢 **Suporte a Decimais**: Trabalha com números inteiros e decimais
- 🔄 **Loop Contínuo**: Faça várias operações sem reiniciar
- ⚠️ **Tratamento de Erros**: Validação de entrada e divisão por zero
- 🧪 **Testes Unitários**: 8 testes (4 positivos + 4 negativos)

## 🛠️ Tecnologias Utilizadas

- **[Java 8+](https://adoptium.net/)** - Linguagem de programação
- **[Maven](https://maven.apache.org/)** - Gerenciador de dependências e build
- **[JUnit 4](https://junit.org/junit4/)** - Framework de testes unitários
- **Scanner** - Entrada de dados do usuário
- **Exception Handling** - Tratamento de erros

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Java JDK 8 ou superior** ([Download](https://adoptium.net/))
- **Maven** ([Download](https://maven.apache.org/download.cgi))

### Verificar instalação:
```bash
java -version
javac -version
mvn -version
```

## 🚀 Instalação e Execução

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd calculadora
```

### 2. Executar Aplicação

#### Opção 1: Script Automatizado (Recomendado)
```bash
executar-completo.bat
```

#### Opção 2: Comandos Manuais
```bash
# Compilar
mvn compile

# Executar
mvn exec:java -Dexec.mainClass="Calculadora"
```

### 3. Executar Testes
```bash
# Script de testes
executar-testes.bat

# Ou manualmente
mvn test
```

## 🎮 Como Usar a Calculadora

1. **Execute** o programa
2. **Escolha** uma operação (1-4):
   ```
   Escolha uma operação:
   1 - Somar (+)
   2 - Subtrair (-)
   3 - Multiplicar (*)
   4 - Dividir (/)
   0 - Sair
   ```
3. **Digite** o primeiro número
4. **Digite** o segundo número
5. **Veja** o resultado
6. **Repita** ou digite 0 para sair

## 📁 Estrutura do Projeto

```
calculadora/
├── src/
│   ├── main/java/
│   │   └── Calculadora.java          # Programa principal
│   └── test/java/
│       └── CalculadoraTest.java      # Testes unitários
├── pom.xml                           # Configuração Maven
├── executar-completo.bat            # Script para executar
├── executar-testes.bat              # Script para testes
├── .gitignore                       # Arquivos ignorados
└── README.md                        # Este arquivo
```

## 🧪 Testes Unitários

**8 testes implementados:**

### ✅ **Testes Positivos (Dados Válidos - 4):**
1. **testSomarDadosValidos** - Soma números inteiros (10 + 5 = 15)
2. **testSubtrairDadosValidos** - Subtração decimais (20.5 - 8.3 = 12.2)
3. **testMultiplicarDadosValidos** - Multiplicação normal (4 × 3 = 12)
4. **testDividirDadosValidos** - Divisão válida (15 ÷ 3 = 5)

### ❌ **Testes Negativos (Dados Inválidos - 4):**
5. **testDividirPorZero** - Divisão por zero → Erro esperado
6. **testDividirZeroPorZero** - Zero por zero → Erro esperado
7. **testOperacaoComInfinito** - Números que geram infinito
8. **testOperacaoComNumerosExtremos** - Overflow com números gigantes

**Executar testes:**
```bash
executar-testes.bat
# ou
mvn test
```

## 📚 O que você aprende:

1. **pom.xml** - Configuração de projetos Maven
2. **Calculadora.java** - Programação Java básica
3. **CalculadoraTest.java** - Testes unitários com JUnit
4. **Scanner** - Entrada de dados do usuário
5. **Exception Handling** - Tratamento de erros
6. **mvn compile** - Compilação com Maven
7. **mvn test** - Execução de testes
8. **mvn exec:java** - Execução de programas

## 🔧 Comandos Maven Úteis

```bash
# Limpar e compilar
mvn clean compile

# Executar testes
mvn test

# Gerar JAR
mvn package

# Executar JAR gerado
java -jar target/calculadora-1.0.jar
```

## 🎯 Funcionalidades

- ✅ **Operações básicas** (+ - * /)
- ✅ **Interface interativa** com menu
- ✅ **Números decimais** suportados
- ✅ **Validação de entrada** 
- ✅ **Tratamento de erros**
- ✅ **Loop contínuo**
- ✅ **Testes unitários completos**
- ✅ **Documentação detalhada**

## 🤝 Próximos Passos

Para expandir o projeto, você pode:

1. Adicionar mais operações (potência, raiz quadrada)
2. Implementar histórico de cálculos
3. Criar interface gráfica (Swing/JavaFX)
4. Adicionar mais testes de cobertura
5. Implementar calculadora científica

---

**Desenvolvido para aprender Java + Maven de forma prática! 🚀**