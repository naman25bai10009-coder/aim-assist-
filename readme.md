

A real-time, computer vision-based aim-assist project designed to detect and track targets dynamically. 

This project explores the application of deep learning models in real-time environments, focusing on low-latency object detection and coordinate mapping. 

*Disclaimer: This project was built strictly for educational purposes and AI research, demonstrating real-time computer vision capabilities.*

## 🛠 Tech Stack
* **Language:** Python
* **Computer Vision / AI:** YOLOv8
* **Image Processing:** OpenCV 
* **Libraries:** PyTorch, NumPy, MSS (for fast screen capture)

## ✨ Key Features
* **Real-Time Detection:** Utilizes YOLOv8 for high-speed, accurate target identification.
* **Low Latency Processing:** Optimized screen grabbing and inference pipeline to ensure minimal input lag.
* **Coordinate Tracking:** Calculates bounding box centers to determine the optimal tracking trajectory.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/sandevistan-v1.git](https://github.com/yourusername/sandevistan-v1.git)
   cd sandevistan-v1
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the main detection script:
```bash
python main.py
```
*(Make sure to configure your target window or screen region in the `config.py` file before running).*

## 📌 Future Improvements
* Transitioning to TensorRT for even faster inference times.
* Implementing advanced smoothing algorithms for the tracking trajectory.
* Expanding the training dataset for edge-case environments.
```

This makes you look like a serious developer who understands how to document their work. 

Do you need help generating the `requirements.txt` file for this, or are you good to go on pushing this to GitHub?
