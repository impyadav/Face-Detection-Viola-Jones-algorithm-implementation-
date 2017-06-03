from haar_features import *

start_time = time.time()

haar_features = []
count = 0

for f in feature_type:
    print 'Im in first loop, feature no :', f
    for width in range(f[0], frame_size, f[0]):
        print 'Im in second loop, width is :', width
        for height in range(f[1], frame_size, f[1]):
            print 'Im in third loop, height is :', height
            for x in range(frame_size - width):
                print 'Im in fourth loop, x coordinate is : ', x
                for y in range(frame_size - height):
                    print 'Im in fifth loop, y coordinate is : ', y
                    haar_features.append(haar_feature_value(integral_image_done, f, (x,y), width, height))
                    count += 1
                    print '...still counting the haar features and current count is : ', count
                    print 'f value : ', f, ', width value : ', width, ',height value : ', height, 'x and y coordinates are : ', x , y



print haar_features
print 'Execution time : ', time.time() - start_time
print 'Total no of features: ', count