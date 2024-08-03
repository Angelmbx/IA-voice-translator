import gradio as gr 
import whisper

# gradio is a helpful framework in the creation of simple pre-made web pages

def translator(audio_file):
   # 1 Transcribe audio to text

   try:
        model= whisper.load_model("base")
        result= model.transcribe(audio_file)
        transcription= result["text"]
   except Exception as e:
        raise gr.Error( 
          f"An error ocurred while trying to transcribe the text: {str(e)}")  
           
# its interface needs a function, inputs and outputs
web = gr.Interface(
    fn= translator, 
    inputs= gr.Audio(
        sources=["microphone"], # how does the program get the voice -> microphone or upload
        type= "filepath" 
    ),
    outputs=[],
    title= "Voice Translator",
    description= "AI voice translator for several lenguages"
)

web.launch() # Running on local URL:  http://127.0.0.1:7860

# Once you record your message and click on 'submit', the audio will be sent to the function in the interface, and it will execute