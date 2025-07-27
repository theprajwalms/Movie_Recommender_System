
# 🎬 Movie Recommender System - Collaborative Filtering Project

## 📌 Project Overview
This project demonstrates a simple recommender system using **collaborative filtering** on the MovieLens dataset. It recommends movies based on user rating patterns and movie similarity using correlation scores.

## 📊 Dataset
- **u.data**: Contains user ratings (user_id, item_id, rating, timestamp)
- **Movie_Id_Titles**: Maps movie IDs to titles

## 🛠️ Tools & Libraries Used
- Python (Jupyter Notebook)
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit (for app)

## 🔍 Workflow
1. Load and merge datasets
2. Perform exploratory data analysis (EDA)
3. Create user-item rating matrix
4. Compute correlations to find similar movies
5. Filter by rating count to improve recommendation quality
6. Build interactive recommender app using Streamlit

## 🎯 Recommender System Logic
- For any selected movie (e.g., *Star Wars*), find users who rated it highly
- Find other movies those users also liked
- Recommend movies with **high correlation** and **sufficient number of ratings**

## 📈 Sample Output
Example: For the movie *Titanic*, the model recommends:
- *My Best Friend's Wedding*
- *Jerry Maguire*
- *Scream*

(Results depend on rating patterns and filters.)

## 📌 Project Conclusion
This project showcases how collaborative filtering works using simple matrix operations and correlation. It builds the foundation for more advanced techniques like:
- Matrix factorization (SVD)
- Deep learning recommender models
- Hybrid (content + collaborative) systems

## 🚀 Streamlit App
An interactive web app was built using Streamlit for real-time movie recommendations.

### ▶️ How to Run the App Locally:
1. Make sure `u.data`, `Movie_Id_Titles`, and `recommender_app.py` are in the same folder
2. Install Streamlit:
   ```
   pip install streamlit
   ```
3. Run the app:
   ```
   streamlit run recommender_app.py
   ```

## 📁 How to Run the Notebook
1. Clone this repository
2. Run the notebook:
   ```
   01-Recommender Systems with Python.ipynb
   ```

## 👨‍🎓 Author
**Prajwal M.S**  
Aspiring Data Scientist | Python & ML Enthusiast
