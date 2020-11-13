import scipy
import subprocess
from glob import glob as globlin


def number_of_real_speakers(main_path):
    folder_paths = globlin(main_path)
    sum_files = 0
    for path in folder_paths:
        sum_files += len(globlin(path + '/*'))
    return sum_files

def convert_files_to_wav(mp3_paths, dest_path):
    counter = 0
    for i in range(len(mp3_paths)):
        if 'en-US-Wavenet-C' in mp3_paths.iloc[i]:
            counter += 1
            mp3_file_name = mp3_paths.iloc[i].replace('{DS_PATH}', '/Users/ahmadchaiban/Desktop/Guelph/6550_project/Data')
            wav_name = dest_path + '/' + mp3_file_name.split('/')[-1].split('.')[0] + '_set_C.wav'
            subprocess.run(f'ffmpeg -i {mp3_file_name} {wav_name}', shell=True, check=True)
            if counter == 13000:
                break


def read_spectogram_from_audio(path):
    pass

def load_generated_audio(gen_data_annotations_df):
    spectogram_files = []
    for i in range(len(gen_data_annotations_df)):
        path = gen_data_annotations_df['mr_link'].iloc[i].replace('{DS_PATH}', './Data')
        spectogram_image = 0
        spectogram_files.append()
        
    
        