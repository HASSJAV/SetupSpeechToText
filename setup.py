from setuptools import setup, find_packages

with open("README.md", "r", encoding="mbcs") as readme_file:
    readme = readme_file.read()
    ''''''

setup(
    name='SpeechToText',
    version='1.0.0',
    description='SpeechToText is a Python base tool collected and developed for speech and language processing in Persian',
    long_description=readme,
    author='Nbic',
    long_description_content_type="text/markdown",
    packages=find_packages(include=["notq*"]),
    url="https://github.com//HASSJAV/SetupSpeechToText",
install_requires=['torchaudio ==0.9.0',
                        'pydub ==0.25.1',
                        'speechRecognition ==3.8.1',
                        'numpy ==1.19.2',
                        'tqdm ==4.61.2',
                        'transformers ==4.11.2',
                        'torch ==1.9.0',
                        'wget ==3.2',
                        'ffmpeg==0.2.0,
                        'glob2==0.4.1,
                        'cryptography==36.0.2,
                        'pydub==0.25.1,
                        'librosa==0.9.2,
                        'fabric==2.7.1,
                        'persian_fluency_detector',
                        'persian_syllable_counter'],
    dependency_links=['https://github.com/salsina/persian-fluency-detector#egg=persian_fluency_detector', 
                      'https://github.com/salsina/Persian-syllable-counter#egg=persian_syllable_counter'],
    
    keywords=['python', 'first package'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]
)
