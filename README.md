# VisionID
The Automatic Attendance System uses facial recognition to identify individuals and log their attendance. It captures video from a webcam, recognizes faces, and records attendance in a CSV file.

**How It Works**
  **Initialization**

    Sets up folders for known faces and attendance data.
    Loads face images and encodes them for recognition.
  **Video Capture**

    Captures real-time video from the webcam.
    Detects and recognizes faces in each frame.
  **Attendance Logging**

    Marks attendance in a CSV file if a recognized face is detected.
    
**Project Structure**

VisionID-system/
│
├── main.py                   # The main script for the attendance system
├── attendance_data/          # Folder for storing attendance records
│   └── attendance.csv        # CSV file created automatically
├── known_people/             # Folder with images of known individuals
    └── person1.jpg           # Sample image file
    
**Clone the Repository**

    git clone https://github.com/yourusername/automatic-attendance-system.git
    cd automatic-attendance-system
    
**Install Required Libraries**

**Run the Application**

Start the attendance system by running the main.py script

The webcam will activate. Press 'q' to exit the video stream.
