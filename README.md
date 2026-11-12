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
| `Sep7.xlsx`             | Lightning strike dataset for September 7th (example file).          |
| `heat.py`               | Generates a lightning strike heatmap for a given time.              |
| `hourly diwnload.py`    | Bar chart of hourly lightning frequency.                            |
| `peak current.py`       | Finds the strongest peak current (Ip) and maps its location.        |

> The April dataset (`april22.xlsx`) mentioned in earlier versions of this README is not included in this repository.

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
| 🌎 Spatial Heatmap         | `python heat.py`                    |
| 📊 Hourly Distribution     | `python "hourly diwnload.py"`       |
| 💥 Peak Current Locator    | `python "peak current.py"`          |

⚠️ **Make sure your Excel files are in the same directory as the script or adjust paths accordingly.**

---

## 📸 Example Output
- **Interactive Folium maps** showing density of lightning strikes.
- **Bar plots** showing hourly lightning distributions.
- **Pinpoint location** of the highest peak current strike, marked in red.

---

## 🏅 Badges
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10307/badge)](https://www.bestpractices.dev/projects/10307)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/krocks9903/Lightning-Research-Using-Python/badge)](https://securityscorecards.dev/viewer/?uri=github.com/krocks9903/Lightning-Research-Using-Python)

---

## 👨‍💻 Author
**Krish Shah**  
🌐 [GitHub Profile](https://github.com/krocks9903)

---

## ⭐ Future Improvements
- Add dynamic time slider to heatmaps.
- Automate daily data updates via APIs.
- Add alert system for peak lightning conditions.

