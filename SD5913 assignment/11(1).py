import pandas as pd
import matplotlib.pyplot as plt

# 加载 CSV 文件
file_path = r'C:\Users\china\Desktop\data\latest_10min_wind.csv'
df = pd.read_csv(file_path)

# 清理列名中的空格
df.columns = df.columns.str.strip()

# 删除含有 NaN 的行，或者可以选择使用其他填充方式
df_clean = df.dropna(subset=['10-Minute Maximum Gust(km/hour)', '10-Minute Mean Speed(km/hour)'])

# 创建一个绘图窗口
plt.figure(figsize=(16, 12))

# 1. 绘制柱状图 - 10分钟平均风速
plt.subplot(3, 1, 1)
plt.bar(df_clean['Automatic Weather Station'], df_clean['10-Minute Mean Speed(km/hour)'], color='skyblue')
plt.xlabel('Weather Station')
plt.ylabel('10-Minute Avg Wind Speed (km/h)')
plt.title('10-Minute Avg Wind Speed by Weather Station')
plt.xticks(rotation=45)

# 2. 绘制饼图 - 10分钟最大阵风分布
plt.subplot(3, 1, 2)
# 绘制时忽略 NaN 值
plt.pie(df_clean['10-Minute Maximum Gust(km/hour)'], labels=df_clean['Automatic Weather Station'], autopct='%1.1f%%')
plt.title('10-Minute Maximum Gust Distribution by Weather Station')

# 3. 绘制折线图 - 10分钟平均风速趋势
plt.subplot(3, 1, 3)
plt.plot(df_clean['Automatic Weather Station'], df_clean['10-Minute Mean Speed(km/hour)'], marker='o', linestyle='-', color='b')
plt.xlabel('Weather Station')
plt.ylabel('10-Minute Avg Wind Speed (km/h)')
plt.title('10-Minute Avg Wind Speed Trend by Weather Station')
plt.xticks(rotation=45)

# 调整图表布局
plt.tight_layout()

# 显示图表
plt.show()
