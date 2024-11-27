# NExa: Dev.to Article Fetcher

**NExa** is a Python-based tool designed to fetch and display the latest articles from **dev.to**. It provides an easy-to-use command-line interface (CLI) for fetching articles based on user-defined categories and displaying them in a human-readable format. You can install and use NExa to keep up with the latest tech trends directly in your terminal!

## Features

- Fetch articles from **dev.to** using a simple CLI.
- Supports browsing different article categories on **dev.to**.
- Displays the top articles with relevant information like title, author, and time.
- Written in Python, easy to extend and modify.
- Allows quick installation with `pip` and can be run as a terminal command `nexa`.
- Available as a pre-built Docker image for easy deployment.

## Installation

To get started with **NExa**, follow the installation steps below:

### Option 1: Using Docker (Recommended)

You can quickly run **NExa** using Docker without needing to set up a Python environment manually.

1. **Pull the Docker image**:

   ```bash
   docker pull bitsgenix/nexa
   ```

2. **Run the container**:
   ```bash
   docker run --rm -it bitsgenix/nexa
   ```

This will start the application inside a Docker container, and you can start fetching articles immediately.

### Option 2: Using Python Environment (Manual Installation)

If you prefer to install **NExa** manually on your system, follow the steps below.

#### Prerequisites

- Python 3.11 or higher
- `pip` (Python package installer)
- Git (for cloning the repository)

#### Step 1: Clone the repository

```bash
git clone https://github.com/m-mdy-m/NExa.git
cd NExa
```

#### Step 2: Install dependencies

Create a virtual environment (recommended) and install the dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -e .
```

This will install **NExa** in editable mode (`-e`), which means any changes you make to the source code will be reflected immediately.

#### Step 3: Make the `nexa` command available globally

Once installed, you can run the `nexa` command in your terminal.

```bash
nexa
```

#### Step 4: Verify the installation

To verify the installation was successful, try running:

```bash
nexa
```

You should see the welcome message and be able to start fetching articles from **dev.to**.

## Usage

After installation, simply run `nexa` from your terminal to fetch articles.

### Example Usage

```bash
$ nexa
Welcome to NExa - Dev.to Article Fetcher
```

The tool will prompt you to choose an article category (e.g., "latest articles", "programming", etc.), and then it will fetch and display the top articles from that category.

### Available Commands

- `nexa`: Start fetching and displaying articles from **dev.to**.
- `nexa -h` or `nexa --help`: Displays help information and available options.

### Output

The output will include:

- The **title** of the article.
- **Author** name.
- **Time** when the article was published.
- A brief **description** or excerpt.

Articles are displayed with colored formatting to make them easy to read directly in your terminal.

## Development

If you wish to contribute to **NExa**, or modify it for your own purposes, you can clone the repository and work on the source code.

### Setting Up Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/m-mdy-m/NExa.git
   cd NExa
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install -e .
   ```

3. Make changes to the code inside the `/bin` and `/modules` directories.

4. After making changes, you can test them by running `nexa` from the terminal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have ideas for enhancements or fixes:

1. Fork the repository.
2. Create a feature branch:

```
git checkout -b feature-name
```

3. Commit your changes and push:

```
git commit -m "Description of changes"
git push origin feature-name
```

4. Open a Pull Request.

For more detailed information on how to contribute, please refer to the [CONTRIBUTING.md](./docs/CONTRIBUTING.md).
