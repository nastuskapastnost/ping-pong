# Ping-pong Python game

### Workstation configuration

Steps to configure workstation (tested on MacOS Monterey):
- install latest PyCharm (source - [JetBrains website](https://www.jetbrains.com/help/pycharm/installation-guide.html#a569cb61))
- install Homebrew
  ```shell
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew update
  ```
- install the latest Python version (at the moment - 3.10)
  ```shell
  brew install python
  python3 --version
  # Python 3.8.9 (system one)
  ln -s /usr/local/bin/python3 /usr/local/bin/python
  python --version
  # Python 3.10.6 (latest one)
  ```
- install Tkinter
  ```shell
  brew install python-tk@3.10
  ```

