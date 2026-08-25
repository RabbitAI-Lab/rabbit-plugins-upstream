## Description:

Resume Review helps an agent evaluate a resume across six dimensions, generate a concise humorous review JSON, and render a 1200x1600 JOJO-style stat panel PNG.

This skill is ready for commercial/non-commercial use.

## Publisher:

[padepa](https://clawhub.ai/user/padepa)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to turn a resume into a shareable visual review. The workflow extracts resume text, asks an LLM to create anonymized scoring data, renders a local PNG panel, and returns a short improvement summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume contents may be processed by the user's chosen external AI model or provider.

Mitigation: Remove or mask names, contact details, IDs, school names, company names, and other sensitive details before sending resume text to an external model.

Risk: The resume extraction helper can write raw resume text to a local file.

Mitigation: Write extracted text only to a controlled local path, delete it after use, and avoid committing or sharing raw resume text.

Risk: The rendering script does not automatically redact private details from generated panel data.

Mitigation: Review the panel JSON before rendering and confirm that persona, verdict, ability text, and dimension labels contain only anonymized or share-safe content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/padepa/skills/resume-review)
- [README](README.md)
- [Roast prompt](references/roast-prompt.md)
- [Humor style and scoring guide](references/humor-style.md)
- [Panel template](templates/panel_template.json)
- [Intro video script](docs/intro-video-script.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, panel JSON, and a rendered PNG file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The rendered image is 1200x1600 PNG; the panel JSON must contain six fixed scoring dimensions.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
