# tiny_python_video_cutter

Source code based on a discussion in [StackOverflow](https://stackoverflow.com/questions/37317140/cutting-out-a-portion-of-video-python)

# Setup project in Pycharm:
- Download & install `Python 3.8.5`.
- Download & install `Pycharm`.
- Configure virtual env in Pycharm. You are done when a folder named ```venv``` is created under your project's root folder.
- Run this command
```
pip install -r requirements.txt
```

# How to use?
- Copy your video to the project's root folder.
- Run this command
```
python src\app.py <start_time_in_minute> <end_time_in_minute>
```