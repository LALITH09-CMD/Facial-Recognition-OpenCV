# Face Recognition Project

## Overview
This project implements a face recognition system using OpenCV and LBPH (Local Binary Patterns Histograms). The system captures images, trains a model, and recognizes faces in real time.

## Installation
Follow these steps to set up the project:

1. **Install Python** (Make sure you have Python 3.7 or higher)
2. **Install Dependencies** by running:
   ```sh
   pip install opencv-contrib-python numpy
   ```

## Folder Structure
```
Face-Recognition/
│── dataset/                # Stores captured images for training
│── trainer/                # Stores trained model (trainer.yml)
│── capture_faces.py        # Script to capture images for dataset
│── train_model.py          # Script to train the model
│── recognize_faces.py      # Script to recognize faces
│── haarcascade_frontalface_default.xml # Pre-trained face detection model
│── README.md               # Project documentation
```

## Steps to Run the Project

### Capture Images
Run the script to capture images and store them in the dataset folder:
```sh
python capture_faces.py
```
Follow the on-screen instructions to save images of different individuals.

### Train the Model
Once images are collected, train the model:
```sh
python train_model.py
```
This will generate `trainer.yml` in the `trainer/` folder.

### Recognize Faces
After training, run the recognition script:
```sh
python recognize_faces.py
```
The script will detect and recognize faces in real-time using your webcam.

## Troubleshooting
- **Error: `cv2.face.LBPHFaceRecognizer_create()` not found**
  - Ensure you installed `opencv-contrib-python`
  ```sh
  pip install opencv-contrib-python
  ```
- **FileNotFoundError: 'trainer/trainer.yml'**
  - Ensure you have trained the model before running face recognition.
- **Dataset folder not found?**
  - Manually create a `dataset/` folder before running `capture_faces.py`.

## Future Enhancements
- Improve accuracy by collecting more training images.
- Implement real-time attendance system.
- Use deep learning for better results.

## Author
RAMESH LALITH KUMAR

---
This documentation ensures a smooth setup and execution of the project.
