import streamlit as st
import plotly.express as px
df=px.data.tips()
st.set_page_config(
    layout='wide',
    page_title = 'DashBoard',
    page_icon='💰'
)
page = st.sidebar.radio('Select Page',['Dataset Overview','Descriptive Statistics','Charts'])
if page=='Dataset Overview':
    st.write('<h1 style="text-align: center; color: GoldenRod;">Tips DashBoard</h1>',unsafe_allow_html=True)
    space1,col,space2=st.columns([2,4,2])
    col.dataframe(df,width=600, height=700)
elif page=='Descriptive Statistics':
    col1, space, col2 = st.columns([5,2,5])
    with col1:
        st.metric('total_bill',round(df['total_bill'].sum(),20))
        st.dataframe(df.describe(include='number'),width=250, height=200)
    with col2:
        st.dataframe(df.describe(include='O'),width=350, height=200)
elif page=='Charts':
    tab1,tab2 = st.tabs(['Univariate','Bivariate'])
    with tab1:
        with st.container():
            space,col,space2 = st.columns([3,4,3])
            col_name=col.selectbox('select column to show its distribution'.title(),df.columns)
        if col_name in df.select_dtypes(include='number'):
            col1,space,col2=st.columns([5,1,5])
            fig1 = px.histogram(df, x=col_name, color_discrete_sequence=px.colors.qualitative.Antique ,
                                title=f'{col} hist distribution',width=500)
            fig2 = px.box(df, x=col_name, color_discrete_sequence=px.colors.qualitative.Bold,
                         title=f'{col} boxplot distribution',width=500)
            col1.plotly_chart(fig1)
            col2.plotly_chart(fig2)  
        else:
            col1,space,col2=st.columns([5,1,5])
            fig1 = px.histogram(df, x=col_name, color_discrete_sequence=px.colors.qualitative.Antique ,
                                title=f'{col} hist distribution',width=500)
            fig2 = px.pie(df, names=col_name, color_discrete_sequence=px.colors.qualitative.Bold,hole=0.3,
                         title=f'{col} boxplot distribution',width=500)
            col1.plotly_chart(fig1)
            col2.plotly_chart(fig2) 
        with tab2:
            col1, space,col2 =st.columns([5,3,5])
            with col1:
                fig =px.histogram(df, x='total_bill', color='sex', color_discrete_sequence=px.colors.qualitative.Antique)
                st.plotly_chart(fig)
                fig2 =px.scatter(df, x='total_bill', y='tip',color='day' , size='size', size_max=40,
                                 color_discrete_sequence=px.colors.qualitative.Antique)
                st.plotly_chart(fig2)
                
