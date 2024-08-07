<div align="center">
  <h1>Baccarat Game Data Generator API</h1>
</div>
<br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/913a2640-90e5-4938-9b2c-acff651fbb4d" alt="image">
</div>

### Overview
A publicly available API designed to generate simulated Baccarat game data. This API is intended for aspiring data engineers, data analysts, and data scientists who are seeking practice with real-time data, statistical analysis, and modeling.



### How to access the API
- View the documentation: https://baccarat-api-v1.onrender.com/docs
- Generate single game data: https://baccarat-api-v1.onrender.com/baccarat/
- Generate multiple game data: https://baccarat-api-v1.onrender.com/baccarat?num_records=10

![image](https://github.com/user-attachments/assets/ae66a938-8897-44c8-8eb9-7c14ada71973)


### API Limitations
- Rate Limit: Requests are limited to 5 per minute
- Records Limit: Up to 100 records per request.


### Project Ideas
- **Data Engineering:**
  - Generate data from the API,
  - Design a database to store the generated data,
  - Create an ETL pipeline
- **Data Modelling:**
  - Create dashboards,
  - Perform statistical analysis,
  - Perform clustering analysis to detect anomalies in the data.
> NOTE: The probabilities in this simulated game have been intentionally tweaked based on certain criteria.<br>It is up to you to discover the patterns using techniques such as clustering analysis or other methods.
### Technology Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

--------------------------------------------------

<div align="center">
  <h1>Developer Notes</h1>
</div>

### Local Development
To run the API locally, follow these steps:
1. **Clone the Repository:**
   `git clone https://github.com/gryAI/baccarat-game-data-generator-api.git`
2. **Navigate to the project directory:**
   `cd baccarat-game-data-generator-api`
3. **Setup a Virtual Environment:**<br>
    `python -m venv venv` <br>
    `source venv/Scripts/activate`
 4. **Install Dependencies:** `pip install -r requirements.txt`
 5. **Run the application:** `uvicorn server.app:app --host 0.0.0.0 --port 8000`

--------------------------------------------------
### Let's connect! https://www.linkedin.com/in/lqestradacpa/
    
