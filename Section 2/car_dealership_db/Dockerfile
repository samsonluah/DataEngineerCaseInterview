FROM postgres:latest

# Set environment variables for the PostgreSQL instance
ENV POSTGRES_USER=dealership
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_DB=dealership_db

# Copy the DDL script that creates the tables
COPY create_db.sql /docker-entrypoint-initdb.d/