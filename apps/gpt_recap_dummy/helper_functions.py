from google.cloud import texttospeech_v1

# def synthesize_speech(ssml_file, unique_id):

#     print(ssml_file)
#     client = texttospeech_v1.TextToSpeechLongAudioSynthesizeClient()

#     with open(ssml_file, "r") as f:
#         ssml = f.read()
#         input_text = texttospeech_v1.SynthesisInput(ssml=ssml)


#     voice = texttospeech_v1.VoiceSelectionParams(
#         language_code="en-gb",
#         name='en-GB-Neural2-B',
#         #name='en-GB-Neural2-F',
#         ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
#     )

#     print(input_text)

#     audio_config = texttospeech_v1.AudioConfig(
#         audio_encoding=texttospeech_v1.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         speaking_rate=0.90
#     )

#     print(audio_config)

#     request = texttospeech_v1.SynthesizeLongAudioRequest(
#         input=input_text,
#         voice=voice,
#         audio_config=audio_config
#     )
    
#     operation = client.synthesize_long_audio(request=request)

#     print("Waiting for operation to complete...")

#     response = operation.result()

#     print(response)

#     # The response's audio_content is binary.
#     with open(f"audio/{unique_id}.wav", "wb") as out:
#         out.write(response.audio_content)
#         print(f'Audio content written to file "audio/{unique_id}.wav"')



# ## ASYNC LONG AUDIO - DOES NOT WORK

# async def synthesize_speech(ssml_file, unique_id):
#     client = texttospeech_v1.TextToSpeechLongAudioSynthesizeAsyncClient()

#     # Initialize request argument(s)
#     with open(ssml_file, "r") as f:
#         ssml = f.read()
#         input_text = texttospeech_v1.SynthesisInput(ssml=ssml)

#     voice = texttospeech_v1.VoiceSelectionParams(
#         language_code="en-gb",
#         name='en-GB-Neural2-B',
#         #name='en-GB-Neural2-F',
#         ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
#     )

#     audio_config = texttospeech_v1.AudioConfig(
#         audio_encoding=texttospeech_v1.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,
#         speaking_rate=0.90
#     )

#     request = texttospeech_v1.SynthesizeLongAudioRequest(
#         input=input_text,
#         audio_config=audio_config,
#         voice=voice
#     )

#     # Make the request
#     operation = client.synthesize_long_audio(request=request)

#     print("Waiting for operation to complete...")

#     response = (await operation).result()

#     # The response's audio_content is binary.
#     with open(f"audio/{unique_id}.wav", "wb") as out:
#         out.write(response.audio_content)
#         print(f'Audio content written to file "audio/{unique_id}.wav"')



def synthesize_speech(ssml_file, unique_id):

    print(ssml_file)
    client = texttospeech_v1.TextToSpeechClient()

    with open(ssml_file, "r") as f:
        ssml = f.read()
        input_text = texttospeech_v1.SynthesisInput(ssml=ssml)

    print(input_text)

    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-gb",
        name='en-GB-Neural2-B',
        #name='en-GB-Neural2-F',
        ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.LINEAR16,
        speaking_rate=0.90
    )

    print(audio_config)

    request = texttospeech_v1.SynthesizeSpeechRequest(
        input=input_text,
        voice=voice,
        audio_config=audio_config,
    )

    response = client.synthesize_speech(request=request)

    # The response's audio_content is binary.
    with open(f"audio/{unique_id}.wav", "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "audio/{unique_id}.wav"')
    
