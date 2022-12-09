

class ImageProcessor():
    colorPercentages = [255,255,255]
    tolerance = 0.2 #20% margin for error ex

    def __init__(self, percentages, tolerance):
        # Describes the ideal percent color distribution of RGB for sorting the image
        self.colorPercentages = percentages 

        # Represends the percent of error ColorShift will allow to return true
        self.tolerance = tolerance


    def someSortOfResult(self, image):
        correctImage = self.findRectanges(image)
        ## Return however the data format they want is here TODO

        return correctImage

    def findRectanges(self, image):
        colors = self.determineColorShift(image)
        rectifiedImage = 
        # Do mathing here to determine rectangles
        for row in colors:
            for col in colors:
                # dosomething TODO


        return 


    def determineColorShift(self, image):
        # convert image into some sort of 2d array of RGB values.
        colors = image.turnTo2D() # something like this. needs to be written. TODO
        result = None
    
        # Processing results to check if within tolerances
        for row in colors:
            for col in colors:

                if(self.tolerance > abs(colors[row][col].red / self.colorPercentages.red)):
                    if(self.tolerance > abs(colors[row][col].green / self.colorPercentages.green)):
                        if(self.tolerance > abs(colors[row][col].blue / self.colorPercentages.blue)):
                            result[row][col] = True
                            continue
                
                result[row][col] = False

        return result

    