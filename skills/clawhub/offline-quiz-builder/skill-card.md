## Description:

Transforms study materials or existing question banks into a fully offline quiz and spaced-review website with local browser storage and optional daily reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hounextitem](https://clawhub.ai/user/hounextitem)

### License/Terms of Use:

MIT-0

## Use Case:

Learners, educators, and developers use this skill to convert notes, documents, spreadsheets, PDFs, or existing question banks into a local quiz site for practice and spaced review. It is also useful when a user wants a no-network study tool with question validation, progress tracking, and optional daily reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser-opening helper can pass a user-influenced local path through shell commands in fallback cases.

Mitigation: Use simple generated site paths without quotes or unusual shell characters, and consider skipping reminders until open_quiz.py is changed to invoke platform open commands without a shell.

Risk: Quiz content generated from study materials can contain incorrect or misleading questions or answers.

Mitigation: Run the build_bank.py validation step and review the required sample questions before building the final site.

Risk: Learning progress is stored only in browser localStorage and can be lost or split if the site path, browser, cache state, or opening method changes.

Mitigation: Open the generated quiz through the same file:// path, avoid local HTTP previews for reminders, and warn users before moving the site or clearing browser data.

## Reference(s):

- [Question Schema](references/question-schema.md)
- [Material Ingestion](references/material-ingestion.md)
- [Automation Reminder](references/automation-reminder.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON question-bank data, generated static HTML/CSS/JavaScript site files, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated site is designed for offline file:// use; learning progress is stored in the user's browser localStorage.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
