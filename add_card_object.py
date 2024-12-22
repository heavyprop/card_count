import cv2
import numpy as np

class CardDetector:
    def __init__(self):
        self.detected_cards = []
        
    def preprocess_image(self, image):
        """Preprocess the image for better card detection"""
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Apply threshold
        _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
        return thresh

    def find_cards(self, image):
        """Find all cards in the image"""
        # Get image dimensions
        height, width = image.shape[:2]
        min_card_area = (width * height) / 50  # Minimum card size
        max_card_area = (width * height) / 2   # Maximum card size
        
        # Find contours
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        cards = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if min_card_area < area < max_card_area:
                # Approximate the contour to a polygon
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
                
                # If we have a rectangle (4 points), it might be a card
                if len(approx) == 4:
                    cards.append(approx)
        
        return cards

    def extract_card_roi(self, image, contour):
        """Extract the region of interest (top-left corner) of the card"""
        # Get the bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        
        # Extract the top-left corner region (where the card value typically is)
        roi = image[y:y + int(h/4), x:x + int(w/4)]
        
        return roi, (x, y, w, h)

    def detect_cards(self, image_path):
        """Detect all cards in the image and store their values"""
        # Read image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Could not read the image")
        
        # Create a copy for drawing
        display = image.copy()
        
        # Preprocess image
        processed = self.preprocess_image(image)
        
        # Find cards
        cards = self.find_cards(processed)
        
        # Process each card
        for i, card in enumerate(cards):
            # Extract ROI
            roi, (x, y, w, h) = self.extract_card_roi(processed, card)
            
            # Draw rectangle around card
            cv2.drawContours(display, [card], -1, (0, 255, 0), 2)
            
            # Show ROI for debugging
            cv2.imshow(f'Card {i+1} ROI', roi)
            
            # Add placeholder value to array (you'll need to implement actual value detection)
            self.detected_cards.append(f"Card {i+1}")
            
            # Draw card number on image
            cv2.putText(display, f'Card {i+1}', (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Show the processed image
        cv2.imshow('Detected Cards', display)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return self.detected_cards

def main():
    try:
        # Initialize detector
        detector = CardDetector()
        
        # Replace with your image path
        image_path = "./card.png"  # Update this with your image path
        
        # Detect cards
        detected_cards = detector.detect_cards(image_path)
        
        # Print results
        print("Detected cards:", detected_cards)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()