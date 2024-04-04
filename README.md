# minutes

A Python library for analyzing meeting/event video recordings with cloud hosted AI.
![minutes-screenshot-1](https://github.com/juslop/minutes/assets/1512110/dbe5bd12-36f8-4d2d-9e34-5a037fea7b7b)
![minutes-screenshot-2](https://github.com/juslop/minutes/assets/1512110/0f154418-41e9-4b5c-8e29-f75c557924f4)

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
- Python3.7 or newer

## Install Application

```bash
python -m pip install minutes
```

## Install FFmpeg

**Mac**

```bash
brew install ffmpeg
```

**Windows**

Follow instructions in this arcticle:
https://phoenixnap.com/kb/ffmpeg-windows


## Run

```bash
python -m minutes
```

## UI themes

Application support UI themes from:
https://ttkbootstrap.readthedocs.io/en/latest/themes/

list available themes:

```bash
python -m minutes -h
```

use a theme by giving theme name as an argument:

```bash
python -m minutes cyborg
```