# Static Site Generator

A simple static site generator built in Python that converts Markdown files into a fully linked HTML website.

## Features

- Converts Markdown to HTML, supporting:
  - Headings, paragraphs, and blockquotes
  - Bold and italic text
  - Ordered and unordered lists
  - Code blocks
  - Links and images
- Recursively copies static assets (CSS, images, etc.)
- Generates HTML pages from a content directory, preserving folder structure
- Uses a customizable HTML template

## Project Structure

```
├── content/         # Markdown source files
├── static/          # Images, CSS, and other static assets
├── template.html    # HTML template used to wrap generated pages
├── src/             # Python source code
└── main.sh          # Script to build and run the site
```

You can delete and add your own structure and your own markdown files into the content folder. This repo uses a Lord of the Rings themed contents.

## Getting Started

### Prerequisites

- Python 3.x

### Running Locally

1. Clone the repository:
   - git clone https://github.com/your-username/your-repo-name.git
   - cd your-repo-name
2. Run the main script:
   - ./main.sh
3. Open your browser to `http://localhost:8888`

## How It Works

1. Static files are copied from `static/` to `public/`.
2. Markdown files in `content/` are recursively converted to HTML using `template.html`.
3. The generated site is served locally for preview.

## What I Learned

- Building a Markdown-to-HTML parser from scratch
- Recursive file system traversal
- Working with the DOM as a tree of nodes
- Writing extensive unit tests for parsing logic

## Live Demo

Here's the live demo link I deployed with GitHub Pages: [static-site-generator](https://lastechomp.github.io/static-site-generator/)

## License

This project is licensed under the MIT License.
