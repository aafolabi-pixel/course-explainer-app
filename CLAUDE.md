# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flask-based web application displaying course information. Uses a simple MVC-style architecture with Flask handling routing, view functions rendering templates, and a Course model managing course data.

## Development Environment

### Setup

```bash
# Unix/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

### Running the Application

```bash
python src/app.py
```

Available at `http://127.0.0.1:5000`

### Running Tests

```bash
# Run all tests
python -m unittest discover -s tests

# Run a specific test file
python -m unittest tests.test_app

# Run a specific test case
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

### Application Structure

- **src/app.py**: Entry point. Routes registered via `add_url_rule()` rather than decorators, keeping views decoupled from Flask.
- **src/views.py**: View functions (pure functions, no Flask decorators). Imports only `render_template` and `request` from Flask.
- **src/models.py**: In-memory `Course` objects in a list. No database — all data is hardcoded. Course lookup uses `course_id - 1` as list index.
- **src/templates/**: Jinja2 templates with `layout.html` as the base (`extends`/`block` pattern).
- **src/static/css/**: CSS stylesheets. Follow the design system in `.claude/skills/ui-designer/references/design-system.md`.

### Routes

| URL | Method | View |
|-----|--------|------|
| `/` | GET | `index` — lists all courses |
| `/course/<course_id>` | GET | `course` — detail page; `course_id` is 1-based integer |
| `/contact` | GET, POST | `contact` — form with server-side validation (name, email, address) |

### Data Model

`Course(title, description, instructor, duration, topics=[])` — stored in a module-level list in `models.py`. Adding courses means appending to that list.

## Development Workflow

### Unit Tests

Always add unit tests for new features and confirm they pass before proceeding.

### Custom Commands

- `/explain_this_file` — explains the currently open file
- `/implement_ui_user_story <story>` — orchestrates full UI workflow: UX design (ux-design-planner agent) → implementation → visual verification (ui-testing-agent)

### Custom Agents

- **ui-testing-agent**: Use after implementing any UI feature. Starts Flask, uses Playwright to interact with the feature, saves screenshots to `test-output/`.
- **ux-design-planner**: Invoked via `/implement_ui_user_story`. Produces design specs before coding begins.

### Verify Changes with Playwright (MANDATORY)

**After implementing any new feature, you MUST:**

1. Start the Flask application (if not already running — `python src/app.py`)
2. Use the Playwright MCP tool to connect at `http://127.0.0.1:5000`
3. Navigate to and interact with the new feature
4. Take a screenshot and save it to `test-output/` with a descriptive filename (e.g., `feature-name-verification-YYYY-MM-DD.png`)

### UI / Design System

All UI changes must follow `.claude/skills/ui-designer/references/design-system.md`:
- Colors: use only palette variables (primary `#2563eb`, neutrals, semantic)
- Spacing: multiples of 4px using `--space-*` tokens
- Typography: Inter font, minimum 14px text, 16px body
- Components: use `.btn`, `.card`, `.input` patterns
- Mobile-first responsive design required
