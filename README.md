# mkdocs-recently-updated-docs

English | [简体中文](README_zh.md)

<br />

Display a list of recently updated documents anywhere on your MkDocs site with a single line of code. This is ideal for sites **with a large number of documents**, so that **readers can quickly see what's new**.

## Features

- Display recently updated documents in descending order by update time, list items are dynamically updated
- Support multiple view modes such as list, detail and grid
- Support automatic extraction of article summaries
- Support custom display quantity
- Support exclude specified files or folders
- Works well for any environment (no-Git, Git, Docker, all CI/CD build systems, etc.)

## Preview

![recently-updated](recently-updated-en.gif)

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
        - blog/*         # Exclude all files in blog folder, including subfolders
```

## Usage

Simply write this line anywhere in your md document:

```markdown
<!-- RECENTLY_UPDATED_DOCS -->
```

<br />

## Other Projects

- [**MaterialX**](https://github.com/jaywhj/mkdocs-materialx), the next generation of mkdocs-material, is based on `mkdocs-material-9.7.0` and is named `X`. I'll be maintaining this branch continuously (since mkdocs-material will stop being maintained). 
Updates have been released that refactor and add a lot of new features, see https://github.com/jaywhj/mkdocs-materialx/releases/

<br />

- [**mkdocs-document-dates**](https://github.com/jaywhj/mkdocs-document-dates), a new generation MkDocs plugin for displaying exact **creation date, last updated date, authors, email** of documents

  ![render](render.gif)

<br />

## Chat Group

**Discord**: https://discord.gg/cvTfge4AUy

**Wechat**: 

<img src="wechat-group.jpg" width="140" />