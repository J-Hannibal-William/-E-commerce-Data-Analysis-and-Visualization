import pandas as pd
import matplotlib.pyplot as plt

# Function to load the data from the file
def load_data(file_path='ecommerce_data.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
        exit()
    except pd.errors.EmptyDataError:
        print("No data found in the file. Please check the file contents.")
        exit()

# Function to perform data analysis
def analyze_data():
    # Your name in the project
    print("Project by J Hannibal William")
    
    # Get the file path from the user
    file_path = input("Enter the path to the ecommerce data CSV file (or press Enter for default): ")
    if not file_path:
        file_path = 'ecommerce_data.csv'

    # Load the data
    df = load_data(file_path)

    # Create necessary columns
    df['Revenue'] = df['price'] * df['quantity']
    df['Profit'] = df['Revenue'] - df['cost']
    df['Loss'] = df['cost'] - df['Revenue']
    df['Sales'] = df['price'] * df['quantity']

    # Show first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Summary statistics
    print("\nSummary of the dataset:")
    print(df.describe())

    try:
        # Ask the user for the type of chart they want to view
        while True:
            chart_type = input("\nEnter the type of chart you want to view (bar/pie/line/hist): ").strip().lower()

            if chart_type == 'bar':
                plot_bar_chart(df)
            elif chart_type == 'pie':
                plot_pie_chart(df)
            elif chart_type == 'line':
                plot_line_chart(df)
            elif chart_type == 'hist':
                plot_histogram(df)
            else:
                print("Invalid chart type. Please enter 'bar', 'pie', 'line', or 'hist'.")
                continue

            # Ask for the specific data to display
            data_type = input("\nEnter the type of data you want to view (profit/revenue/loss/sales): ").strip().lower()

            if data_type == 'profit':
                plot_profit_chart(df)
            elif data_type == 'revenue':
                plot_revenue_chart(df)
            elif data_type == 'loss':
                plot_loss_chart(df)
            elif data_type == 'sales':
                plot_sales_chart(df)
            else:
                print("Invalid data type. Please enter 'profit', 'revenue', 'loss', or 'sales'.")
                continue

            change_chart = input("\nDo you want to change the chart? (yes/no): ").strip().lower()
            if change_chart != 'yes':
                break

    except KeyError as e:
        print(f"Error plotting data: {e}")

# Function to plot a bar chart
def plot_bar_chart(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(df['product_name'], df['Revenue'], color='skyblue')
        plt.xlabel('Product Name')
        plt.ylabel('Revenue')
        plt.title('Revenue by Product (Bar Chart)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a pie chart
def plot_pie_chart(df):
    try:
        plt.figure(figsize=(8, 8))
        plt.pie(df['Revenue'], labels=df['product_name'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title('Revenue by Product (Pie Chart)')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a line chart
def plot_line_chart(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(df['product_name'], df['Revenue'], marker='o', linestyle='-', color='b')
        plt.xlabel('Product Name')
        plt.ylabel('Revenue')
        plt.title('Revenue by Product (Line Chart)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a histogram
def plot_histogram(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(df['Revenue'], bins=10, color='lightgreen', edgecolor='black')
        plt.xlabel('Revenue')
        plt.ylabel('Frequency')
        plt.title('Revenue Distribution (Histogram)')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a profit chart
def plot_profit_chart(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(df['product_name'], df['Profit'], color='green')
        plt.xlabel('Product Name')
        plt.ylabel('Profit')
        plt.title('Profit by Product')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a revenue chart
def plot_revenue_chart(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(df['product_name'], df['Revenue'], color='blue')
        plt.xlabel('Product Name')
        plt.ylabel('Revenue')
        plt.title('Revenue by Product')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a loss chart
def plot_loss_chart(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(df['product_name'], df['Loss'], color='red')
        plt.xlabel('Product Name')
        plt.ylabel('Loss')
        plt.title('Loss by Product')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Function to plot a sales chart
def plot_sales_chart(df):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(df['product_name'], df['Sales'], color='orange')
        plt.xlabel('Product Name')
        plt.ylabel('Sales')
        plt.title('Sales by Product')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Main function to drive the program
if __name__ == "__main__":
    analyze_data()
