import scipy
from glob import glob as globlin


def number_of_real_speakers(main_path):
    folder_paths = globlin(main_path)
    sum_files = 0
    for path in folder_paths:
        sum_files += len(globlin(path + '/*'))
    return sum_files


def read_spectogram_from_audio(path):
    pass

def load_generated_audio(gen_data_annotations_df):
    spectogram_files = []
    for i in range(len(gen_data_annotations_df)):
        path = gen_data_annotations_df['mr_link'].iloc[i].replace('{DS_PATH}', './Data')
        spectogram_image = 0
        spectogram_files.append()
        