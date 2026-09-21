## Description:

Kraken.io (kraken.io). Use this skill for ANY Kraken.io request: reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Kraken.io through an OOMOL-connected account, including checking plan status and optimizing images from URLs or uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes conditional remote installer commands for the oo CLI.

Mitigation: Install the oo CLI manually from official documentation with verification where possible, and do not let an agent run the remote installer automatically.

Risk: Image optimization is a write action that can submit data to Kraken.io and consume account quota.

Mitigation: Review and approve the exact optimization payload and expected effect before running the action.

Risk: Kraken.io actions are mediated through OOMOL-connected credentials.

Mitigation: Install only if you are comfortable with OOMOL acting as the intermediary for Kraken.io actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kraken-io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Kraken.io homepage](https://kraken.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect connector schemas and run Kraken.io actions; write actions require payload confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
