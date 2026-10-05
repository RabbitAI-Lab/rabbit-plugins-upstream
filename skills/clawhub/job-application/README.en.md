# Job Application Skill for OpenClaw

[Deutsche Dokumentation](README.md)

This skill creates a tailored CV, cover letter, and plain-text application from structured profile data. All bundled personal, employer, and application data is fictional.

The bundled portrait of Mira Hoffmann was AI-generated and does not depict a real person. For actual applications, remove `profile_picture` from `assets/profile/master_profile.json` or point it to your own image.

## Requirements

- OpenClaw with support for local skills
- Python 3.10 or newer; no additional Python packages are required
- A LaTeX distribution that provides `pdflatex` on `PATH`
- Bash for the optional Linux/macOS wrapper

Suitable LaTeX distributions include:

- Linux: TeX Live from your distribution's package manager
- Windows: MiKTeX or TeX Live
- macOS: MacTeX or BasicTeX with the required packages

The templates use common packages: `geometry`, `fontenc`, `inputenc`, `lmodern`, `xcolor`, `graphicx`, `tikz`/PGF, `textpos`, `ragged2e`, and `hyperref`. You may need to add these packages to a minimal LaTeX installation. MiKTeX can optionally install missing packages during the first run.

Verify the installation:

```text
python3 --version
pdflatex --version
```

On Windows, the Python command is often `py -3` instead of `python3`.

## Keeping private data safe across updates

Store real profile data and generated applications outside the installed skill directory. The skill supports two optional environment variables:

```text
JOB_APPLICATION_PROFILE_DIR=/path/to/private/profile
JOB_APPLICATION_OUTPUT_DIR=/path/to/applications
```

OpenClaw can provide these under `skills.entries.job-application.env`. ClawHub updates then replace only skill code, templates, and fictional examples. Your profile, personal photograph, and applications remain unchanged. Without configuration, the skill uses the bundled fictional profile and `./applications`.

## Does the skill work on Linux and Windows?

Yes. The generators and PDF renderer are implemented in Python and use platform-independent paths. The complete PDF workflow has been tested on Linux. On Windows, Python and either MiKTeX or TeX Live must be installed and available on `PATH`. The Bash script is only a convenience wrapper for Linux and macOS; Windows users run `scripts\render_application.py` directly.

PDF output can vary slightly between LaTeX distributions in font metrics or document metadata. The content and general layout remain the same.

## Quick test

Linux/macOS, from the skill directory:

```bash
python3 scripts/prepare_application.py --slug 2026-09-example-demo
cp examples/*.json applications/2026-09-example-demo/
python3 scripts/generate_cv_selection.py --job applications/2026-09-example-demo/job.json --output applications/2026-09-example-demo/cv_selection.json
python3 scripts/generate_cv.py --selection applications/2026-09-example-demo/cv_selection.json --output applications/2026-09-example-demo/CV.tex
python3 scripts/generate_cover_letter.py --content applications/2026-09-example-demo/cover_letter.json --output applications/2026-09-example-demo/cover_letter.tex
python3 scripts/generate_plain_text.py --content applications/2026-09-example-demo/indeed_text.json --output applications/2026-09-example-demo/indeed_text.txt
python3 scripts/render_application.py applications/2026-09-example-demo
```

Windows PowerShell, from the skill directory:

```powershell
py -3 scripts\prepare_application.py --slug 2026-09-example-demo
Copy-Item examples\*.json applications\2026-09-example-demo\
py -3 scripts\generate_cv_selection.py --job applications\2026-09-example-demo\job.json --output applications\2026-09-example-demo\cv_selection.json
py -3 scripts\generate_cv.py --selection applications\2026-09-example-demo\cv_selection.json --output applications\2026-09-example-demo\CV.tex
py -3 scripts\generate_cover_letter.py --content applications\2026-09-example-demo\cover_letter.json --output applications\2026-09-example-demo\cover_letter.tex
py -3 scripts\generate_plain_text.py --content applications\2026-09-example-demo\indeed_text.json --output applications\2026-09-example-demo\indeed_text.txt
py -3 scripts\render_application.py applications\2026-09-example-demo
```

The results will be written to `applications/2026-09-example-demo/`. Pre-generated examples are available in `examples/generated/`.

## Using your own data

Keep the files in `assets/profile/` as public fictional examples. Store your own JSON files with the same structure and the optional profile image in a private directory outside the skill, then point `JOB_APPLICATION_PROFILE_DIR` to it. Relative image paths are resolved from the profile directory. This keeps personal data out of the published repository and safe from skill updates.

Projects can optionally be attributed to an organization and a professional context. `context` is the stable machine-readable value, while `context_label` is displayed in the CV:

```json
{
  "organization": "Example Company GmbH",
  "context": "employment",
  "context_label": "Created as part of employment"
}
```

For projects created through the candidate's own company, use `own_company` with a suitable visible label such as `Own company`. If these fields are absent, the existing project subtitle is rendered on its own.

The skill does not automatically send or publish applications. External delivery always requires explicit authorization for the specific destination.

## Development with OpenSpec

The shipped behavior contracts live in `openspec/specs/`. OpenSpec changes are planned separately under `openspec/changes/` and archived into the current specifications after implementation.

Node.js 20.19 or newer is required. Install and validate with:

```bash
npm install -g @fission-ai/openspec
openspec --version
openspec validate --specs --strict
```

Start a change with `openspec new change <change-id>`. Review its proposal, specification delta, design, and tasks before implementation. After implementation and validation, use `openspec archive <change-id>` to merge the change into the main specifications.

This repository intentionally uses tool-neutral OpenSpec initialization so that additional agent skills are not included in the published ClawHub package.
