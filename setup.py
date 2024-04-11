from setuptools import setup, find_packages

long_description = """
SummarAIze is a Python library for analyzing meeting/event video recordings with cloud hosted AI.

Save time and enhance efficiency by using AI to generate summaries, battle cards, meeting minutes, 
sales arguments and action item lists directly from recordings.
Hone your prompt engineering skills to distill the desired information.

## Technology

The video recording is transformed into a text transcript using the FFmpeg library 
and the OpenAI Whisper speech-to-text model. 
Then, the OpenAI ChatGPT-4 Turbo model analyzes and summarizes the transcript 
according to the user's prompt. The user interface (UI) is developed with the 
Tkinter library, part of the standard Python distribution, and styled using 
the ttkbootstrap library.

## Supported languages

From: https://platform.openai.com/docs/guides/speech-to-text/supported-languages

OpenAI lists the languages that exceeded <50% word error rate (WER),
which is an industry standard benchmark for speech to text model accuracy.

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese,
Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek,
Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean,
Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish,
Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog,
Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

## Requirements

- Ffmpeg needs to be installed and set in path. https://ffmpeg.org
- OpenAI API key to access Whisper and GPT4-Turbo models. https://platform.openai.com/docs/quickstart
- Python3.10 or newer

## Install Application

```python
python -m pip install summaraize
```

## Install FFmpeg

**Mac**

```bash
brew install ffmpeg
```

**Windows**

Follow instructions in this arcticle:
https://phoenixnap.com/kb/ffmpeg-windows

**Linux**

FFmpeg: https://ffmpeg.org//download.html#build-linux

Many Linux python distributions lack tkinter. Use distro package manager to install.
Note: Tkinter package name varies between distros.

## Run

```python
python -m summaraize
```

## Usage

1. Application will ask for OpenAI API key. Provide the API key
   - alternatively set OPENAI_API_KEY environment variable
2. Application will ask to select language and video recording file
   - video recording file is processed into a text transcipt
   - this may take several minutes
4. Application will ask a prompt to instruct ChatGPT4-turbo to extract the information from the transcript
   - this is called prompt engineering
   - try different prompts to see what works and what not
   - after prompt is ready, application will deliver prompt and the transcript to ChatGPT
   - creating summary in most cases takes less than a minute
5. Application will show the ChatGPT4-turbo created summary
   - you can copy the summary to clipboard or save the summary to a file. ChatGPT answers in markdown
     (md) format. You can ask bulleted or numbered lists and so on.
   - make a new summary by returning to summary view
   - application will answer in the language you selected unless you instruct otherwise in prompt
   - the application user interface texts are only in english
6. Close the application by closing the window
   - note application will not save the text transcript
   - to analyze other recording file, restart the application

## UI themes

Application support UI themes from:
https://ttkbootstrap.readthedocs.io/en/latest/themes/

list available themes:

```python
python -m summaraize -h
```

use a theme by giving theme name as an argument:

```python
python -m summaraize cyborg
```

"""

setup(
    name="summaraize",
    version="0.4",
    author="Jussi Löppönen",
    description="Analyze event video recordings with cloud hosted AI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/juslop/summaraize",
    packages=find_packages(where="src"),
    package_dir = {"": "src"},
    install_requires=["openai", "ttkbootstrap"],
    python_requires=">=3.10",
)
