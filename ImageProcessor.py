

class ImageProcessor():
    colorPercentages = [255,255,255]

    def __init__(self, percentages):
        # Describes the ideal percent color distribution of RGB for sorting the image
        self.colorPercentages = percentages 

    def processImage(self, image):
        result = None
        # Process image here, and return result. 
        # Result should be a 2D array of values between 0 -> 1 in terms of how close to correct 
        # colorPercentages they are.

        return result