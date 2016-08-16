cp -f source.jpg basic_resize/source.jpg
cp -f target.jpg basic_resize/target.jpg
cd basic_resize/
python resize.py
mv -f basic_source.jpg ../kMeans/basic_source.jpg
mv -f basic_target.jpg ../kMeans/basic_target.jpg
mv -f source4knn.jpg ../kMeans/source4knn.jpg
mv -f 'basic_target(224).jpg' ../convnet/'basic_target(224).jpg'
cd ..

cp -f source.jpg FAST/source.jpg
cp -f target.jpg FAST/target.jpg
cd FAST/
python FAST.py
mv -f FAST_source.csv ../kMeans/FAST_source.csv
mv -f FAST_target.csv ../kMeans/FAST_target.csv
cd ..

cp -f source.jpg canny/source.jpg
cp -f target.jpg canny/target.jpg
cd canny/
./canny source.jpg canny_source.jpg
./canny target.jpg canny_target.jpg
mv -f canny_source.jpg ../kMeans/canny_source.jpg
mv -f canny_target.jpg ../kMeans/canny_target.jpg
cd ..

cp -f source.jpg lab/source.jpg
cp -f target.jpg lab/target.jpg
cd lab/
./lab source.jpg L_source.jpg A_source.jpg B_source.jpg
./lab target.jpg L_target.jpg A_target.jpg B_target.jpg
cd ..

cd kMeans/
Rscript kMeans.R
mv -f input_matrix1.csv ../convnet/input_matrix1.csv
mv -f input_matrix2.csv ../convnet/input_matrix2.csv
mv -f 'input_matrix1(canny).csv' ../convnet/'input_matrix1(canny).csv'
mv -f 'input_matrix2(canny).csv' ../convnet/'input_matrix2(canny).csv'
mv -f 'input_matrix1(FAST).csv' ../convnet/'input_matrix1(FAST).csv'
mv -f 'input_matrix2(FAST).csv' ../convnet/'input_matrix2(FAST).csv'
mv -f X1.csv ../convnet/X1.csv
mv -f X2.csv ../convnet/X2.csv
mv -f Y.csv ../convnet/Y.csv
mv -f testX.csv ../convnet/testX.csv
mv -f testY.csv ../convnet/testY.csv
mv -f label-color.rds ../convnet/label-color.rds
mv -f 'X1(canny).csv' ../convnet/'X1(canny).csv'
mv -f 'X2(canny).csv' ../convnet/'X2(canny).csv'
mv -f 'testX(canny).csv' ../convnet/'testX(canny).csv'
mv -f 'X1(FAST).csv' ../convnet/'X1(FAST).csv'
mv -f 'X2(FAST).csv' ../convnet/'X2(FAST).csv'
mv -f 'testX(FAST).csv' ../convnet/'testX(FAST).csv'
cd ..

cd convnet/
#source ~/tensorflow/bin/activate
python convnet.py
python predict.py
#deactivate
Rscript label2pic.R
mv -f result.jpg ../result.jpg
rm -f 'input_matrix1(canny).csv'
rm -f 'input_matrix2(canny).csv'
rm -f 'input_matrix1(FAST).csv'
rm -f 'input_matrix2(FAST).csv'
rm -f X1.csv
rm -f X2.csv
rm -f Y.csv
rm -f testX.csv
rm -f testY.csv
rm -f 'X1(canny).csv'
rm -f 'X2(canny).csv'
rm -f 'testX(canny).csv'
rm -f 'X1(FAST).csv'
rm -f 'X2(FAST).csv'
rm -f 'testX(FAST).csv'

cd ..
cp -f result.jpg lab/result.jpg
cd lab/
./lab result.jpg L_result.jpg A_result.jpg B_result.jpg
cd ..
