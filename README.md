## ThyroDetect App

### Overview
The ThyroDetect App is an advanced healthcare tool designed to assist users and healthcare providers in assessing the risk of thyroid disorders. This mobile application leverages machine learning to analyze symptoms and medical history, helping with early detection and intervention for thyroid health issues. The app provides a user-friendly, automated, and private platform for thyroid risk assessment, aiming to increase awareness, streamline diagnostics, and support better health outcomes.

### Features
* **Risk Assessment**: Predicts thyroid disorder risk based on user-reported symptoms and medical history.
* **User-Friendly Interface**: Intuitive, easy-to-navigate design for non-specialist users.
* **Real-Time Analysis**: Employs machine learning to assess thyroid health based on specific input parameters.
* **Educational Resources**: Provides materials on thyroid health, symptoms, and treatment options.
* **Record Keeping**: Archives past assessments for ongoing monitoring and healthcare continuity.
* **Privacy-Focused**: Ensures data security, including password hashing using SHA512.

### File Structure
* `app_frontend/`: Contains the Flutter code for the app’s interface.
* `backend/`: FastAPI-based backend for data processing and storage.
* `database/`: MongoDB configuration files for managing user data and thyroid health records.
* `models/`: Includes machine learning models for thyroid disorder prediction.
* `README.md`: Project overview, installation guide, and usage instructions.

### Installation

#### Prerequisites
* **Primary Platform**: Android (may expand to other platforms in the future).
* **Technologies**:
  * **Frontend**: Flutter (Dart)
  * **Backend**: FastAPI with Python
  * **Database**: MongoDB for storing and retrieving user data

#### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/thyrodetect-app.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd thyrodetect-app
   ```

3. **Set Up the Backend**:
   * Install Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   * Start the FastAPI server:
     ```bash
     uvicorn backend.main:app --reload
     ```

4. **Configure the Database**:
   * Set up MongoDB and configure the connection settings in `backend/config.py`.

5. **Run the Frontend**:
   * Open the `app_frontend/` folder in a Flutter-compatible IDE (e.g., Android Studio or VSCode).
   * Connect an Android emulator or device.
   * Run the Flutter app:
     ```bash
     flutter run
     ```

### Usage
1. **Launch the App**:
   * Open the ThyroDetect App on an Android device or emulator.

2. **Complete the Questionnaire**:
   * Enter symptoms, medical history, and relevant parameters such as age and weight.
   * Submit responses for an immediate assessment of thyroid health.

3. **View Results**:
   * Results provide a thyroid disorder risk level (e.g., Low, Moderate, High) along with recommendations for further action.

4. **Access Educational Resources**:
   * Learn about thyroid health, common symptoms, and available treatment options.
   * Use links to connect with healthcare providers and support groups.

### Model Training
The backend includes machine learning models trained on thyroid disorder datasets. For re-training or updating:
1. **Data Preparation**: Collect and preprocess data, handling missing values and normalizing features.
2. **Training**: Use Scikit-learn or TensorFlow to train models on labeled thyroid health data.
3. **Evaluation**: Evaluate models with metrics like accuracy, precision, and recall.
4. **Deployment**: Update models in the `models/` directory for integration into the app.

### Contributing
1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-name`).
3. **Commit your changes** (`git commit -m 'Add feature'`).
4. **Push to the branch** (`git push origin feature-name`).
5. **Open a Pull Request**.
