# Web MVP Architecture Specification

*Date: April 20, 2025*

This document outlines the technical architecture for transforming the current Heavy Oil Rheology ML project into a web-based Minimum Viable Product (MVP). The MVP will maintain the same analytical capabilities as the current implementation while providing a user-friendly web interface for data entry, processing, and visualization.

## 1. System Overview

The RheoML Web MVP will follow a three-tier architecture:

1. **Frontend**: A web-based user interface for data upload, parameter configuration, and result visualization
2. **Backend API**: A RESTful service that provides endpoints for data processing and model execution
3. **Machine Learning Core**: The existing ML pipeline refactored for web integration

This architecture enables separation of concerns while maintaining the analytical capabilities of the current implementation.

## 2. Technical Stack

### Frontend
- **Framework**: React.js
- **UI Components**: Material UI or Tailwind CSS
- **Visualization**: D3.js or Chart.js for interactive visualizations
- **State Management**: Context API or Redux for application state
- **API Integration**: Axios or Fetch API for backend communication

### Backend
- **Framework**: FastAPI (Python)
- **Authentication**: JWT-based authentication
- **Validation**: Pydantic models for request validation
- **API Documentation**: Swagger/OpenAPI

### Machine Learning
- **Core Libraries**: scikit-learn, pandas, numpy (existing implementation)
- **Explainability**: SHAP for model interpretation
- **Model Storage**: Pickle or joblib for model serialization

### Infrastructure
- **Containerization**: Docker and Docker Compose
- **Deployment**: Cloud platform (initially Render, Heroku, or Railway)
- **Database**: PostgreSQL for user data and metadata
- **Storage**: Cloud object storage for data files and model artifacts

## 3. Component Architecture

### 3.1 Frontend Architecture

The frontend will be organized as a single-page application with the following components:

```
src/
├── components/           # Reusable UI components
│   ├── Header.jsx       # Application header
│   ├── Footer.jsx       # Application footer
│   ├── DataUpload.jsx   # File upload component
│   ├── ModelSelector.jsx # Model selection interface
│   ├── ResultsView.jsx  # Results visualization
│   └── ...
├── pages/               # Application pages
│   ├── Home.jsx         # Landing page
│   ├── Analysis.jsx     # Analysis configuration
│   ├── Results.jsx      # Results display
│   └── ...
├── services/            # API integration
│   ├── api.js           # API client
│   ├── auth.js          # Authentication service
│   └── ...
├── utils/               # Utility functions
│   ├── formatters.js    # Data formatting utilities
│   ├── validators.js    # Input validation
│   └── ...
└── App.jsx              # Main application component
```

### 3.2 Backend Architecture

The backend will be structured as a REST API with the following components:

```
app/
├── api/                 # API endpoints
│   ├── __init__.py      
│   ├── auth.py          # Authentication endpoints
│   ├── models.py        # ML model endpoints
│   ├── upload.py        # File upload endpoints
│   └── ...
├── core/                # Core functionality
│   ├── config.py        # Configuration settings
│   ├── security.py      # Authentication logic
│   └── ...
├── db/                  # Database integration
│   ├── models.py        # Database models
│   ├── session.py       # Database session
│   └── ...
├── ml/                  # Machine learning components
│   ├── pipeline.py      # Refactored ML pipeline
│   ├── models.py        # ML model implementations
│   ├── preprocessing.py # Data preprocessing
│   └── evaluation.py    # Model evaluation
├── schemas/             # Pydantic schemas
│   ├── user.py          # User schemas
│   ├── analysis.py      # Analysis request/response schemas
│   └── ...
├── utils/               # Utility functions
│   ├── file_handling.py # File processing utilities
│   └── ...
└── main.py              # Application entry point
```

### 3.3 Data Flow

The system will follow this data flow:

1. **Data Upload**: User uploads rheological data through the web interface
2. **Data Validation**: Backend validates file format and data structure
3. **Parameter Configuration**: User configures analysis parameters
4. **Processing**: Backend processes data using the ML pipeline
5. **Model Execution**: Selected model is applied to processed data
6. **Result Generation**: Results including predictions and SHAP analysis are generated
7. **Visualization**: Results are visualized in the frontend

## 4. API Specification

### 4.1 Core Endpoints

#### Authentication
- `POST /api/auth/register`: Register new user
- `POST /api/auth/login`: User login
- `POST /api/auth/logout`: User logout

#### Data Management
- `POST /api/data/upload`: Upload rheological data
- `GET /api/data`: List user's uploaded datasets
- `GET /api/data/{id}`: Get specific dataset
- `DELETE /api/data/{id}`: Delete dataset

#### Analysis
- `POST /api/analysis/run`: Run analysis with specified parameters
- `GET /api/analysis`: List user's analyses
- `GET /api/analysis/{id}`: Get specific analysis result
- `DELETE /api/analysis/{id}`: Delete analysis

### 4.2 Request/Response Examples

#### Upload Data

