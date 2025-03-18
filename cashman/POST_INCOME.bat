@echo off 
curl -X POST -H "Content-Type: application/json" -d "{ \"amount\": 300.0, \"description\": \"loan payment\" }" http://localhost:5000/incomes
