# ⚡ Lightning Strike Data Visualization & Peak Current Analysis

## 🌟 Overview
This project visualizes lightning strike data from Excel files using interactive heatmaps and data plots. You can:

- 🌎 View lightning strikes spatially across Florida.
- 📊 See hourly lightning frequency distributions.
- 💥 Identify and map the strongest lightning strike (based on peak current Ip).

---

## 📂 Features
| Feature | Description |
|---------|-------------|
| 🌎 **Interactive Heatmap** | Visualize lightning strikes on a map by specifying month, day, hour, and minute. |
| 📊 **Hourly Distribution Plot** | Display bar charts showing lightning activity by hour. |
| 💥 **Peak Current (Ip) Locator & Map** | Automatically find the strongest lightning strike and mark it on an interactive map. |
| 🔎 **User Input-Based Filtering** | Filter large datasets by exact date, time, and second to zoom in on key moments. |

---

## 🛠️ Technologies Used
- Python 3
- Pandas
- Folium (with HeatMap plugin)
- Matplotlib
- OpenPyXL
- Jupyter Notebook (for inline map display)

---

## 📁 Project Structure
| File Name               | Purpose                                                             |
|-------------------------|---------------------------------------------------------------------|
| `april22.xlsx`          | Lightning strike dataset for April.                                 |
| `Sep7.xlsx`             | Lightning strike dataset for September 7th (example file).          |
| `spatial_plot.py`       | Script to generate a lightning strike heatmap for a given time.     |
| `hourly_distribution.py`| Script to generate bar charts showing hourly lightning frequency.   |
| `peak_current_map.py`   | Script to find the strongest peak current (Ip) and visualize its location on a map. |

---

## 🚀 How to Run
### 1️⃣ Clone the Repository:
```bash
git clone https://github.com/krocks9903/Lightning-Research-Using-Python.git
cd Lightning-Research-Using-Python
```

### 2️⃣ Install Required Packages:
```bash
pip install pandas folium matplotlib openpyxl
```

### 3️⃣ Run the Scripts:
| Script                     | How to run                         |
|----------------------------|-------------------------------------|
| 🌎 Spatial Heatmap         | `python spatial_plot.py`            |
| 📊 Hourly Distribution     | `python hourly_distribution.py`     |
| 💥 Peak Current Locator    | `python peak_current_map.py`        |

⚠️ **Make sure your Excel files are in the same directory as the script or adjust paths accordingly.**

---

## 📸 Example Output
- **Interactive Folium maps** showing density of lightning strikes.
- **Bar plots** showing hourly lightning distributions.
- **Pinpoint location** of the highest peak current strike, marked in red.

---

## 🏅 Badges
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10307/badge)](https://www.bestpractices.dev/projects/10307)

---

## 👨‍💻 Author
**Krish Shah**  
🌐 [GitHub Profile](https://github.com/krocks9903)

---

## ⭐ Future Improvements
- Add dynamic time slider to heatmaps.
- Automate daily data updates via APIs.
- Add alert system for peak lightning conditions.

