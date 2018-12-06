from scipy import io
import numpy as np
from sklearn.svm import SVC
from sklearn.utils import shuffle
import math

# human fixation rate defined as 1 - omission rate


def extract_omission_rate(data, om_rates):
    """extract sentence level omission rate from Matlab struct"""
    for sent in data:
        om_rates.append(sent.omissionRate)


def main():

    subjects = ["ZJN", "ZPH", "ZAB", "ZJM", "ZKB", "ZKH", "ZMG", "ZGW", "ZKW", "ZDM"]

    omission_rates = []
    for subject in subjects:
        filename_nr = "/Users/norahollenstein/Downloads/results_NR/results" + subject + "_NR.mat"
        filename_sr = "/Users/norahollenstein/Downloads/results_SR/results" + subject + "_SR.mat"
        # filename_tsr = "/Users/norahollenstein/Downloads/results_TSR/results" + subject + "_TSR.mat"
        data_nr = io.loadmat(filename_nr, squeeze_me=True, struct_as_record=False)['sentenceData']
        data_sr = io.loadmat(filename_sr, squeeze_me=True, struct_as_record=False)['sentenceData']
        # data_tsr = io.loadmat(filename_tsr, squeeze_me=True, struct_as_record=False)['sentenceData']

        extract_omission_rate(data_nr, omission_rates)
        extract_omission_rate(data_sr, omission_rates)
        # extract_omission_rate(data_tsr, omission_rates)

        # print(np.mean(omission_rates))
        subj_fixation_rate = 1 - np.mean(omission_rates)

        print(subject, "fixation rate in ZuCO:", subj_fixation_rate)

    fixation_rate = 1 - np.mean(omission_rates)
    print("\n------------\nHuman average fixation rate in ZuCO:", fixation_rate)


if __name__ == '__main__':
    main()
