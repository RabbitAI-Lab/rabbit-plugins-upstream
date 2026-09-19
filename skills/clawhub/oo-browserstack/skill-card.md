## Description:

BrowserStack (browserstack.com). Use this skill for ANY BrowserStack request: reading, creating, and updating data through the OOMOL-connected BrowserStack connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and release teams use this skill to inspect BrowserStack Automate builds and sessions, retrieve session details, and update session status after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include installer commands that execute downloaded code directly.

Mitigation: Review the installer path before use and prefer a pinned package, checksum or signature verification, or manual inspection of the oo CLI installer.

Risk: The skill can update BrowserStack session status.

Mitigation: Confirm the exact payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [BrowserStack homepage](https://www.browserstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browserstack)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing BrowserStack connector requests; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
