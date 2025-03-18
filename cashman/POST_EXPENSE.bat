@echo off
curl -X POST -H "Content-Type: application/json" -d "{ \"amount\": 20, \"description\": \"lottery ticket\" }" http://localhost:5000/expenses