**Request:**
```
POST /api/data/upload
Content-Type: multipart/form-data

{
  "file": <file>,
  "name": "Heavy Oil Sample 1",
  "description": "Measurement from Haake RS 6000",
  "device_type": "haake_rs6000"
}
```

**Response:**
```json
{
  "id": "dataset_123",
  "name": "Heavy Oil Sample 1",
  "description": "Measurement from Haake RS 6000",
  "device_type": "haake_rs6000",
  "created_at": "2025-04-20T12:00:00Z",
  "columns": ["Temperature", "Shear Rate", "Shear Stress", "Viscosity"],
  "rows": 120,
  "status": "ready"
}
```

#### Run Analysis

**Request:**
```json
POST /api/analysis/run
Content-Type: application/json

{
  "dataset_id": "dataset_123",
  "model_type": "gradient_boosting",
  "parameters": {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "max_depth": 3
  },
  "target_variable": "Apparent Viscosity",
  "features": ["Temperature", "Shear Rate", "Shear Stress"]
}
```

**Response:**
```json
{
  "id": "analysis_456",
  "dataset_id": "dataset_123",
  "status": "processing",
  "created_at": "2025-04-20T12:05:00Z",
  "estimated_completion": "2025-04-20T12:06:30Z"
}
```

## 5. Database Schema

### Users
```
users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
```

### Datasets
```
datasets (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  device_type VARCHAR(100),
  file_path VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  metadata JSONB
)
```

### Analyses
```
analyses (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  dataset_id UUID REFERENCES datasets(id),
  model_type VARCHAR(100) NOT NULL,
  parameters JSONB NOT NULL,
  target_variable VARCHAR(100) NOT NULL,
  features JSONB NOT NULL,
  status VARCHAR(50) NOT NULL,
  results JSONB,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)
```

## 6. ML Pipeline Integration

The existing ML pipeline will be refactored into a modular architecture:

1. **Data Loading**: Convert uploaded files to pandas DataFrames
2. **Preprocessing**: Apply data cleaning and normalization
3. **Feature Engineering**: Generate derived features
4. **Model Selection**: Choose appropriate model based on user input
5. **Training and Evaluation**: Train model and compute metrics
6. **SHAP Analysis**: Generate feature importance explanations
7. **Result Formatting**: Format results for API response

## 7. AI Result Interpretation

The MVP will include an integration with Claude API to provide natural language interpretation of results:

1. **Analysis Summarization**: Generate concise summaries of analysis results
2. **SHAP Explanation**: Interpret SHAP values in plain language
3. **Recommendation Generation**: Provide actionable insights based on analysis

## 8. Security Considerations

The MVP will implement the following security measures:

1. **Authentication**: JWT-based authentication for API access
2. **Authorization**: Role-based access control for data and analyses
3. **Data Protection**: Encrypted storage for sensitive data
4. **Input Validation**: Comprehensive validation of all user inputs
5. **Rate Limiting**: Protection against abuse and DoS attacks

## 9. Development and Deployment Plan

### Development Phases

1. **Phase 1: Backend Development** (2-3 weeks)
   - Set up project structure
   - Implement core API endpoints
   - Refactor ML pipeline for web integration
   - Implement data validation and processing

2. **Phase 2: Frontend Development** (2-3 weeks)
   - Create user interface components
   - Implement data upload and visualization
   - Integrate with backend API
   - Add result interpretation views

3. **Phase 3: Integration and Testing** (1-2 weeks)
   - End-to-end integration testing
   - Performance optimization
   - Security testing
   - User acceptance testing

4. **Phase 4: Deployment** (1 week)
   - Set up containerization
   - Deploy to cloud platform
   - Configure monitoring and logging
   - Document deployment process

### Deployment Architecture

```
┌────────────────┐      ┌────────────────┐      ┌────────────────┐
│                │      │                │      │                │
│  Web Frontend  │◄────►│  Backend API   │◄────►│  ML Pipeline   │
│  (React)       │      │  (FastAPI)     │      │  (Python)      │
│                │      │                │      │                │
└────────────────┘      └─────────┬──────┘      └────────────────┘
                                  │
                        ┌─────────▼──────┐
                        │                │
                        │   Database     │
                        │  (PostgreSQL)  │
                        │                │
                        └────────────────┘
```

## 10. Future Extensions

While the MVP focuses on replicating the current functionality in a web interface, the architecture is designed to support future extensions:

1. **Multi-Device Support**: Expand data importers for various rheometer brands
2. **Additional ML Models**: Implement alternative model types
3. **Advanced Visualizations**: Add interactive 3D visualizations
4. **Collaboration Features**: Enable sharing and team collaboration
5. **API Access**: Provide API keys for programmatic access
6. **Custom Model Training**: Allow users to train custom models

## Conclusion

This architecture provides a solid foundation for transforming the current research project into a web-based application. By maintaining the core analytical capabilities while improving accessibility through a user-friendly interface, the MVP will serve as the first step toward the comprehensive RheoML platform outlined in the product roadmap.

The design prioritizes modularity, extensibility, and security, allowing for incremental development and expansion as the project evolves beyond the MVP phase.