# ── Java Maven ──
FROM maven:3.9-eclipse-temurin-21 AS builder
WORKDIR /app
COPY pom.xml ./
RUN mvn dependency:go-offline -B || true
COPY src ./src
RUN mvn clean package -DskipTests -B

FROM eclipse-temurin:21-jre
WORKDIR /app
ENV PORT=8080
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/actuator/health || \
        curl -f http://localhost:8080/ || exit 1
CMD ["java", "-jar", "app.jar"]
