# Tacotron 2 Phonetic

This repo contains attempts to improve the accuracy of NVIDIA's [Tacotron 2](https://github.com/NVIDIA/tacotron2) code. This is done by first converting all text to a phonetic representation using Kyubyong's [g2p](https://github.com/Kyubyong/g2p) library. The conversion is done automatically without invervention from the user. A terminating character is also added. These modifications necessitate changes in the model structure that are not compatible with the original code, so new models are required. A model which has been trained using the LJSpeech dataset can be found [here](https://drive.google.com/file/d/1aT1ieuQ8iQnZSrk-vN8nToxg75XgOsUS/view?usp=sharing). If you would like to train a model from scratch, the LJSpeech 1.1 dataset can be found [here](https://keithito.com/LJ-Speech-Dataset/). I recommend extracting transcription data from a modified metadata.csv file found [here](https://github.com/kwmkwm/LJSpeech1.1-expanded).

# Usage

For information on how to use this code please visit NVIDIA's original [Tacotron 2](https://github.com/kwmkwm/LJSpeech1.1-expanded) repository. You may also find [this Youtube video](https://www.youtube.com/watch?v=Y7gJAEIweSE) helpful.
