# Dock Mennonite Biology Website

Course website for freshman Biology at Dock Mennonite Academy, built with Jekyll and GitHub Pages.

The site combines:
- rigorous, standards-aligned science instruction,
- clear daily lesson pacing for class and home support,
- faith-integrated framing that honors God as Creator.

## Live Site

- https://ajesbenshade.github.io/biology/

## Site Structure

- Home: `index.md`
- Unit 4 overview + lessons: `lessons/unit4/`
- Unit 5 overview + lessons: `lessons/unit5/`
- Syllabus: `syllabus.md`
- Resources hub: `resources/`
- Full curriculum map: `full-curriculum-map.md`

## Design + Front-End Notes

- Layout file: `_layouts/default.html`
- Theme CSS: `assets/css/custom.css`
- Tailwind is loaded via CDN for lightweight utility styling.
- Custom CSS provides the creation-themed palette, typography, and responsive table behavior.

## Screenshots

Add screenshots here as the site evolves:
- `assets/images/screenshots/home-desktop.png`
- `assets/images/screenshots/home-mobile.png`
- `assets/images/screenshots/unit4-overview.png`
- `assets/images/screenshots/unit5-overview.png`

## Local Development Setup

### Prerequisites

- Ruby 2.6+ (currently tested on Ruby 2.6.10)
- Bundler (`gem install bundler`)
- Ruby version manager recommended (`rbenv`, `rvm`, `asdf`, or `mise`); this project includes `.ruby-version`.

**Important Ruby note:**
This project currently pins `jekyll ~> 3.9.5` for compatibility with Ruby 2.6.10.
If you are on Ruby 2.7+ or 3.x, you can upgrade to `jekyll ~> 4.3` and run `bundle update jekyll`.
If you hit dependency conflicts, Ruby 2.7–3.2 is typically the smoothest range for Jekyll setups.

### 1) Install dependencies

From this `website/` directory:

```bash
bundle install
```

### 2) Run locally

```bash
bundle exec jekyll serve --livereload
```

Open `http://127.0.0.1:4000/biology/`.

### 3) Build check

```bash
bundle exec jekyll build
```

## Content Workflow

1. Update lesson pages in `lessons/unit4/` or `lessons/unit5/`.
2. Confirm unit overview tables link correctly.
3. Update `resources/index.md` when adding new handouts/guides.
4. Run local server and verify mobile + projector readability.

## `integrate_lessons.py` Script

Path: `integrate_lessons.py`

Purpose:
- Removes leftover `<VSCode.Cell>` wrappers.
- Removes accidental surrounding markdown fences.
- Adds basic Jekyll frontmatter if a lesson file is missing it.

Run from `website/`:

```bash
python integrate_lessons.py
```

Recommended before committing large lesson imports.

## Deployment (GitHub Pages)

1. Commit your changes.
2. Push to `main` on GitHub.
3. GitHub Pages rebuilds automatically.

## Quick Links

- [Unit 4 Overview](lessons/unit4/index.md)
- [Unit 5 Overview](lessons/unit5/index.md)
- [Resources](resources/index.md)
