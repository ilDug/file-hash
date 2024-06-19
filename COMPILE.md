# Compile binary

In order to execte the command, you must compile the python source code to get a binary executable file.
To do so,  use [pyinstaller](https://pyinstaller.org/en/stable/).

## Run pyinstaller

Use this command to compile the python source code:

```bash
pyinstaller ./src/main.py --onefile --name fhash
```

This create a directory called `dist/` where the binary file is saved.

## Ubuntu installation

If does not  exists,  create a folder into `~/bin`.

Then create a link into this folder, that points to compiled executable:

```bash
ln -d path/to/cimg/dist/cimg ~/bin/cimg
```

Ensure t create an alias into `.bashrc` file or `.zshrc` 

```bash
...
alias cimg="~/bin/cimg"
...
```

