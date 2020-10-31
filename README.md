# pidginCli
Command line interface to [Pidgin](https://www.pidgin.im/) + bash completion

## Demo

[![screencast](https://img.youtube.com/vi/BBvfG0d-AxU/0.jpg)](https://youtu.be/BBvfG0d-AxU)

## Usage

```
# Reads message from stdin
echo "My message" | pidginMsg <buddy1> <buddy2> ...

# Just opens the chat window
pidginMsg <buddy1> <buddy2> ...
```

## Requirements

1. `python-dbus`

    On Ubuntu, this can be installed with:

    ```
    sudo apt-get install python-dbus
    ```

2. Pidgin must be running.

## Instalation

1. Clone this repo
   ```
   git clone https://github.com/tfga/pidginCli
   cd pidginCli
   ```

1. Install

    * Without virtualenv:

      ```sh
      pip2 install .
      ```

    * With virtualenv:

      1. Edit the `install` script and change the value of  `INSTALL_DIR` to point to the directory where the executables should be installed. This directory should be in your `$PATH`.

      2. Run:

         ```sh
         ./install
         ```

1. Now you should have two new executables on your PATH:

  * `pidginMsg`: the main executable
  * `_pidginCompleteBuddy`: used by the bash completion


### Shell completion

Add this to your `.bashrc`:

```sh
source <absolute path to pidginCli>/bash/bashCompletion
```

If you don't want to keep the repo around, move `bash/bashCompletion` somewhere else and adjust the path accordingly.

## How the completion works

The completion takes into account both the username and full name. For instance, in the demo (above), the following completions take place:

* `luciv_ => lucivaldo.costa`  -- username match
* `bern_  => thiago.almeida`   -- full name match ("Thiago  **Bern**ardes de Almeida")

where `_` is where the cursor was when I pressed `TAB`.

## FAQ

1. Is this thing interactive?

   No. The use case is, e.g. when you want to send the output of some command to a co-worker without leaving the terminal.


# PidginQuickLaunch

Actually... there's a _second_ application hidden in this repo. :raised_eyebrow:

The attentive user will certainly have noticed that after the installation, a third executable is also present:

  `pidginQuickLaunch`

_Hum... what might that be?_  :thinking:

It's a GUI version of `pidginMsg`.

:exploding_head:

## Installation

If you want to use this, you must also install `python-keybinder` and `python-gtk2`:

```sh
sudo apt-get install python-keybinder python-gtk2
```

## Shortcuts

Once the application is running, the GUI can be summoned with the (global) shortcut `Ctrl + Alt + m`. And dismissed with `Esc`.
