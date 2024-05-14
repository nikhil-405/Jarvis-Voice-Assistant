# Jarvis-Voice-Assistant
_Contributions are appreciated_

## Usage
Install the required modules using 
> pip install {module_name}

For installing the required modules, you can individually excute the below commands in your terminal window

```
$ pip install pyttsx3    
```

```
$ pip install SpeechRecognition    
```

```
$ pip install wikipedia    
```

```
$ pip install pyautogui  
```

```
pip install rich
```

And if you need AI functionalities, also run the command: 
```
$ pip install openai    
```

If you want to access the AI functionalities, complete the code by using your OpenAI developer API. For further information on how to implement the same, you can refer to the Python file 'jarvis_assistant.py' and this [link](https://platform.openai.com/docs/api-reference/introduction?lang=python)

Additionally, ensure that you download 'jokes.txt' file, and it is in the same directory as 'jarvis_assistant.py'

## Features 
This is a simple Voice assistant that can do the following:
* Upon booting, it wishes you based on the time in your timezone(for example, before 12 noon it would wish you "Good Mowrning!", and so on)
* Open Wikipedia/Youtube pages of your choice
* Help you in making hands-free Google searches
* Tell you jokes from a text file of already written jokes
* Tell you the current time
* Open Spotify and play the song that you ask it to play
* Integrates with OpenAI to help you perform tasks such as writing a poem

The output is in audio format and can also 

## Future scopes/To-do's
* Find and use a voice that closely resembles the voice of Jarvis from the Iron Man movies
* Integration with OpenAI's developer API
* Find an alternative to hard-coding because that leaves the user with very little room for error while giving voice commands. A possible way around this problem might be to use AI to decrypt what the user is trying to say and then take actions accordingly, but this would require re-writing the app from scratch and is not in the current scope of the project
* Develop a GUI for the app 
  
