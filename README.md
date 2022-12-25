# SpeechToText
ref:
## Prerequisites
```python
pip install git+https://github.com/salsina/persian-fluency-detector#egg=persian_fluency_detector
```
```python
pip install git+https://github.com/salsina/Persian-syllable-counter#egg=persian_syllable_counter
```
```python
pip install git+https://github.com/HassanJavaheri/SetupSpeechToText#egg=SetupSpeechToText
```

## speechToText
This function converts audio files to text files.
### Arguments
- audio_file_path: The path of the **.wav** audio file 
- function_name: The tool of speech-to-text converter user wants to use. it can have the values of “VOSK_wav”, “Google_wav” or “Microsoft”. If no argument is given, the default value would be “VOSK_wav”.
- output_text_directory: The directory in which the output text file would be saved. Default value is "notq_outputs"+os.sep+"text_files".
- subscription: The subscription for microsoft azure.
- region: The region for microsoft azure.

### Example
```python
speechToText("VOICE_AD\\titleA.mp3", function_name="Google_wav", output_text_directory="myDirectory\\myTextFiles")
```
