# Wheelchair-Terrain-Classification

Terrain classification for power-assist wheelchairs using machine learning!

## Classification Framework

1. Collect accelerometer and gyroscope data from IMU module placed in three locations on the wheelchair: one on the wheelchair frame, and one on each wheel
 
2. Divide IMU data into time windows, then extract features (e.g. Mean, Min, etc) and transforms from each window (FFT and PSD)

3. Run mRMR feature selection to find the most relevant features of the data

4. Train multiple classifiers and compare their accuracy and testing time

5. Export best classifier to real time environment

## Notebooks

- `TerrainClassification`: Runs various preprocessing and visualization on raw data `imu_data/` from wheelchair data acquisition modules and exports processed data `processed_data/` as .csv files, then run feature selection and different classifiers
- `TerrainClassification-Preprocessed`: For running machine learning solely off of exported .csv data, to be used once data from all three modules is integrated into a single .csv file
- `TerrainClassification-WindowSize`: For comparing different metrics with varying window size

## Notable Dependencies

- Jupyter: <https://jupyter.org/>
- Pandas: <https://pandas.pydata.org/>
- Scikit Learn: <https://scikit-learn.org/stable/>
- PymRMR: <https://pypi.org/project/pymrmr/>

#### Created by Keenan McConkey
