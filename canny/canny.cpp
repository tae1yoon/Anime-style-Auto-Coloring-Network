/* 
input path should be put in argv[1] with *.jpg
out path should be put in argv[2] with *.jpg
*/
#include "opencv2/imgproc.hpp"
#include "opencv2/core.hpp"
#include "opencv2/flann/miniflann.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/highgui.hpp"
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace cv;
using namespace std;

void writeCSV(string filename, Mat m);

int main(int argc, char* argv[])
{
    Mat src = imread(argv[1]);
    if (!src.data)
    {
        cout << "no input";
        return -1;
    }
    
    Mat gray, edge, blured_image,edge_resized; 
    //Mat lab_convert, upscaled;
    //Mat tmp gray_resized;
    //Mat near,linear,area,cubic,lanz;
    //resize(src,src,Size(112,112));
    cvtColor(src,gray,COLOR_BGR2GRAY);
    blur(gray, blured_image,Size(3,3));
    Canny(blured_image,edge,20,80,3,false);
    
    //corner detection
    //int threshodld = 9;
    //vector<KeyPoint> key;
    //FAST(gray,key,threshold,true);
   
    //resizing to 112X112
    resize(edge,edge_resized,Size(112,112),0,0,INTER_AREA);
    //resize(gray,gray_resized,Size(112,112),0,0,INTER_AREA);
    //resize(src,tmp,Size(112,112),0,0,INTER_AREA);

    //cvtColor(tmp,lab_convert,CV_BGR2Lab);

    //split lab to each channels;
    //vector<Mat> lab_channels;
    //split(lab_convert,lab_channels);
   
    //cvtColor(lab_convert,tmp,CV_Lab2BGR);
    //first try of seperate channels
    /*
    int step = lab_convert.step;
    int channels = lab_convert.channels();
    for (int i = 0; i < lab_convert.rows(); i++) {
        for (int j = 0; j < lab_convert.cols(); j++) {
            Point3_<uchar> pixelData;
            pixelData.x = lab_convert.data[step*i + channels*j + 0];
            pixelData.y = lab_convert.data[step*i + channels*j + 1];
            pixelData.z = lab_convert.data[step*i + channels*j + 2];
        }
    }
    resize(edge,near,Size(112,112),0,0,INTER_NEAREST);
    resize(edge,linear,Size(112,112),0,0,INTER_LINEAR);
    resize(edge,area,Size(112,112),0,0,INTER_AREA);
    resize(edge,cubic,Size(112,112),0,0,INTER_CUBIC);
    resize(edge,lanz,Size(112,112),0,0,INTER_LANCZOS4);

    imshow("linear",linear);
    imshow("near",near);
    imshow("area",area); 
    imshow("cubic",cubic);
    imshow("lanz",lanz);

    waitKey(0);
    //by checking 5 different interoplation
    //AREA is the best choice for denoizing.
    */



    string edge_out = argv[2];
    //L*: 0-255 (elsewhere is represented by 0 to 100 in R, L <- L*255/100)
    //a*: 0-255 (elsewhere is represented by -127 to 127 in R, a <- a + 128)
    //b*: 0-255 (elsewhere is represented by -127 to 127 in R, b < b + 128)
	/*
    L_channel = lab_out + argv[3];
    A_channel = lab_out + argv[4];
    B_channel = lab_out + argv[5];

    imwrite(gray_out,gray_resized);
    */
    imwrite(edge_out,edge_resized);
    /*
    writeCSV(L_channel,lab_channels[0]);
    writeCSV(A_channel,lab_channels[1]);
    writeCSV(B_channel,lab_channels[2]);
    */
    //imwrite(lab_out,tmp);
    //imshow("L channels",lab_channels[0]);
    //imshow("A channels",lab_channels[1]);
    //imshow("B channels",lab_channels[2]);
    //waitKey(0);
    //writeCSV(lab_out,lab_convert);

    return 1;
}
void writeCSV(string filename, Mat m)
{
   ofstream myfile;
   myfile.open(filename.c_str());
   myfile<< format(m, cv::Formatter::FMT_CSV) << std::endl;
   myfile.close();
}
/*
Mat gray(Mat input)
{
    if(!input.data)
    {
        cout << "gray error"<<endl;
        assert();
    }
    Mat gray;
    cvtColor(input,gray,COLOR_BGR2GRAY);
    return gray;
}
Mat edge(Mat gray_input)
{
    if(!gray_input.data)
    {
        cout << "edge error"<<endl;
        assert();
    }

    Mat canny;
    Mat blured_image;
    
    blur(gray_input, blured_image,Size(3,3));
    Canny(blured_image,canny,20,80,3,false);
    
    return canny;   
}
Mat resize(Mat src,int x,int y)
{
    if(!src.data)
    {
        cout << "resize error" <<endl;
        assert();
    }
    Mat resized;
    resize(src,out,Size(x,y));
    return resized;
}
Mat Lab(Mat input)
{
    if(!input.data)
    {
        cout << "LAB conversion error"<<endl;
        assert();
    }
    Mat lab_convert;
    cvtColor(input,lab_convert,CV_BGR2Lab);
    return lab_convert;
}
*/

