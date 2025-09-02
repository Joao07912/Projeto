@echo off
echo 🧮 Calculadora Interativa Java + Maven
echo =====================================

echo.
echo 🔧 Configurando JDK...
set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-21.0.8.9-hotspot
set PATH=%JAVA_HOME%\bin;%PATH%

echo.
echo 📦 Compilando com Maven...
call mvn compile

if %errorlevel% neq 0 (
    echo ❌ Erro na compilação!
    pause
    exit /b 1
)

echo.
echo 🚀 Executando calculadora interativa...
call mvn exec:java -Dexec.mainClass="Calculadora"

echo.
pause