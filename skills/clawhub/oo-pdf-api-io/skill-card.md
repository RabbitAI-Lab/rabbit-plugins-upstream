## Description:

PDF-API.io helps agents operate PDF-API.io through the OOMOL pdf_api_io connector to list templates, retrieve template details, and render PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected PDF-API.io account from an agent: list templates, retrieve template details, and render templates with JSON data into temporary hosted PDF URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may run an unverified remote installer for the oo CLI.

Mitigation: Use a verified or package-manager-based oo CLI installation path before allowing an agent to execute connector commands.

Risk: PDF rendering may send user-provided payload data to PDF-API.io and create a temporary hosted PDF URL.

Mitigation: Review render_pdf payloads and confirm the intended data exposure before rendering templates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pdf-api-io)
- [PDF-API.io Homepage](https://pdf-api.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce temporary hosted PDF URLs from PDF-API.io render operations.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
