import speech_recognition as sr
r = sr.Recognizer()

class CommandExecuter:
    def __init__(self, wav_file_path):
        self.wav_file_path = wav_file_path
        self.command_text = self.speech_to_text()
        self.id_and_list = self.execute_command(self.command_text)
    

    def speech_to_text(self):
        wav_file = sr.AudioFile(self.wav_file_path)
        with wav_file as source:
            audio = r.record(source)
        
        try:
            text = r.recognize_google(audio, language='tr-TR')
            print("Ses dosyası okunuyor")
            print (text)
            return text
        except Exception as e:
            print("Ses dosyası okunurken hata oluştu")
            print (e)
        return ""
    
    def execute_command(self, command_string):
        command_string = command_string.lower()
        id_and_command =[]
        if command_string =="":
            return id_and_command
        else:
            if "ışık" in command_string or "ışığı" in command_string or "işığı" in command_string:
               id_and_command.append("1") 
            elif "kapı" in command_string:
               id_and_command.append("2")
            elif "perde" in command_string:
               id_and_command.append("3")
            elif "sulama" in command_string or "sulamayı" in command_string or "su" in command_string or "suyu" in command_string:
               id_and_command.append("4")
            else:
                id_and_command.append(command_string)
                return id_and_command

            if "aç" in command_string:
               id_and_command.append("enable")
            elif "kapat" in command_string or "kapa" in command_string:
                id_and_command.append("disable")
            else:
                return id_and_command
        return id_and_command