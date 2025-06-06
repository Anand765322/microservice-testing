# 🧪 PyTest-based Microservice Test Suite (Python + Flask + Docker + Postman)

## 🧱 Project Structure

microservice-testing/
├── app/ # Flask microservice
│ └── app.py
├── tests/ # PyTest test cases
│ ├── test_api.py
│ ├── schema/ # JSON schema definitions
│ │ └── data_schema.json
│ └── data/ # (Optional) Test payloads or fixtures
├── postman/ # Postman collection
│ └── MicroserviceTests.postman_collection.json
├── locustfile.py # Load testing script (Locust)
├── Dockerfile # Docker setup for the Flask app
└── README.md

## ⚙️ Getting Started

### 🔧 1. Install Requirements

```bash
pip install flask pytest pytest-cov requests jsonschema locust
Optional:

npm install -g newman
🚦 2. Run the Microservice

python app/app.py
Now the API will be live at:
http://localhost:5000

✅ 3. Run Tests with PyTest

pytest tests/
📊 With Test Coverage

pytest --cov=app tests/
📬 4. Run Postman Collection via Newman

newman run postman/MicroserviceTests.postman_collection.json
🐳 5. Dockerize and Run
Build Docker Image:


docker build -t microservice-app .
Run Container:

docker run -p 5000:5000 microservice-app
⚡ 6. Load Testing with Locust (Bonus)

locust
Open your browser at:
http://localhost:8089

Enter:

Host: http://localhost:5000

Start testing

🧪 Sample Endpoints
Method	Endpoint	Description
GET	/api/hello	Basic health check
POST	/api/data	Echoes posted data


👨‍💻 Author
Made with by Anand
