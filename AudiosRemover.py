from moviepy.editor import VideoFileClip
import os
import warnings
warnings.filterwarnings("ignore")



paths = ['./Day1/Camera/','./Day1/Moible/', #Path of videos to be removed audio.
        './Day2/','./Day3/',
        './Disassemble videos/Dell-XPS/',
        './Disassemble videos/iPhone 5s/',
        './Disassemble videos/OPTIPLEX 780/',
        './Disassemble videos/OPTIPLEX 960/',
        './Disassemble videos/OPTIPLEX 990/',
        './Disassemble videos/Optiplex 9020/',
        './Disassemble videos/Verizon-Kyocera E4610/']

savePaths = ['./D1withoutSounds/Camera/','./D1withoutSounds/Moible/', #Path of transferred videos without audio.
            './D2withoutSounds/','./D3withoutSounds/',
            './DisVidNoAudio/Dell-XPS/',
            './DisVidNoAudio/iPhone 5s/',
            './DisVidNoAudio/OPTIPLEX 780/',
            './DisVidNoAudio/OPTIPLEX 960/',
            './DisVidNoAudio/OPTIPLEX 990/',
            './DisVidNoAudio/Optiplex 9020/',
            './DisVidNoAudio/Verizon-Kyocera E4610/']


for n in range(len(paths)):
    path = paths[n]
    savePath = savePaths[n]
    filenames = os.listdir(path)
    for f in filenames:
        if f[-3:] == 'MP4' or f[-3:] == 'mp4' :
            print(f)
            videoClip = VideoFileClip(path+f)
            afterClipV = videoClip.without_audio() #Create new clip.
            afterClipV.write_videofile(savePath+f, verbose=False, logger=None) #Save videos after removing audio.
