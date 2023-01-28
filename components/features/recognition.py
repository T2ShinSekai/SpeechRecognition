import whisper
import os

class AudioRecognition:
    
    PRCOESS_MODEL = 'base'
    LANGUAGE_USED = 'Japanese'

    def recognize(self, input_file_path: str, output_dir: str) -> None:

        model = whisper.load_model(self.PRCOESS_MODEL)

        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(input_file_path)
        audio = whisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # detect the spoken language
        # _, probs = model.detect_language(mel)
        # print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)

        # if output is required
        if output_dir:
            path = os.path.abspath(output_dir) + "\script.txt"
            with open(path, "w", encoding='utf-8') as file:
                file.write(result.text)

        return result.text





