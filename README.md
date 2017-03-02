# pidginCli
Command line interface to [Pidgin](https://www.pidgin.im/) + bash completion

## Demo

[![screencast](https://img.youtube.com/vi/BBvfG0d-AxU/0.jpg)](https://youtu.be/BBvfG0d-AxU)

## Usage

```
# Reads message from stdin
echo "My message" | pidginMsg <buddy1> <buddy2> ...

# Opens $EDITOR
pidginMsg <buddy1> <buddy2> ...
```

## Requirements

Pidgin must be running.

## Instalation

1. Clone this repo
   ```
   git clone https://github.com/tfga/pidginCli pidginCli
   cd pidginCli
   ```

2. Edit `src/PidginCli/conf.py`

   Pidgin is multi-protocol and you can have multiple accounts, but for the time being, `pidginCli` supports only one domain. Sorry. If you need support for multiple domains, feel free to create an issue or a PR.

   `domain` is everything that comes after `@` in your contacts. E.g. if your contacts are of the form

   `someone@gmail.com`

   then the contents of your `conf.py` should be:

    ```
    domain = 'gmail.com'
    ```

3. Install

   ```
   sudo pip install --upgrade .
   ```

This will install 2 executables:

  * `pidginMsg`: the main executable
  * `_pidginCompleteBuddy`: used by the bash completion

### Shell completion

Add this to your `.bashrc`:

```sh
source <absolute path to pidginCli>/bash/bashCompletion
```

If you don't want to keep the repo around, move `bash/bashCompletion` somewhere else and adjust the path accordingly.
