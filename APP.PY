
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

st.title("📊 HR Analytics Dashboard - Employee Attrition Insights")
st.markdown("A comprehensive view for HR Directors and Stakeholders to track employee attrition trends and patterns.")

# Sidebar Filters
st.sidebar.header("Filter Employees")
dept_filter = st.sidebar.multiselect("Select Department(s):", options=df["Department"].unique(), default=df["Department"].unique())
role_filter = st.sidebar.multiselect("Select Job Role(s):", options=df["JobRole"].unique(), default=df["JobRole"].unique())

filtered_df = df[(df["Department"].isin(dept_filter)) & (df["JobRole"].isin(role_filter))]

# Tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Attrition Insights", "Demographics"])

with tab1:
    st.subheader("1️⃣ Overall Attrition Breakdown")
    st.markdown("This pie chart gives a macro view of the attrition rate across the filtered dataset.")
    fig1 = px.pie(filtered_df, names="Attrition", title="Attrition Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### Attrition by Gender")
    fig2 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Attrition by Marital Status")
    fig3 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.subheader("2️⃣ Deeper Dive into Attrition")
    st.markdown("Income levels can correlate with attrition likelihood. Here's the distribution.")
    fig4 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("### Years at Company vs Attrition")
    fig5 = px.violin(filtered_df, y="YearsAtCompany", x="Attrition", box=True, points="all", color="Attrition")
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### Job Satisfaction vs Attrition")
    fig6, ax = plt.subplots()
    sns.countplot(data=filtered_df, x="JobSatisfaction", hue="Attrition", ax=ax)
    st.pyplot(fig6)

    st.markdown("### Overtime vs Attrition")
    fig7 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
    st.plotly_chart(fig7, use_container_width=True)

with tab3:
    st.subheader("3️⃣ Demographic Insights")
    st.markdown("Here's how age, education and environment impact attrition.")

    st.markdown("### Age Distribution")
    fig8 = px.histogram(filtered_df, x="Age", color="Attrition", nbins=30)
    st.plotly_chart(fig8, use_container_width=True)

    st.markdown("### Education Field")
    fig9 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig9, use_container_width=True)

    st.markdown("### Work Life Balance")
    fig10 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition", barmode="group")
    st.plotly_chart(fig10, use_container_width=True)

    st.markdown("### Distance from Home vs Attrition")
    fig11 = px.box(filtered_df, x="Attrition", y="DistanceFromHome", color="Attrition")
    st.plotly_chart(fig11, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.write("Data Source: EA.csv")

