import argparse
import os
from components.features import AudioRecognition


def init_args():
    parser = argparse.ArgumentParser(description="Audio Text Program")
    parser.add_argument('--audio', type=str, required=True, help='Input audio file')
    parser.add_argument('--output-dir', type=str, required=False, help='Output folder if text is required')
    parser.add_argument('--model', type=str, default='base', required=False, help='available mode is tiny, base, small, medium, large')
    parser.add_argument('--language', type=str, default='Japanese', required=False, help='the language which is spoken on audio')
    args = parser.parse_args()
    return args


def main():
    args = init_args()
    audio = args.audio

    AudioRecognition.PRCOESS_MODEL = args.model
    AudioRecognition.LANGUAGE_USED = args.language

    audioController = AudioRecognition()
    audio_path = os.path.abspath(audio)
    text = audioController.recognize(audio_path, output_dir=args.output_dir)

    print(text)


if __name__ == '__main__':
    main()






