# tiny_python_video_cutter

Source code based on a discussion in [StackOverflow](https://stackoverflow.com/questions/37317140/cutting-out-a-portion-of-video-python)

# Setup project in Pycharm:
- Configure virtual env in Pycharm. You are done when a folder named ```venv``` is created under your project's root folder.
- Windows: Run this command
```
"venv\Scripts\pip.exe" install -r requirements.txt
```

# How to use?
- Copy your video to the project's root folder.
- Select ```start_time```, ```end_time``` in ```src\test.py```. Run this command
```
"venv\Scripts\python.exe" src\test.py
```