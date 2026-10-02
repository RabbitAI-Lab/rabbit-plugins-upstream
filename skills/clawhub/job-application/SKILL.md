---
name: job-application
description: Creates tailored job-application materials from structured profile and job data, including a focused CV, cover letter, plain-text application, and optional local PDF rendering. Use for drafting or rendering an application; do not use for submitting it without explicit authorization.
license: MIT-0
metadata:
  openclaw:
    requires:
      bins: [pdflatex]
      anyBins: [python3, python, py]
    envVars:
      - name: JOB_APPLICATION_PROFILE_DIR
        required: false
        description: Persistent profile directory outside the installed skill; bundled fictional data is used when unset.
      - name: JOB_APPLICATION_OUTPUT_DIR
        required: false
        description: Persistent application output root outside the installed skill; ./applications is used when unset.
---

# Job application

Create truthful, role-specific application documents from the bundled structured profile or a profile supplied by the user.

## Privacy and authorization

- Treat all profile and application data as private.
- Never invent qualifications, employment, education, or contact details.
- The bundled profile is fictional demonstration data and may be replaced by the user.
- Do not submit, email, upload, or message an application without explicit authorization for that specific destination.

## Persistent data and inputs

- Profile data: `$JOB_APPLICATION_PROFILE_DIR/*.json` when configured, otherwise the fictional demonstration data in `assets/profile/*.json`
- Application output: `$JOB_APPLICATION_OUTPUT_DIR` when configured, otherwise `applications/` in the user's working directory
- Job data: a `job.json` shaped like `examples/job.json`
- Templates: `assets/templates/`

Keep real profiles, photographs, generated documents, and application history outside the installed skill directory. ClawHub updates may replace that directory. Resolve bundled resources relative to this skill directory, but honor the two environment variables for private persistent data. Do not assume a username, home directory, workspace layout, messaging channel, or recipient ID.

## Workflow

1. Create the application folder with `python3 scripts/prepare_application.py --slug <yyyy-mm-company-role>`. Use the printed absolute path for all following files. Never overwrite an existing application directory unless the user explicitly requests reuse.
2. Save normalized job details as `job.json`.
3. Run `scripts/generate_cv_selection.py --job <job.json> --output <cv_selection.json>`. Review its deterministic suggestion and adjust only with facts supported by the profile.
4. Create `cover_letter.json` and `indeed_text.json` using the example schemas. Keep claims grounded in selected profile records.
5. Generate source documents:

   ```bash
   python3 scripts/generate_cv.py --selection <cv_selection.json> --output <CV.tex>
   python3 scripts/generate_cover_letter.py --content <cover_letter.json> --output <cover_letter.tex>
   python3 scripts/generate_plain_text.py --content <indeed_text.json> --output <indeed_text.txt>
   ```

6. If `pdflatex` is available and PDFs are requested, run the cross-platform renderer:

   ```bash
   python3 scripts/render_application.py <application-dir>
   ```

   On Windows, `py -3` can be used instead of `python3`. Linux and macOS users may alternatively use the `scripts/render_application.sh` wrapper.
7. Return the generated paths. Deliver files externally only after destination-specific approval.

Installation requirements and platform-specific commands are documented in `README.md`. Generated sample PDFs using only fictional data are in `examples/generated/`.

## Content policy

- Default to a one-page CV.
- Use at most five skills, three experience entries, two education entries, one project, and three languages.
- Prefer evidence relevant to the posting over generic claims.
- Keep each experience entry to at most two concise achievement sentences.
- Preserve optional project attribution fields (`organization`, `context`, and `context_label`) so generated CVs can distinguish employer projects from work performed through the candidate's own company.
- Omit date of birth, signature image, and full street address by default. Include a profile photograph only when the user requests one or the supplied profile explicitly declares `profile_picture`; the bundled photo is fictional demonstration material.
- Match the job's language unless the user requests another language.

JSON contains content, Python performs deterministic transformation, and LaTeX handles layout. Do not hand-edit generated LaTeX when the source JSON can be corrected instead.
