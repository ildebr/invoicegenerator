# invoicegenerator

Invoice generator is a python application to generate pdf invoices using tkinter and fdpdf2.

# Installation

```bash
pip install -r requirements.txt
```

## Usage

To use this application you must run the command

```bash
py main.py
```

Which will open the tkinter application.

![tkinter app](https://github.com/ildebr/invoicegenerator/blob/master/usagephotos/Screenshot%202023-11-07%20041013.png)

Once you have added all of your invoice information and charges you can press the generate invoice button, which will generate a file such as

![pdf](https://github.com/ildebr/invoicegenerator/blob/master/usagephotos/Screenshot%202023-11-07%20041053.png)


## Stand-alone application

If you want to avoid opening a command line everytime you want to use the application, you can run

```bash
pyinstaller main.py
```

Which will create a stand-alone .exe application which you can easily place anywhere and double-click to open, bear in mind that as of now the file generated will always have the same name, meaning that as you generate a new invoice the old one will get overwritten.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)
