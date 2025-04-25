# 🐛 MinibeastAI

**Smart Macroinvertebrate Identification with AI**

MinibeastAI is an open-source project that uses computer vision and machine learning to assist in the identification of aquatic macroinvertebrates. Designed to help streamline biological surveys and ecological research, MinibeastAI provides rapid image-based species suggestions and a peer review system to enhance dataset accuracy over time.

---

## 🚀 Features
- Upload macroinvertebrate images for automated AI identification
- Get top-3 prediction labels with confidence scores
- Peer review functionality to confirm or correct predictions
- Growing database of reviewed images to improve future model accuracy
- Built with Python, Flask, OpenCV, and deep learning

---

## 🏗️ Project Structure
```text
minibeast_ai/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # API and frontend routes
│   ├── model.py           # AI model loading and predictions
│   ├── utils.py           # Image preprocessing utilities
│   └── templates/
│       └── index.html     # Web frontend
├── static/
│   └── uploads/           # Uploaded images
├── run.py                 # App runner
└── requirements.txt       # Project dependencies
```
---

## 📸 Example Workflow
1. User uploads an aquatic macroinvertebrate image.
2. MinibeastAI predicts the top three possible species or groups.
3. User confirms or corrects the prediction.
4. Confirmed data is added to improve the training dataset over time.

---

## 🧰 Technologies Used
- [Python 3.11+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [TensorFlow](https://www.tensorflow.org/) or [PyTorch](https://pytorch.org/) (I haven't decided on a model backend)
- [SQLite](https://www.sqlite.org/) (lightweight database)

---

## 🛠️ Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/minibeast-ai.git
   cd minibeast-ai
   ```

2. **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

3. **Install Requirements**
    ```bash
    pip install -r requirements.txt
   ```

4. **Run the App**
    ```bash
    python run.py
   ```

5. **Open your browser to http://127.0.0.1.5000**

---

## 🌊 Future Roadmap

- Integrate a more advanced object detection model (YOLOv8, EfficientNet)

- User account system for contributors and peer reviewers

- Model retraining pipeline based on confirmed data

- Cloud storage for scalability

- Deployment to a public web server

---

## 🤝 Contributing

Contributions are welcome! Whether it's fixing bugs, improving performance, or adding features, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

