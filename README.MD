# AI CLI Assistant

A packaged, functional AI assistant operating right from your terminal. No heavy frameworks, just a clean, conversational agent built using Groq and Llama.

This repository demonstrates a working agent that can read, write, and edit files through natural conversation. It has been structured into a modern Python package using `pyproject.toml` and managed via `uv`, meaning you can install it globally with a single command.

You'll understand how AI agents parse responses, execute tools, and maintain conversation context.

## Credits

This repository is forked from Francis Beeson's implementation: [Single-File AI Agent Tutorial](https://github.com/leobeeson/single-file-ai-agent-tutorial)

The code is based on the tutorial by Thorsten Ball in ["How to Build an Agent"](https://ampcode.com/how-to-build-an-agent) from ampcode.com. Thank you, Thorsten. Brilliant guide.

## Features

- Complete Python package structure.
- The AI agent can:
  - Read file contents.
  - List directory contents.
  - Edit existing files or create new ones.
- Interactive chat interface.
- Error handling and feedback.
- Logging of agent tool usage (`agent.log`).

## Requirements

- `uv` package manager (see installation instructions below)
- Python 3.11 or higher
- Groq API key (you can get one from [Groq Console](https://console.groq.com/keys))

## Installing uv

`uv` is an extremely fast Python package manager that simplifies installing modern Python applications.

To [install](https://docs.astral.sh/uv/getting-started/installation/) `uv`:

### Linux/macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, verify it's working:

```bash
uv --version
```

## Installing the Agent

The tool can be installed globally on your system using `uv`. From the repository root, run:

```bash
uv tool install .
```

If you plan to modify the code, you can install it in editable mode:
```bash
uv tool install -e .
```

## Running the Agent

Once installed, you can start the assistant from any terminal using:

```bash
ai-assist
```

The first time you run it, the agent will prompt you to enter your Groq API key, which it will securely save to `~/.config/ai_cli/config.json` (or the equivalent user config dir). Alternatively, you can pass it via an environment variable or flag:

```bash
export GROQ_API_KEY="your-api-key-here"
ai-assist
```

Or:

```bash
ai-assist --api-key "your-api-key-here"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
