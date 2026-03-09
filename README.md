# Network Security — Phishing Detection System

A machine learning-powered end-to-end pipeline for detecting phishing threats in network data. Built with Python, Flask, and MongoDB, this project covers the full ML lifecycle: data ingestion, validation, transformation, model training, evaluation, and deployment.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Application](#running-the-application)
  - [Running with Docker](#running-with-docker)
- [ML Pipeline](#ml-pipeline)
- [API Endpoints](#api-endpoints)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project implements an automated network security system that classifies URLs and network traffic patterns as **phishing** or **legitimate** using supervised machine learning. The system is designed with a modular, production-ready architecture that includes data versioning, model evaluation gates, and a REST API served via Flask.

---

## Features

- End-to-end ML pipeline (ingestion → validation → transformation → training → evaluation)
- Real-time phishing prediction via Flask REST API
- MongoDB integration for data storage and experiment tracking
- Modular package structure for easy extension
- Docker support for containerized deployment
- Environment-based configuration management

---

## Project Structure

```
NetworkSecurity/
├── Network_Data/
│   └── phisingData.csv          # Raw phishing dataset
├── networksecurity/
│   ├── cloud/                   # Cloud storage utilities
│   ├── components/              # Pipeline stage implementations
│   ├── constant/                # Project-wide constants
│   ├── entity/                  # Config and artifact data classes
│   ├── exception/               # Custom exception handling
│   ├── logging/                 # Logging configuration
│   ├── pipeline/                # Training & prediction pipelines
│   └── utils/                   # Helper functions
├── notebooks/                   # Exploratory data analysis notebooks
├── src/                         # Application entry points
├── static/
│   └── images/                  # Static assets for the web UI
├── templates/                   # Flask HTML templates
├── Dockerfile                   # Docker build configuration
├── requirements.txt             # Python dependencies
└── setup.py                    # Package setup
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Web Framework | Flask |
| ML / Data | scikit-learn, NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Database | MongoDB (via PyMongo) |
| Serialization | Joblib, Dill |
| Containerization | Docker |
| Configuration | python-dotenv |

---

## Getting Started

### Prerequisites

- Python 3.12+
- MongoDB instance (local or Atlas)
- Docker (optional, for containerized deployment)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/NetworkSecurity.git
cd NetworkSecurity

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

### Environment Variables

Create a `.env` file in the project root:

```env
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/
DATABASE_NAME=networksecurity
COLLECTION_NAME=phishing_data
```

### Running the Application

```bash
python src/app.py
```

The Flask server will start at `http://localhost:5000`.

### Running with Docker

```bash
# Build the image
docker build -t networksecurity .

# Run the container
docker run -p 5000:5000 --env-file .env networksecurity
```

---

## ML Pipeline

The training pipeline consists of the following sequential stages:

1. **Data Ingestion** — Loads raw data from MongoDB or CSV and splits into train/test sets.
2. **Data Validation** — Checks schema conformity, detects data drift, and validates feature distributions.
3. **Data Transformation** — Applies feature engineering and preprocessing (scaling, encoding).
4. **Model Training** — Trains a classification model and tunes hyperparameters.
5. **Model Evaluation** — Compares the new model against the production baseline using accuracy and F1-score.
6. **Model Pusher** — Promotes the best model to the serving layer if evaluation thresholds are met.

To trigger the full training pipeline:

```bash
python src/train_pipeline.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check / home page |
| `POST` | `/predict` | Predict phishing for input features |
| `GET` | `/train` | Trigger the training pipeline |

### Example Prediction Request

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [...]}'
```

---

## Dataset

The dataset (`Network_Data/phisingData.csv`) contains labeled network and URL features commonly used to distinguish phishing sites from legitimate ones. Features include URL length, presence of special characters, domain age, HTTPS usage, and more.

- **Target column:** `Result` — `1` (legitimate) or `-1` (phishing)
- **Source:** UCI Machine Learning Repository — Phishing Websites dataset

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
