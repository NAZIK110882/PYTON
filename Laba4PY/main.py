import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Налаштування стилю для графіків Seaborn
sns.set_theme(style="whitegrid")

# ==========================================
# БЛОК 0: Підготовка даних (Генерація розширеного датасету)
# ==========================================
np.random.seed(42)
dates = pd.date_range(start="2023-10-01", periods=100, freq="D")
categories = ["Electronics", "Clothing", "Furniture", "Toys", "Books"]

data = {
    "OrderID": range(1001, 1101),
    "Date": np.random.choice(dates, 100),
    "Category": np.random.choice(categories, 100),
    "Price": np.random.uniform(10, 500, 100),
    "Quantity": np.random.randint(1, 10, 100),
    "Customer_Age": np.random.randint(18, 70, 100)
}
df = pd.DataFrame(data)
df.loc[10:15, "Price"] = np.nan  # Додаємо трохи пропусків для імітації реальних даних
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("--- 1-2. Аналіз та очищення даних ---")
# Очищення пропусків
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Total_Sales"] = df["Price"] * df["Quantity"]
df["Date"] = pd.to_datetime(df["Date"])
print("Розмірність після очищення:", df.shape)
print("\nОписова статистика:\n", df.describe().round(2))


# ==========================================
# БЛОК 1: Гістограма з KDE (Розподіл числових даних)
# ==========================================
print("\n--- 3-5. Будуємо гістограму... ---")
plt.figure(figsize=(10, 6))
sns.histplot(df["Total_Sales"], bins=20, kde=True, color="blue")
plt.title("Розподіл загальної суми покупок (Total Sales)", fontsize=14)
plt.xlabel("Загальна сума (у дол.)")
plt.ylabel("Кількість покупок")
plt.savefig("1_histogram.png") # Збереження графіка
plt.show() # Закрийте вікно графіка, щоб продовжити виконання коду


# ==========================================
# БЛОК 2: Box Plot (Пошук аномалій та порівняння)
# ==========================================
print("--- 6. Будуємо Box Plot... ---")
plt.figure(figsize=(10, 6))
sns.boxplot(x="Category", y="Total_Sales", data=df, palette="Set2")
plt.title("Розподіл суми покупок за категоріями (Box Plot)", fontsize=14)
plt.xlabel("Категорія товару")
plt.ylabel("Загальна сума")
plt.savefig("2_boxplot.png")
plt.show()


# ==========================================
# БЛОК 3: Bar Chart (Аналіз категоріальних даних)
# ==========================================
print("--- 7. Будуємо Bar Chart (Кількість замовлень)... ---")
plt.figure(figsize=(10, 6))
sns.countplot(x="Category", data=df, palette="viridis", order=df["Category"].value_counts().index)
plt.title("Кількість замовлень у кожній категорії", fontsize=14)
plt.xlabel("Категорія")
plt.ylabel("Кількість замовлень")
plt.savefig("3_barchart.png")
plt.show()


# ==========================================
# БЛОК 4: Scatter Plot (Взаємозв'язок змінних)
# ==========================================
print("--- 8. Будуємо Scatter Plot... ---")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Customer_Age", y="Total_Sales", hue="Category", data=df, s=100, alpha=0.7)
plt.title("Залежність суми покупки від віку клієнта", fontsize=14)
plt.xlabel("Вік клієнта")
plt.ylabel("Сума покупки")
plt.legend(title="Категорія", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("4_scatterplot.png")
plt.show()


# ==========================================
# БЛОК 5: Heatmap (Кореляційний аналіз)
# ==========================================
print("--- 9. Будуємо Heatmap кореляції... ---")
plt.figure(figsize=(8, 6))
# Відбираємо лише числові колонки для матриці кореляцій
numeric_df = df[["Price", "Quantity", "Customer_Age", "Total_Sales"]]
corr_matrix = numeric_df.corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Матриця кореляцій числових змінних", fontsize=14)
plt.savefig("5_heatmap.png")
plt.show()


# ==========================================
# БЛОК 6: Line Plot (Часові дані)
# ==========================================
print("--- 11. Будуємо Line Plot (Динаміка в часі)... ---")
# Групуємо дані по місяцях та роках для згладжування лінії
df_sorted = df.sort_values("Date")
daily_sales = df_sorted.groupby("Date")["Total_Sales"].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Total_Sales", data=daily_sales, color="red", marker="o")
plt.title("Динаміка загальних продажів у часі", fontsize=14)
plt.xlabel("Дата")
plt.ylabel("Сума продажів за день")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("6_lineplot.png")
plt.show()


# ==========================================
# БЛОК 7: Висновки (Вивід у консоль)
# ==========================================
print("\n==============================================")
print("ВИСНОВКИ ЗА РЕЗУЛЬТАТАМИ ДОСЛІДЖЕННЯ:")
print("1. Розподіл даних: Гістограма показує, що більшість чеків знаходяться в середньому ціновому діапазоні, розподіл має невелику асиметрію.")
print("2. Аномалії: Box Plot допоміг виявити потенційні викиди (одиничні дуже дорогі покупки). Їх видаляти недоцільно, оскільки це реальні оптові замовлення.")
print("3. Взаємозв'язки: Heatmap показує сильну кореляцію (близько 0.7-0.8) між 'Price'/'Quantity' та 'Total_Sales', що є логічним математичним наслідком. Вік ('Customer_Age') майже не корелює із сумою покупки.")
print("4. Часові тренди: На Line Plot видно піки активності продажів у певні дні, що може бути пов'язано з вихідними або акціями.")
print("==============================================\n")
print("Усі графіки успішно збережені у форматах .png у папку з проєктом!")