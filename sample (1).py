import streamlit as st
from sklearn.impute import KNNImputer

# Load data
@st.cache
def load_data():
    return pd.read_csv("supermarket_sales.csv")

df =data.copy()

# Data preprocessing
# Handle missing values using KNN Imputer
imputer = KNNImputer()
df_filled = pd.DataFrame(imputer.fit_transform(df.select_dtypes(include=['float64', 'int64'])), columns=df.select_dtypes(include=['float64', 'int64']).columns)
df[df_filled.columns] = df_filled

# Dashboard design
st.title('Supermarket Sales Dashboard')

# Show data
st.subheader('Raw Data')
st.write(df)

# Interactive components
st.sidebar.title('Filters')
branch_filter = st.sidebar.multiselect('Select Branch', df['Branch'].unique())
product_filter = st.sidebar.multiselect('Select Product Line', df['Product_line'].unique())

# Apply filters
filtered_df = df[df['Branch'].isin(branch_filter) & df['Product_line'].isin(product_filter)]

# Visualization
st.subheader('Sales Analysis')
if not filtered_df.empty:
    # Bar plot
    st.write('Total Sales by Product Line')
    sales_by_product_line = filtered_df.groupby('Product_line')['Total'].sum()
    sns.barplot(x=sales_by_product_line.index, y=sales_by_product_line.values)
    plt.xticks(rotation=45)
    st.pyplot()

    # Line plot
    st.write('Total Sales over Time')
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
    sales_over_time = filtered_df.groupby('Date')['Total'].sum()
    sns.lineplot(x=sales_over_time.index, y=sales_over_time.values)
    plt.xticks(rotation=45)
    st.pyplot()
else:
    st.write('No data available for the selected filters.')
