# E-commerce Database Management with Etsy API Integration

## Project Overview  
This project is a **Python-based eCommerce database management system** using **Tkinter for UI** and **MySQL for backend storage**. It allows users to:  
- Add and manage **customers**  
- Display available **products**  
- Add selected products to a **cart**  
- **Automatically integrate Etsy API data** (pending approval)  

## Current Status  
🔹 **Etsy API approval is still pending.**  
🔹 Right now, the project works with **sample product data** stored in MySQL.  
🔹 The **Etsy API integration code is already included** but currently commented out.  
🔹 Once the API key is approved, it will be activated to **fetch real Etsy shop data** and update the database automatically.  

## Files Included  
- `Ecommerce_database_management.py` – Python script managing the eCommerce database and UI.  
- `ecommerce_database.sql` – MySQL dump file to set up the database.  
- `index.html` – Simple webpage for Etsy API integration description.  
- `README.md` – This documentation file.  

## How to Use  
1. **Set up MySQL Database:**  
   - Import `ecommerce_database.sql` into MySQL.  
   - Ensure MySQL is running.  

2. **Run the Python Script:**  
   ```bash
   python Ecommerce_database_management.py
