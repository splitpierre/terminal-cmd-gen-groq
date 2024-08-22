Terminal Command Generator with Groq
====================================

This tool allows you to generate terminal commands using the Groq API. It can take a description of the task you want to accomplish, generate the appropriate terminal command, and copy it to your clipboard for easy use. You can provide the task description directly as a command-line argument or input it interactively.

Features
--------

*   **Command Generation**: Generates terminal commands based on a task description using the Groq API.
*   **Clipboard Integration**: Copies the generated command to your clipboard for easy pasting.
*   **Flexible Input**: Accepts task descriptions directly from the command line or interactively prompts for input.

Setup
-----

### 1. Clone the Repository

```bash 
git clone https://github.com/splitpierre/terminal-cmd-gen-groq.git cd terminal-cmd-gen-groq
```

### 2. Install Dependencies

Ensure you have Python 3 installed on your system. Install any required Python packages:

```bash 
# install xclip for copy to clipboard
sudo apt-get install xclip
# install python requirements
pip install -r requirements.txt
```

### 3. Configure API Keys

Copy and edit the `.env-sample` to `.env` file in the project directory with your Groq API key.

Also, inform the model of choice in the .env file.
Read available models here:

https://console.groq.com/docs/models

### 4. Make the Script Executable and Available on Terminal

Make the `main.py` script executable and optionally move it to a directory in your `PATH` or create a symlink:

```bash
chmod +x main.py
sudo ln -s /path/to/your/main.py /usr/local/bin/groq-gen
```

Usage
-----

### Command-Line Usage

You can provide a task description directly when calling the script:

```bash
groq-gen How to find a file named "Ball" in the current directory?
```
The command will be generated, printed, and copied to your clipboard.

### Interactive Usage

If no task description is provided, the script will prompt you to enter one:

```bash
groq-gen
```

You will then be asked to enter the task description interactively.


Contributing
------------

Feel free to submit issues or pull requests if you find bugs or want to improve the tool!

Notes
-----
This tool is provided as is, I don't plan to make improvements or keep adding features to it. Feel free to use, copy, share or modify.
