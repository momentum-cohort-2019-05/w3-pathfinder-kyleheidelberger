from PIL import Image
from pathfinder_classes import ElevationMap

def read_file_into_list(filename):
    """
    Open file and read line-by-line.
    """
    with open(filename) as file:
        return file.readlines()

def read_file_into_ints(filename):
    """
    Given a filename, read that file and then convert it to a list of lists of ints.
    """
    lines = read_file_into_list(filename)

    list_of_lists = []
    for line in lines:
        list_of_lists.append(read_line_of_ints(line))
    return list_of_lists

def read_line_of_ints(text):
    ints = []
    ints_as_strs = split_line(text)

    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints

def split_line(line):
    return line.split()

def draw_grayscale_gradient(filename, width, height):
    image = Image.new(mode='L', size=(width, height))
    for x in range (width):
        for y in range (height):
            image.putpixel((x, y), (int(x / width * 255),))
    image.save(filename)


if __name__ == "__main__":
    elevations = read_file_into_ints('elevation_small.txt')
    e_map = ElevationMap(elevations)
    
    draw_grayscale_gradient('map.png', 600, 600)
