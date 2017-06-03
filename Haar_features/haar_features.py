# from enum import Enum
import numpy as np
from IntegralImage import *

integral_image_done = summed_mat(original_mat)

def enum(**enums):
    return type('Enum', (), enums)


feature = enum(Two_horz = (1,2), Two_vert = (2,1),  Three_horz = (1,3), Three_vert = (3,1), four_sq = (2,2))
feature_type = [feature.Two_horz, feature.Two_vert, feature.Three_horz, feature.Three_vert, feature.four_sq]
frame_size = 24

def haar_feature_value(integral_image, type_of_feature, start_position, width, height):

    print '****************Haar features calculation starts**************\n'
    haar_value = 0
    start_position = (start_position[0], start_position[1])


    if type_of_feature == feature.Two_horz:
        bright = get_area(integral_image_done, start_position, (start_position[0]+width/2, start_position[1]+height))
        dark   = get_area(integral_image_done, (start_position[0]+width/2, height), (start_position[0]+width, start_position[1]+height))
        haar_value = bright - dark

    elif type_of_feature == feature.Two_vert:
        bright = get_area(integral_image_done, start_position, (start_position[0]+width, start_position[1]+height/2))
        dark   = get_area(integral_image_done, (start_position[0], start_position[1]+height/2), (start_position[0]+width, start_position[1]+height))
        haar_value = bright - dark

    elif type_of_feature == feature.Three_horz:
        bright1 = get_area(integral_image_done, start_position, (start_position[0]+width/3, start_position[1]+height))
        dark    = get_area(integral_image_done, (start_position[0]+width/3, start_position[1]), (start_position[0]+(2*width)/3, start_position[1]+height))
        bright2 = get_area(integral_image_done, (start_position[0]+(2*width)/3, start_position[1]), (start_position[0]+width, start_position[1]+height))
        haar_value = (bright1 + bright2) - dark

    elif type_of_feature == feature.Three_vert:
        bright1 = get_area(integral_image_done, start_position, (start_position[0]+width, start_position[1]+height/3))
        dark    = get_area(integral_image_done, (start_position[0], start_position[1]+height/3),  (start_position[0]+width, start_position[1]+(2*height)/3))
        bright2 = get_area(integral_image_done, (start_position[0], start_position[1]+(2*height)/3), (start_position[0]+width, start_position[1]+height))
        haar_value = (bright1 + bright2) - dark

    elif type_of_feature == feature.four_sq:
        bright1 = get_area(integral_image_done, start_position, (start_position[0]+width/2, start_position[1]+height/2))
        dark1   = get_area(integral_image_done, (start_position[0]+width/2, start_position[1]), (start_position[0]+width, start_position[1]+height/2))
        dark2   = get_area(integral_image_done, (start_position[0], start_position[1]+height/2), (start_position[0]+width/2, start_position[1]+height))
        bright2 = get_area(integral_image_done, (start_position[0]+width/2, start_position[1]+height/2),   (start_position[0]+width,start_position[1]+height))
        haar_value = ((bright1 + bright2) - (dark1 + dark2))

    return haar_value


def get_vote(Haar_value, polarity, threshold):
    return 1 if Haar_value < polarity * threshold else -1

