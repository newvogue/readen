# Readen Project Context

## Project Overview

Readen is a lightweight, self-hosted EPUB reader that allows users to read EPUB books one chapter at a time. It's designed to make it easy to copy and paste chapter contents to an LLM (Large Language Model) for interactive reading experiences. The project has both a legacy implementation and a newer backend implementation using modern Python web technologies.

The project was originally "90% vibe coded" to demonstrate how to read books together with LLMs, as referenced by Andrej Karpathy's tweet about reading with LLMs.

## Project Structure

```
Readen/
├── backend/           # Modern FastAPI-based backend implementation
│   └── app/
│       ├── __init__.py
│       ├── database.py    # SQLAlchemy database setup
│       ├── main.py        # FastAPI application routes
│       ├── models.py      # SQLAlchemy data models
│       └── services.py    # Business logic services
├── legacy/            # Original implementation
│   ├── readen.py      # EPUB processing script
│   ├── server.py      # Legacy FastAPI web server
│   ├── templates/     # HTML templates for web interface
│   │   ├── library.html
│   │   └── reader.html
│   └── Readen.png     # Project logo image
├── pyproject.toml     # Project dependencies and metadata
├── uv.lock           # Dependency lock file (uv package manager)
├── README.md         # Project documentation
├── Dialectical_Prompt_Template.md
├── Universal_Prompt_Template.md
└── chat_history.md
```

## Technologies Used

- **Backend Framework**: FastAPI (modern Python web framework)
- **Database**: SQLAlchemy with SQLite (for the modern backend)
- **EPUB Processing**: ebooklib library
- **HTML Parsing**: BeautifulSoup4
- **Template Engine**: Jinja2
- **Package Manager**: uv (fast Python package installer)
- **Web Server**: Uvicorn (ASGI server)

## Legacy Implementation

The legacy system works in two phases:

1. **EPUB Processing (**`legacy/readen.py`**)**:
   - Parses EPUB files into structured Python objects
   - Extracts chapters, metadata, and images
   - Saves processed data as pickle files in `{bookname}_data` directories

2. **Web Interface (**`legacy/server.py`**)**:
   - FastAPI server that serves the processed books
   - Provides a library view showing all available books
   - Chapter-by-chapter reading interface with navigation
   - Static file serving for images

## Modern Backend Implementation

The newer backend follows a more structured architecture:

- **Database Models**: SQLAlchemy models for Book and Chapter entities
- **Services**: Business logic separated into service functions
- **API Endpoints**: RESTful API endpoints for books and chapters
- **Dependency Injection**: Uses FastAPI's dependency injection for database sessions

## Building and Running

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager installed

### Running the Legacy Version

1. Place an EPUB file in the project root directory (e.g., `dracula.epub`)
2. Process the EPUB:
   ```bash
   uv run legacy/readen.py dracula.epub
   ```
   This creates a `dracula_data` directory with the processed book
3. Start the server:
   ```bash
   uv run legacy/server.py
   ```
4. Visit [http://localhost:8123/](http://localhost:8123/) to access your library

### Running the Modern Backend

The backend exposes API endpoints, but the legacy frontend is still used for the web interface.

## Key Features

- **EPUB Processing**: Extracts and structures EPUB content into chapters with navigation
- **Web Interface**: Clean, responsive interface for reading books chapter by chapter
- **Image Support**: Proper handling of images embedded in EPUB files
- **Navigation**: Both linear (previous/next) and hierarchical (TOC) navigation
- **Self-Hosted**: Runs entirely on your local machine for privacy
- **LLM Integration**: Designed to facilitate copying and pasting text to AI tools

## Development Conventions

- The project uses FastAPI's modern Python type hints and dependency injection
- Database operations are handled through SQLAlchemy ORM
- The project uses uv for fast dependency management
- Templates are written in Jinja2 for clean HTML generation
- The legacy code includes detailed comments explaining the processing logic

## Project Status

The original developer states this is an experimental project not intended for active maintenance, but it provides a solid foundation for reading books with LLMs. The project includes both a legacy implementation that's fully functional and a newer backend structure that could be expanded.

## Usage Tips

1. **Adding Books**: Place EPUB files in the project directory and run the parser to create data directories
2. **Copy/Paste Interface**: The chapter-by-chapter view makes it easy to select and copy text for AI interaction
3. **Image Handling**: The system properly extracts and serves images from EPUB files
4. **Navigation**: Both TOC-based and linear navigation are available

## Dependencies

The project depends on:
- `beautifulsoup4`: HTML parsing
- `ebooklib`: EPUB file processing
- `fastapi`: Web framework
- `jinja2`: Template rendering
- `sqlalchemy`: Database ORM
- `uvicorn`: ASGI server

## Architecture Notes

The project has evolved from a simple, functional implementation to a more structured backend architecture. The legacy implementation is fully functional and demonstrates a complete readen application, while the backend directory shows a more modern approach with proper API design and database interactions.

The legacy system stores processed books as pickle files, which provides fast loading but couples the data format to Python. The newer backend is set up to use SQLite for data storage, which would provide more flexibility for cross-platform access and querying.
