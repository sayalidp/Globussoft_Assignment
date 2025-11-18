# Globussoft_Assignment

## Task 1: Amazon Laptop Scraper

**Information Captured for Each Laptop:**

- Image
- Title
- Rating
- Price
- Ad / Organic Result

**Example Output:**  
Below is a screenshot of the CSV output:

![Task 1 Output Screenshot](https://github.com/sayalidp/Globussoft_Assignment/blob/95d1516428321e7af741df59773891e7fa96e477/Task1_AmazonLaptopScraper/output%20ss.png)

---

## Task 2(B): Drone Count Detection

**Information Returned by API:**
This API is designed to detect and count drones within an image uploaded by the user. 

- List of bounding boxes
- Confidence scores
- Total count of detected drones

#### 1\. 🛠️ Setup and Execution

1.  **Clone the repository and switch to the branch:**
    ```bash
    git clone [https://github.com/sayalidp/Globussoft_Assignment.git](https://github.com/sayalidp/Globussoft_Assignment.git)
    cd Globussoft_Assignment
    git checkout Task2_B_Drone_Detection
    ```
2.  **Install Dependencies:**
    This requires a `requirements.txt` file in the project directory.
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the API Server:**
    Assuming your main application file is named `main.py` and the application object is named `app`:
    ```bash
    uvicorn main:app --reload
    ```
    *The API will be accessible at **`http://127.0.0.1:8000`**.*

#### 2\. 🗺️ API Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| **GET** | `/docs` | Accesses the interactive **Swagger UI documentation** for testing and review. |

#### 3\. ✅ Testing the API

The easiest way to test the functionality is using the integrated Swagger UI:

1.  Navigate to **`http://127.0.0.1:8000/docs`** in your browser.
2.  Click **"Try it out"**.
3.  Upload a sample image file containing drones.
4.  Click **"Execute"**.

**Example API Response Screenshot:**

![Task 2 Output Screenshot](https://github.com/sayalidp/Globussoft_Assignment/blob/95d1516428321e7af741df59773891e7fa96e477/Task2(B)_DroneDetection/DroneDetection%20output%20SS/Screenshot%202025-11-18%20121044.png)

![Task 2 Output Screenshot](https://github.com/sayalidp/Globussoft_Assignment/blob/95d1516428321e7af741df59773891e7fa96e477/Task2(B)_DroneDetection/DroneDetection%20output%20SS/Screenshot%202025-11-18%20121100.png)

![Task 2 Output Screenshot](https://github.com/sayalidp/Globussoft_Assignment/blob/95d1516428321e7af741df59773891e7fa96e477/Task2(B)_DroneDetection/DroneDetection%20output%20SS/Screenshot%202025-11-18%20121125.png)

---

