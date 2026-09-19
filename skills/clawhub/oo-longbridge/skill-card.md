## Description:

Longbridge (longbridge.com) skill for reading, creating, and updating Longbridge data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents supporting Longbridge users use this skill to inspect action schemas, retrieve market and account data, and run supported Longbridge connector actions with confirmation for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes shell and PowerShell commands that directly execute remote installer scripts.

Mitigation: Use a verified installer when available, or inspect and verify the downloaded script before executing it.

Risk: Longbridge account data is accessed through OOMOL as an intermediary.

Mitigation: Install only when the user accepts OOMOL's role in handling connected Longbridge account access.

Risk: Tagged write or destructive actions can change Longbridge state.

Mitigation: Fetch the live schema, present the exact payload and expected effect, and obtain explicit user confirmation before execution.

## Reference(s):

- [ClawHub Longbridge skill page](https://clawhub.ai/oomol/skills/oo-longbridge)
- [Longbridge homepage](https://longbridge.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads/responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Longbridge connector payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
