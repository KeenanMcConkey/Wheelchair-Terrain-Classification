# Wheelchair-Terrain-Classification

#### Terrain classification for power-assist wheelchairs using machine learning!

## Classification Framework

1. Collect 6-axis accelerometer and gyroscope data from IMU modules placed on three locations on the wheelchair: one on the wheelchair frame, and one on each wheel.
 
2. Divide IMU data into time windows, then extract features from each window, using direct extraction (e.g. Mean, Min) and transforms (FFT, PSD).

3. Run feature selection (mRMR or PCA) to find the most relevant features for classification.

4. Train multiple classifiers on the different feature vectors and compare the accuracy and testing time of these combinations.

5. Export best classifiers to real time environment.

## Current Notebooks

- `TerrainPreprocessing-GeneralData` - Imports raw IMU data collected from DAQ modules mounted to the wheelchair for each user, runs this data through filtering, windowing, feature extraction, and standardization, and processed data to csv to be used for classification.
- `TerrainClassification-AllData` - Imports all the types of preprocessed feature vectors from all users, runs feature selection and trains/compares classifiers on the feature vectors, and exports the best classifiers using joblib.
- `TerrainClassification-WindowSize` - Imports all the types of preprocessed feature vectors for all the different window sizes, then trains/compares classifiers according to window size.

## Notable Dependencies

- Jupyter: <https://jupyter.org/>
- Pandas: <https://pandas.pydata.org/>
- Scikit Learn: <https://scikit-learn.org/stable/>
- PymRMR: <https://pypi.org/project/pymrmr/>
- Joblib: <https://joblib.readthedocs.io/en/latest/>

## Archived Notebooks

- `TerrainClassification-OldSetup`: Runs various preprocessing and visualization on raw data `imu_data/` from wheelchair data acquisition modules and exports processed data `processed_data/` as .csv files, then run feature selection and different classifiers.
- `TerrainClassification-OldSetup-Preprocessed`: For running machine learning solely off of exported .csv data, to be used once data from all three modules is integrated into a single .csv file.
- `TerrainClassification-RemoteData` - Processes data and runs classification on remote-controlled wheelchair data.
- `TerrainClassification-WindowSize-RemoteData` - Compares metrics of different window sizes for remote wheelchair data.
- `Terrainclassification-<User><Power>Data` - Instances of the same notebook running on data collected from different users on different wheelchairs.

### Glossary

- `Power Assist vs Manual Wheelchair` - A power assist (specifically a PAPAW) is similar to a standard manual wheelchair, but has hub motors attached to the wheels that boosts user torque applied to pushrims on the wheels.
- `Dataset` - Data recorded on one terrain, using a specific movement pattern, by a single user for a set time.
- `Data Window` - A portion of a `Dataset`, from which features are extracted.
- `Direction / Axes` - Collectively linear acceleration or gyroscope in $x,y$ or $z$.
- `Feature Vector` - Any feature of the data that can be used to classify terrain, i.e. Time Domain Features, Frequency Domain Features, FFTs, PSDs.
- `Transformed Features` - Features extracted by performing a transform on a data window, either FFT or PSD (which is usually just log(PSD)). Each frequency bin of a transform corresponds to a feature of a feature vector.
- `Time Domain Features` - Features that are extracted directly from time domain data in a data window, e.g. Mean, Min, Max, Skew, etc.
- `Frequency Domain Features` - Features that are extracted from frequency domain data, i.e. PSD transforms, e.g. Variance Frequency, Mean Square Frequency, etc.
- `Placement` - One of three IMU placements on the wheelchair, i.e. Middle, Left, or Right, or Synthesis data which is computed by the wheelchair DAQ. Middle refers to the IMU mounted to the wheelchair frame, while Left and Right refer to the IMUs mounted on the left and right wheels.q

#### Created by Keenan McConkey
