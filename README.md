# mkdocs-recently-updated-docs

English | [简体中文](README_zh.md)

<br />

Display a list of recently updated documents anywhere on your MkDocs site with a single line of code. This is ideal for sites with a large number of documents, so that readers can quickly see what's new.

## Features

- Display recently updated documents in descending order of update time
- Support exclude specified files or folders
- Support custom display quantity
- Support custom rendering template
- Works well for any environment (no-Git, Git, Docker, all CI/CD build systems, etc.)

## Preview

![recently-updated](recently-updated.png)

## Installation

```bash
pip install mkdocs-recently-updated-docs
```

## Configuration

Just add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - recently-updated
```

Or, full configuration:

```yaml
plugins:
  - recently-updated:
      limit: 10          # Limit the number of docs displayed
      exclude:           # List of excluded files
        - index.md       # Exclude specific file
        - drafts/*       # Exclude all files in drafts folder, including subfolders
      template: templates/recently_updated_list.html    # Custom rendering template
```

## Usage

Simply write this line anywhere in your md document:

```markdown
<!-- RECENTLY_UPDATED_DOCS -->
```

## Custom template

See [templates](https://github.com/jaywhj/mkdocs-recently-updated-docs/tree/main/mkdocs_recently_updated_docs/templates) directory

<br />

## Other plugins

[mkdocs-document-dates](https://github.com/jaywhj/mkdocs-document-dates)

A new generation MkDocs plugin for displaying exact **creation time, last update time, authors, email** of documents

![render](render.gif)
