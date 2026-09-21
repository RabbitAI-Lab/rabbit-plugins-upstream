## Description:

Zoom (zoom.com). Use this skill for Zoom requests that read, create, and update meeting or user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Zoom through an OOMOL-connected account, including creating or updating meetings, listing meetings, and fetching user details. It is suited for external or employee workflows that need Zoom automation while confirming write actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote script execution for installing the OOMOL CLI.

Mitigation: Review the OOMOL CLI installation path before use and prefer an official documented installer with verification where available.

Risk: The skill can create or update Zoom meetings through the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Zoom homepage](https://www.zoom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zoom)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the oo CLI to return JSON connector responses containing data and an execution ID.]

## Skill Version(s):

1.0.5 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
