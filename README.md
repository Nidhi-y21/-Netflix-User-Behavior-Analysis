### 📊 Netflix User Behavior Analysis

#### 🧠 Objective

To understand what types of content Netflix users prefer by analyzing their viewing habits, genres watched, and ratings given.

#### 📁 Dataset

A synthetic dataset containing:

* `User`: Unique user identifier
* `Title`: Show title
* `Genre`: Content genre
* `HoursWatched`: Number of hours watched
* `Rating`: User's rating (1–5)
* `Date`: Viewing date

The dataset is saved as `netflix_data.csv`.

#### 📈 Key Analyses

* Total watch hours by genre
* Top 10 users by watch hours and sessions
* Ratings distribution per genre
* Viewing trend over time

#### 📷 Visual Output

The following plots are saved as PNGs:

* `top_genres.png`
* `top_users_watch_hours.png`
* `top_users_sessions.png`
* `ratings_vs_genres.png`
* `watch_time_trend.png`

#### 🚀 How to Run

```bash
python netflix_behavior_analysis.py
```

Make sure the following libraries are installed:

```bash
pip install pandas numpy plotly
```

---

