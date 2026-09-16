## Description:

Front (front.com). Use this skill for ANY Front request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Front through an OOMOL-connected account, including inspecting live connector schemas and running read or write actions for contacts and teammates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute arbitrary code.

Mitigation: Review the setup path before installation and prefer an official package manager, pinned release, checksum, or signed installer for the oo CLI.

Risk: Front write actions can change contact data.

Mitigation: Confirm the exact JSON payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Front skill page](https://clawhub.ai/oomol/skills/oo-front)
- [Front homepage](https://front.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text URL, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live action schemas before constructing payloads and to confirm write or destructive actions before execution.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
