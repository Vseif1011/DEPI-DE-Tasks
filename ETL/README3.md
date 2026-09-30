# Text-to-SQL Project

## 🎯 Objective

Build a Text-to-SQL application using the Gemini API.

The application should allow the user to enter a question in natural language, convert it into a SQL query using Gemini, execute the query on a database, and display the result.

---

## 🔄 Project Flow

```text
User Question
      ↓
Gemini API
      ↓
SQL Query
      ↓
Database
      ↓
pd.read_sql()
      ↓
Output
```

---

## 🛠️ Requirements

You should use:

* Python
* Gemini API
* SQL Database
* Pandas
* `pd.read_sql()`

---

## 💡 Example

The user enters:

```text
Show me the top 5 customers by total sales.
```

Gemini should generate a SQL query such as:

```sql
SELECT TOP 5
    customer_id,
    SUM(total_amount) AS total_sales
FROM orders
GROUP BY customer_id
ORDER BY total_sales DESC;
```

Then execute the generated query using:

```python
df = pd.read_sql(query, connection)
```

Finally, display the result.

---

## 📋 Requirements

### 1. Database

Use Company_SD

```

### 2. Gemini API

Use the Gemini API to convert the user's question into SQL.

The prompt should include the database schema so Gemini knows the available tables and columns.

Example:

```text
Database Schema:

customers:
- SSN
- fname
- address

Convert the following question to SQL:

"Show the top 5 customers by total sales."
```

### 3. Execute SQL

Execute the generated SQL using Pandas:

```python
df = pd.read_sql(query, connection)
```

### 4. Display the Result

Display:

1. User question
2. Generated SQL query
3. Query result

Example:

```text
Question:
Show the top 5 customers by total sales.

SQL:
SELECT TOP 5 ...

Result:
customer_id | total_sales
------------|------------
101         | 25000
205         | 21000
...
```

---

## ⭐ Bonus — Flask Web App

Create a simple web application using:

* Flask
* HTML
* CSS

The page should contain:

```text
-----------------------------------
        Text to SQL
-----------------------------------

Ask your question:

[ Show top 5 customers by sales ]

          [ Generate ]

Generated SQL:

SELECT TOP 5 ...

Result:

| customer_id | total_sales |
|-------------|-------------|
| 101         | 25000       |
| 205         | 21000       |
-----------------------------------
```

---


## 🎯 Expected Result

The final application should be able to:

```text
Natural Language
       ↓
     Gemini
       ↓
    SQL Query
       ↓
   pd.read_sql()
       ↓
    DataFrame
       ↓
 Display Result
```
