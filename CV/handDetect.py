import cv2
import mediapipe as mp
import time
import os

# Inisialisasi MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Inisialisasi kamera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Buat folder untuk menyimpan gambar jika belum ada
save_dir = "C:/Users/LENOVO/Desktop/Python/CV"
os.makedirs(save_dir, exist_ok=True)

pTime = 0
img_counter = 1  # Nomor urut gambar
finger_tips = [4, 8, 12, 16, 20]  # ID landmark ujung jari

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image.")
        break

    flip_cam = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(flip_cam, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    fingers_up = 0
    
    # Gambar landmark tangan dan hitung jari yang terangkat
    if results.multi_hand_landmarks:
        for hand_idx, handLms in enumerate(results.multi_hand_landmarks):
            handedness = results.multi_handedness[hand_idx].classification[0].label
            cv2.putText(flip_cam, f"{handedness} Hand", (10, 100 + hand_idx * 30), 
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            mpDraw.draw_landmarks(flip_cam, handLms, mpHands.HAND_CONNECTIONS)
            
            # Ambil koordinat jari untuk mendeteksi jumlah jari yang terangkat
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = flip_cam.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
            
            if lmList:
                fingers_up = sum(1 for i in finger_tips[1:] if lmList[i][2] < lmList[i - 2][2])

    # Jika dua jari terangkat, simpan gambar
    if fingers_up == 2:
        img_name = os.path.join(save_dir, f"captured_image_{img_counter}.jpg")
        cv2.imwrite(img_name, flip_cam)
        print(f"Image saved: {img_name}")
        img_counter += 1
        time.sleep(1)  # Hindari pengambilan gambar berulang dalam waktu singkat
    
    # Hitung dan tampilkan FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(flip_cam, f"FPS: {int(fps)}", (10, 70), 
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    # Tampilkan frame
    cv2.imshow("Hand Tracking", flip_cam)
    
    # Keluar dengan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
