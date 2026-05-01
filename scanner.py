import cv2

def scan_camera():
    print("Booting Hardware Scanner on Index 0...")
    
    # We use DirectShow because it's the standard Windows driver level
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("CRITICAL ERROR: Cannot access camera. Is Lenovo Vantage or another app using it?")
        return

    print("Camera Unlocked. Testing bandwidth...\n")

    resolutions = [
        ("1440p", 2560, 1440),
        ("1080p", 1920, 1080),
        ("720p", 1280, 720),
        ("480p", 640, 480)
    ]

    for name, w, h in resolutions:
        # 1. Demand the resolution
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        
        # 2. Check what the camera actually agreed to
        actual_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        actual_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if int(actual_w) == w and int(actual_h) == h:
            print(f"[ O K ] {name} ({w}x{h}) is SUPPORTED.")
        else:
            print(f"[LOCKED] Requested {name}, but camera forcefully downgraded to {actual_w}x{actual_h}")

    cap.release()
    print("\nScan complete. Awaiting orders.")

if __name__ == "__main__":
    scan_camera()