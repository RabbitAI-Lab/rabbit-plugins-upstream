# PDF Rendering Specification

## Purpose

Defines portable generation and local rendering of application documents on supported desktop platforms while preserving useful source artifacts and errors.

## Requirements

### Requirement: LaTeX source generation
The skill SHALL generate `CV.tex` and `cover_letter.tex` from structured JSON inputs and bundled templates.

#### Scenario: Valid content is supplied
- **GIVEN** valid profile, selection, and cover-letter JSON
- **WHEN** the source generators run
- **THEN** they produce compilable LaTeX source files in the application directory

### Requirement: Local PDF rendering
The renderer SHALL create `CV.pdf` and `cover_letter.pdf` when `pdflatex` is available and both LaTeX source files exist.

#### Scenario: Render complete application
- **GIVEN** `pdflatex`, `CV.tex`, and `cover_letter.tex` are available
- **WHEN** the renderer processes the application directory
- **THEN** both PDF files are generated locally
- **AND** a build log is retained

#### Scenario: LaTeX is unavailable
- **GIVEN** `pdflatex` is not available on `PATH`
- **WHEN** PDF rendering is requested
- **THEN** the renderer exits with an actionable dependency error

#### Scenario: Source file is missing
- **GIVEN** one or both required LaTeX source files are absent
- **WHEN** PDF rendering is requested
- **THEN** the renderer exits without claiming successful PDF creation

### Requirement: Cross-platform execution
The Python renderer SHALL support Linux and Windows environments with Python and a LaTeX distribution installed.

#### Scenario: Windows execution
- **GIVEN** Python and MiKTeX or TeX Live are available on Windows
- **WHEN** the user invokes `scripts\\render_application.py` with the Python launcher
- **THEN** rendering does not require the Bash wrapper

#### Scenario: Linux execution
- **GIVEN** Python and TeX Live are available on Linux
- **WHEN** the user invokes the Python renderer or Bash convenience wrapper
- **THEN** the same application sources are rendered
