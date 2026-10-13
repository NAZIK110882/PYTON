import pandas as pd
import numpy as np

# ==========================================
# БЛОК 0: Створення тестового датасету
# ==========================================
data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 102], # 102 - дублікат
    "Date": ["2023-10-01", "2023-10-02", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07", "2023-10-08", "2023-10-02"],
    "Category": ["Electronics", "Clothing", "Clothing", "Furniture", "Electronics", "Furniture", "Clothing", "Electronics", "Furniture", "Clothing"],
    "Price": [250.5, 45.0, np.nan, 120.0, 300.0, 150.0, 50.0, np.nan, 200.0, 45.0],
    "Quantity": [1, 3, 2, 1, 1, np.nan, 4, 1, 2, 3],
    "Customer_Age": [34, 28, 45, 50, 23, 38, 29, 41, 35, 28]
}

df_raw = pd.DataFrame(data)
df_raw.to_csv("sales_dataset.csv", index=False)
print("--- Файл sales_dataset.csv успішно створено! ---\n")


# ==========================================
# КРОК 3: Зчитування даних
# ==========================================
df = pd.read_csv("sales_dataset.csv")

print("--- Перші 5 рядків ---")
print(df.head(), "\n")

print("--- Останні 5 рядків ---")
print(df.tail(), "\n")

print(f"Кількість рядків і стовпців (shape): {df.shape}\n")

print("--- Інформація про датасет ---")
df.info()

print("\n--- Кількість унікальних значень ---")
print(df.nunique(), "\n")


# ==========================================
# КРОК 4: Очищення даних
# ==========================================
print("--- Пропущені значення до очищення ---")
print(df.isnull().sum(), "\n")

# Заповнюємо пропуски: ціну - середнім, кількість - медіаною
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# Видаляємо дублікати
print(f"Кількість дублікатів: {df.duplicated().sum()}")
df = df.drop_duplicates()

print("--- Дані після очищення пропусків ---")
print(df.isnull().sum(), "\n")


# ==========================================
# КРОК 5: Приведення типів
# ==========================================
df["Date"] = pd.to_datetime(df["Date"])
df["Category"] = df["Category"].astype("category")
df["Quantity"] = df["Quantity"].astype(int)

print("--- Типи даних після перетворення ---")
print(df.dtypes, "\n")


# ==========================================
# КРОК 6: Дослідницький аналіз (EDA)
# ==========================================
print("--- Описова статистика ---")
print(df.describe(), "\n")

print("--- Розподіл за категоріями ---")
print(df["Category"].value_counts(), "\n")

# Створюємо новий стовпець
df["Total_Sales"] = df["Price"] * df["Quantity"]


# ==========================================
# КРОК 7: Фільтрація та сортування
# ==========================================
print("--- Фільтрація (Лише Електроніка) ---")
print(df[df["Category"] == "Electronics"], "\n")

print("--- Фільтрація (Вік > 30 ТА Загальна сума > 200) ---")
print(df[(df["Customer_Age"] > 30) & (df["Total_Sales"] > 200)], "\n")

print("--- Сортування (За категорією та сумою) ---")
print(df.sort_values(by=["Category", "Total_Sales"], ascending=[True, False]).head(), "\n")


# ==========================================
# КРОК 8: Групування та агрегація
# ==========================================
print("--- Групування за категорією ---")
grouped_df = df.groupby("Category")["Total_Sales"].agg(["count", "sum", "mean", "min", "max"]).reset_index()
grouped_df.columns = ["Категорія", "К-ть продажів", "Загальна каса", "Середній чек", "Мін. чек", "Макс. чек"]
print(grouped_df, "\n")


# ==========================================
# КРОК 9: Збереження результатів
# ==========================================
df.to_csv("cleaned_sales_dataset.csv", index=False)
grouped_df.to_csv("category_sales_summary.csv", index=False)

print("--- Збереження завершено! ---")
print("Файли 'cleaned_sales_dataset.csv' та 'category_sales_summary.csv' створено у папці з проєктом.")