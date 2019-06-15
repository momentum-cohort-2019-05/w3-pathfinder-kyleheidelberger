class ElevationMap:
    """
    ElevationMap is a class that takes a matrix (list of lists, 2D) of integers and can be used to generate an image of those elevations like a standard elevation map.
    """

    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        """
        Go through each row and get the minimum in each row. Then get the minimum of those numbers.
        """
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        """
        Get the maximum in each row, then get the maximum of those.
        """
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y):
        """
        Given an x, y coordinate, return the intensity level (used for grayscale in image) of the elevation at that coordinate.
        """
        elevation = self.elevation_at_coordinate(x, y)
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()

        return (elevation - min_elevation) / (max_elevation - min_elevation)