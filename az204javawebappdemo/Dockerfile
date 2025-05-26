# 1. Schritt: Wähle das Basis-Image
FROM maven:3-amazoncorretto-17 as build

# 2. Schritt: Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# 3. Schritt: Kopiere die POM-Datei (falls du Maven verwendest)
COPY pom.xml .

# 4. Schritt: Lade die Abhängigkeiten (dies ist optional, um den Cache zu nutzen und nicht immer die Abhängigkeiten neu zu laden)
RUN mvn dependency:go-offline

# 5. Schritt: Kopiere den Rest des Codes
COPY src /app/src

# 6. Schritt: Baue das Spring Boot Projekt mit Maven (du kannst auch Gradle verwenden, falls du es bevorzugst)
RUN mvn clean package -DskipTests

# 7. Schritt: Erstelle das endgültige Image mit einem kleineren Java-Image
FROM openjdk:17-jdk-slim

# 8. Schritt: Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# 9. Schritt: Kopiere die erstellte JAR-Datei aus dem Build-Image
COPY --from=build /app/target/*.jar app.jar

# 10. Schritt: Exponiere den Port, den die App verwendet
EXPOSE 8080

# 11. Schritt: Definiere den Befehl zum Starten der Anwendung
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
