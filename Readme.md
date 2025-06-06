# 🧪 PyTest-based Microservice Test Suite (Python + Flask + Docker + Postman)

This project demonstrates a complete test suite setup for a mock RESTful microservice using **Python**, **Flask**, **PyTest**, **Docker**, and **Postman** — built specifically to showcase the skillset needed for an SDET3 role.

---

## 🚀 Why This Project?

- 🔍 Shows expertise in API testing using **PyTest**
- 📜 Includes **JSON schema validation** (contract testing)
- 🔐 Demonstrates **auth/rate-limit style tests**
- 📦 Integrates **Postman/Newman** for smoke testing
- 🐳 Run everything via **Docker** and **PyTest CLI**
- 📊 Supports test coverage via `pytest-cov`
- ⚡ Bonus: Load testing with **Locust**

---

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

yaml
Copy
Edit

---

## ⚙️ Getting Started

### 🔧 1. Install Requirements

```bash
pip install flask pytest pytest-cov requests jsonschema locust
Optional:

bash
Copy
Edit
npm install -g newman
🚦 2. Run the Microservice
bash
Copy
Edit
python app/app.py
Now the API will be live at:
http://localhost:5000

✅ 3. Run Tests with PyTest
bash
Copy
Edit
pytest tests/
📊 With Test Coverage
bash
Copy
Edit
pytest --cov=app tests/
📬 4. Run Postman Collection via Newman
bash
Copy
Edit
newman run postman/MicroserviceTests.postman_collection.json
🐳 5. Dockerize and Run
Build Docker Image:

bash
Copy
Edit
docker build -t microservice-app .
Run Container:

bash
Copy
Edit
docker run -p 5000:5000 microservice-app
⚡ 6. Load Testing with Locust (Bonus)
bash
Copy
Edit
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

📚 Skills Demonstrated
✅ Functional & schema-based API testing

🔐 Auth/rate-limiting style validation

📊 Test coverage & reporting

🧪 Postman + PyTest comparison

🐳 Dockerized testing pipeline

⚡ Load testing simulation

👨‍💻 Author
Made with by Anand