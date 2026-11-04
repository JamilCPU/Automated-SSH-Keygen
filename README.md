# Automated SSH Keygen

A small desktop GUI that wraps `ssh-keygen`. You enter a key comment and choose separate directories for the private and public key, and it generates an Ed25519 key pair for you. It was written to remove the repetitive command-line steps of creating keys for new machines.

## Stack

- Python 3
- tkinter / ttk for the GUI
- OpenSSH `ssh-keygen` (called through `subprocess`)

## Running

Requires Python 3 with tkinter and OpenSSH installed. On Debian or Ubuntu:

```bash
sudo apt install python3-tk python3-venv
python3 -m venv venv
source venv/bin/activate
python app.py
```

`requirements.txt` has no pip packages; it only documents the tkinter system dependency. On Windows, tkinter ships with the standard Python installer and `ssh-keygen` comes with the OpenSSH client feature.

Fill in the comment, pick the private and public key directories, and press "Generate Key".

## Project layout

- `app.py` - the tkinter window and input handling
- `commands/ssh.py` - validates input, runs `ssh-keygen -t ed25519`, and moves the `.pub` file into the chosen directory

## Notes

- Keys are created with an empty passphrase, and the tool refuses to overwrite an existing `id_ed25519`.
- Directories are created if they do not exist.

## Status

Work in progress. There is no passphrase option, key-name field or test suite yet.
