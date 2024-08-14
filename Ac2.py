import sounddevice as sd
import wave
import speech_recognition as sr

def guardaraudio(nome_arquivo,duracao=10,taxa=44100):
    audio = sd.rec(int(10*taxa),samplerate=taxa, channels=1,dtype='int16')
    print("Fale os itens que deseja adicionar a sua lista de compras...")
    sd.wait()
    with wave.open(nome_arquivo,'wb') as wb:
        wb.setsampwidth(2)
        wb.setnchannels(1)
        wb.setframerate(taxa)
        wb.writeframes(audio.tobytes())

    print("Gravado com sucesso")
guardaraudio("sla.wav",10)



