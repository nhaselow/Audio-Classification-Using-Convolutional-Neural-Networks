# Stats 479 Deep Learning Final Project Code Repository

This repo contains the code used to clean the data for "Audio Classification Using Convolutional Neural Networks", a paper written for Sebastian Raschka's Deep Learning course at UW-Madison. It takes data scraped from the Google Audioset and converts a select set of them into spectrograms that we used to train a Convolutional Neural Network. All code has been written for and tested in Python 2.7.10.

## Selecting a Subset of the Audioset

Google Audioset gives a [download link](https://research.google.com/audioset/download.html) for 2 million audio files, but we didn't want to use all 2 million due to time and computing power constriants. **'data_subset_maker.py'** takes the unbalanced training set, selects the first 500 examples for each of 10 specified classes, and creates a new csv file 'unbalanced_subset.csv' that is used to download the subset. Run the script with:

> $ python data_subset_maker.py

## Downloading the Audio Files

We used a script written by [Alex Nichol](https://github.com/unixpickle) to scrape the data from YouTube. He published the scripts on [his GitHub](https://github.com/unixpickle/audioset), and we used the download function to scrape the data. Pipe 'unbalanced_subset.csv' into his script:

> $ cat unbalanced_subset.csv | ./download.sh

## Converting to Spectrograms

To convert the audio files into spectrograms, put the zipped audio files (.wav.gz) into a folder 'audio_files', and create two empty directories 'file_in_progress' and 'spectrograms' on the same level in your directory structure. Then, run:

> $ python spectrogram_maker.py

## Link Images with their Class Labels

To train a model using the spectrograms, we need a clean csv linking the file names to their respective class label. To run this code, you will need to download the [Google Audioset Ontology](https://github.com/audioset/ontology) and put the directory containing the json file on the same level as unbalanced_subset.csv. To create the new csv, run:

> $ python clean_data.py
