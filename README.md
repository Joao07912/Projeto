# 🧮 Calculadora Java + Maven

> Projeto **MAIS SIMPLES POSSÍVEL** para aprender Java com Maven

## 📁 O que tem no projeto:

```
calculadora/
├── src/main/java/
│   └── Calculadora.java    ← Seu programa Java
├── pom.xml                 ← Configuração do Maven
├── executar.bat           ← Script para rodar
└── README.md              ← Este arquivo
```

## 🎯 O que o programa faz:

- **Menu interativo** para escolher operação
- **Soma** dois números que você digita
- **Subtrai** dois números que você digita
- **Multiplica** dois números que você digita
- **Divide** dois números que você digita
- **Funciona com decimais** (1.5, 2.7, etc)
- **Tratamento de erros** (divisão por zero, entrada inválida)
- **Loop contínuo** - faça várias operações

## 🚀 Como executar:

### Opção 1: Script automático
```bash
executar.bat
```

### Opção 2: Comandos manuais
```bash
# Compilar
mvn compile

# Executar
mvn exec:java -Dexec.mainClass="Calculadora"

# Executar testes
mvn test
```

### Opção 3: Executar testes
```bash
executar-testes.bat
```

## 📚 O que você aprende:

1. **pom.xml** - Como configurar um projeto Maven
2. **Calculadora.java** - Como escrever código Java
3. **CalculadoraTest.java** - Como criar testes unitários
4. **mvn compile** - Como compilar com Maven
5. **mvn test** - Como executar testes
6. **mvn exec:java** - Como executar com Maven

## 🧪 Testes Unitários:

**8 testes criados:**
- ✅ **4 Testes Positivos**: Dados válidos que o sistema espera
- ❌ **4 Testes Negativos**: Dados inválidos que causam erros

**Executar testes:**
```bash
executar-testes.bat
# ou
mvn test
```

## 🔧 Pré-requisitos:

- Java 8 ou superior
- Maven instalado

---

**É isso! Projeto Java + Maven mais simples que existe! 🎉**