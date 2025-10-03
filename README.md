# mkdocs-recently-updated-docs

English | [简体中文](README_zh.md)



One line of code to display a list of recently updated documents

## Features

- Support list display of recently updated documents
- Flexible display position (`sidebar` or `in md document`)
- Rich template examples
- Works well for any environment (no-Git, Git, all CI/CD build systems, etc.)

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
