## Description:

Docsend2pdf converts DocSend document URLs to PDF download metadata through the docsend_2_pdf connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the live Docsend2pdf connector schema, submit a DocSend URL for conversion, and return JSON-safe PDF download metadata without handling raw service credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include unverified remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, reviewed, version-pinned method and verify the source before allowing agent use.

Risk: The skill runs connector actions that fetch PDF conversion results from a third-party service.

Mitigation: Inspect the live connector schema before execution and review the DocSend URL and expected conversion target with the user when the request is sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsend-2-pdf)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Docsend2pdf homepage](https://docsend2pdf.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action output is JSON-safe PDF download metadata with execution details.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
