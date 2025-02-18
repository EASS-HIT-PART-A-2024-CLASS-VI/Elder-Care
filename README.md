
# Elder Care Management System

The Elder Care Management System is an innovative and user-friendly platform designed to enhance the quality of life for elderly individuals while simplifying care management for families, guardians, caregivers, and elder care facilities.

---

## ✨ Features
1. 🛠️ Manage caregivers, elderly individuals, tasks, and medications.
2. 📝 Generate a PDF payment report for caregivers.
3. 🔄 Assign and unassign caregivers to elderly individuals.
4. 🏥 View comprehensive caregiver and elderly profiles
5. 🚀 Flexible and extensible design for future enhancements.


---

## 📂 Project Structure
```
Elder-Care/
│── backend/
│   │── db/                # Database configuration and connection
│   │   │── __init__.py
│   │   │── database.py
│   │
│   │── models/            # SQLAlchemy models for database
│   │   │── __init__.py
│   │   │── caregiver.py
│   │   │── caregiver_assignments.py
│   │   │── elderly.py
│   │   │── medication.py
│   │   │── task.py
│   │
│   │── routes/            # FastAPI route handlers
│   │   │── __init__.py
│   │   │── caregiver_assignments.py
│   │   │── caregivers.py
│   │   │── elderly.py
│   │
│   │── schemas/           # Pydantic schemas for data validation
│   │   │── caregiver.py
│   │   │── caregiver_assignment.py
│   │   │── elderly.py
│   │   │── medication.py
│   │   │── task.py
│   │
│   │── utils/             # Utility functions (e.g., PDF generation)
│   │   │── __init__.py
│   │   │── pdf_generator.py
│   │
│   │── Tests/             # Automated test scripts
│   │   │── test_api_integration.py
│   │   │── test_units.py
│   │
│   │── Dockerfile         # Backend containerization
│   │── main.py            # FastAPI application entry point
│   │── requirements.txt   # Backend dependencies
│
│── frontend/
│   │── components/        # Streamlit UI components
│   │   │── __init__.py
│   │   │── add_data.py
│   │   │── manage_caregivers.py
│   │   │── manage_elderly.py
│   │   │── view_data.py
│   │
│   │── Dockerfile         # Frontend containerization
│   │── api_client.py      # Handles API communication
│   │── requirements.txt   # Frontend dependencies
│   │── ui.py              # Streamlit main UI file
│
│── docker-compose.yml     # Docker configuration for services
│── README.md              # Project documentation
│── pytest.ini             # Pytest configuration
```


## 💻 Technologies Used
- **FastAPI**: Backend framework.
- **PostgreSQL**: Database management.
- **Docker**: Containerization.
- **SQLAlchemy**: ORM for database interactions.
- **Pydantic**: Data validation and settings management.
- **FPDF**: PDF generation.
- **pytest**: Testing framework.

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-VI/Elder-Care.git
```

---

### Step 2: Navigate to the Project Directory
```bash
cd Elder-Care
```

---

### Step 3: Create a `.env` File
Create a `.env` file in the project's root directory and add the following variables:
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=elder_care_db
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/elder_care_db
```

---

### Step 4: Build and Run the Application with Docker
```bash
docker-compose up --build
```
---

### Step 5: Access the Application UI
Once the application is running, you can access the UI of the Elder Care Management System in your web browser:

**Frontend (Streamlit):**  
- **URL**: [http://localhost:8501](http://localhost:8501)  
  - Manage caregivers and their salaries, and generate a detailed PDF including all caregiver details and payment information."  
  - Manage elderly individuals, their tasks, and medications.  
  - View all data in a structured and user-friendly format.  

**Backend API (Swagger Documentation):**  
- **URL**: [http://localhost:8000/docs](http://localhost:8000/docs)  
  - Provides API documentation and allows you to test the backend endpoints directly.  

 ---

## 📬 Contact Info
**Ori Levi**  
📧 Email: Leviori1218@gmail.com  
🐙 GitHub: [OriLevi12](https://github.com/OriLevi12)


 ---
## illustration
![application design](frontend/media/ApplicationDesign.png)

