## Description:

PDFMonkey helps agents read, create, update, list, and poll PDFMonkey documents and templates through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage PDFMonkey documents and templates from an agent workflow while relying on OOMOL-connected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code on the user's machine.

Mitigation: Prefer a verified, version-pinned oo CLI installation method and review installer contents before execution.

Risk: Write actions can create documents or queue PDF generation in the connected PDFMonkey account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [PDFMonkey homepage](https://pdfmonkey.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [PDFMonkey skill on ClawHub](https://clawhub.ai/oomol/skills/oo-pdfmonkey)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
