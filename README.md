# Aaron Esbenshade — Biology Website

Static Jekyll site for Dock Mennonite High School Biology. GitHub Pages builds this repository into static HTML pages, so every lesson page is pre-rendered and linkable.

## Site Structure

- `index.md` — homepage and quick links
- `lessons/unit4/` — Unit 4 overview + daily lesson pages
- `lessons/unit5/` — Unit 5 overview + daily lesson pages
- `resources/` — study guides, worksheets, and parent/teacher supports
- `_layouts/default.html` — shared layout for all pages
- `assets/css/custom.css` — site styling

## Static Publishing Notes

- This site is static: Jekyll compiles Markdown + frontmatter into plain HTML.
- Lesson links should use permalink directory paths (for example `/lessons/unit5/day-01/`), not `.md` file links.
- Unit coverage is complete:
  - Unit 4 day pages are published under `lessons/unit4/.../index.md`
  - Unit 5 day pages are published under `lessons/unit5/day-01` through `day-21`

## Local Development

1. Install gems:

	`bundle install`

2. Build the static site:

	`bundle exec jekyll build`

3. Serve locally:

	`bundle exec jekyll serve --livereload`

4. Open:

	`http://127.0.0.1:4000/biology/`

## Lesson Content Workflow

- Edit daily lesson pages in `lessons/unit4/` and `lessons/unit5/`.
- Keep each lesson file with YAML frontmatter (`layout`, `title`, `permalink`).
- Keep overview tables in each unit hub aligned with available day folders.

## `integrate_lessons.py`

`integrate_lessons.py` is a helper script for integrating lesson sources into this website structure. Use it only when importing/updating lesson content in bulk, then verify:

- each destination day folder has `index.md`
- each page has valid frontmatter
- all hub links resolve to permalink paths
