@echo off
echo 🧪 Executando Testes Unitários da Calculadora
echo =============================================

echo.
echo 🔧 Configurando JDK...
set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-21.0.8.9-hotspot
set PATH=%JAVA_HOME%\bin;%PATH%

echo.
echo 📦 Compilando projeto e testes...
call mvn compile test-compile

if %errorlevel% neq 0 (
    echo ❌ Erro na compilação!
    pause
    exit /b 1
)

echo.
echo 🧪 Executando testes...
call mvn test

echo.
echo ✅ Testes concluídos!
pause