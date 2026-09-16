## Description:

Use OCR Web Service (ocrwebservice.com) for account lookup and document OCR through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect OCR Web Service account status and process public image or PDF URLs for extracted text or output file metadata through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes one-line remote installer commands that execute code from cli.oomol.com in the user's shell.

Mitigation: Review or verify the OOMOL installer source, or use a trusted package-manager installation path when available; run setup only after the oo CLI is missing or authentication fails.

## Reference(s):

- [OCR Web Service homepage](https://www.ocrwebservice.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ocr-web-service)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; connector responses include JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
