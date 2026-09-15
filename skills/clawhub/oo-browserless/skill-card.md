## Description:

Browserless lets agents operate Browserless through the OOMOL oo CLI to fetch rendered webpage content and generate PDFs or screenshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Browserless actions through an OOMOL-connected account, including fetching rendered HTML, producing PDFs, and taking screenshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run a remotely downloaded installer without integrity verification.

Mitigation: Before running setup commands, use the official install guide, inspect the downloaded installer, and verify its source or checksum if available.

## Reference(s):

- [ClawHub Browserless skill page](https://clawhub.ai/oomol/skills/oo-browserless)
- [Browserless homepage](https://www.browserless.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browserless action results may include JSON responses with rendered HTML or base64-encoded PDF and screenshot data.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
