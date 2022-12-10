from scipy import misc
import numpy as np


class ImageProcessor():
    colorPercentages = [255,255,255]
    rectangeProportions = []
    tolerance = 0.2 #20% margin for error ex

    def __init__(self, percentages, tolerance):
        # Describes the ideal percent color distribution of RGB for sorting the image
        self.colorPercentages = percentages 
        
        # Represends the percent of error ColorShift will allow to return true
        self.tolerance = tolerance


    def someSortOfResult(self, imagePath):
        correctImage = self.findRectanges(imagePath)
        ## Return however the data format they want is here TODO

        return correctImage


    def findRectanges(self, imagePath):
        possibleRect = self.determineColorShift(imagePath)

        # dosomething TODO
        foundRectangels = None

        return 


    def determineColorShift(self, imagePath):
        # convert image into some sort of 2d array of RGB values.
        colors = misc.imread(imagePath) # WxHx3 array of RBG values misc.imread('example.png')
        result = None
    
        # Processing results to check if within tolerances 
        # TODO convert to gradient, rn we just check specific pixels. may not even be nessicary because checking
        # within a tolerance is basically the same thing.
        for row in colors:
            for col in colors: #Not starting with a np array because I am lazy, converting at the end.

                if(self.tolerance > abs(colors[row, col, 0] / self.colorPercentages[0])):
                    if(self.tolerance > abs(colors[row, col, 1] / self.colorPercentages[1])):
                        if(self.tolerance > abs(colors[row, col, 2] / self.colorPercentages[2])):
                            result[row][col] = True
                            continue
                
                result[row][col] = False

        return np.array(result)

    