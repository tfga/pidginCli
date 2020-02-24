# pidginCli
Command line interface to [Pidgin](https://www.pidgin.im/) + bash completion

## Demo

![Demo](https://i.imgur.com/cIUqiJJ.gif)

## Usage

```
# Reads message from stdin
echo "My message" | pidginMsg <buddy1> <buddy2> ...

# Opens $EDITOR
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

2. Edit `src/PidginCli/conf.py`

   Pidgin is multi-protocol and you can have multiple accounts, but for the time being, `pidginCli` supports only one domain. If you need support for multiple domains, feel free to create an issue or a PR.

   `domain` is everything that comes after `@` in your contacts. E.g. if your contacts are of the form:

   `someone@gmail.com`

   then the contents of your `conf.py` should be:

   ```
   domain = 'gmail.com'
   ```

3. Install

   ```sh
   pip2 install .
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

## How the completion works

The completion takes into account both the username and full name. For instance, in the demo (above), the following completions take place:

* `luciv_ => lucivaldo.costa`  -- username match
* `bern_  => thiago.almeida`   -- full name match ("Thiago  **Bern**ardes de Almeida")

where `_` is where the cursor was when I pressed `TAB`.

## FAQ

1. Is this thing interactive?

   No. The use case is, e.g. when you want to send the output of some command to a co-worker without leaving the terminal.
