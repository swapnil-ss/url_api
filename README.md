# Image URL API using flask framework

This is a python script to read 1000s of image urls in a given csv file and the output will be an another csv file with the properties of the image urls present in the csv file
th 
This API takes input a CSV file in which 1000s of image urls are present. They may be correct or broken and there can be similar images in those urls. So this API checks all the urls present int the column of the csv file without even downloading the images(using PIL library and creating objects of the urls present). Then it gets the details of the image url like its size, dimensions and also stores phash value of the images to match similarity score with other images. We use multithreading to increase the speed of processing the data. And finally it stores the output in form of a csv file with the properties of the urls. And the output is a link to the csv file with the image properties as its output.



