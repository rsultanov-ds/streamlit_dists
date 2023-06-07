import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib as mpl
import seaborn as sns

st.markdown("<h1 style='text-align: center;'>Визуализация кривых распределений</h1>", unsafe_allow_html=True)
''
''

st.subheader('1. Нормальное распределение')
norm_dist_plot = plt.figure(figsize=(10,8))
n_feed = np.linspace(-50, 50, 500)
n_mu = st.slider('Выберите значение математического ожидания:', -20, 20, 0)
n_sigma = st.slider('Выберите значение стандартного отклонения:', 1, 20, 1)
norm_dist = stats.norm(n_mu, n_sigma)
sns.lineplot(x=n_feed, y=norm_dist.pdf(n_feed))
st.pyplot(norm_dist_plot)
''
st.subheader('2. Экспоненциальное распределение')
expon_dist_plot = plt.figure(figsize=(10,8))
e_feed = np.linspace(0, 10, 500)
e_scale = st.slider('Выберите значение среднего значения:', 0.2, 3.0, 1.0)
expon_dist = stats.expon(scale=e_scale)
sns.lineplot(x=e_feed, y=expon_dist.pdf(e_feed))
st.pyplot(expon_dist_plot)
''
st.subheader('3. Распределение Пуассона')
poi_dist_plot = plt.figure(figsize=(10,8))
p_feed = np.arange(0,30)
p_lambda = st.slider('Выберите значение лямбда:', 1, 20, 6)
poi_dist = stats.poisson(p_lambda)
sns.barplot(x=p_feed, y=poi_dist.pmf(p_feed), color='darkgrey')
st.pyplot(poi_dist_plot)