## Description:

Agora (agora.io). Use this skill for ANY Agora request - reading, creating, updating, and deleting data. Whenever a task involves Agora, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Agora Console projects through an OOMOL-connected account, including listing projects, retrieving usage, creating projects, changing project status, and managing primary certificates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute unverified code.

Mitigation: Review the installer source and install the oo CLI only through a verified, trusted method; do not allow an agent to run curl|bash or irm|iex setup commands automatically.

Risk: Write and destructive Agora actions can change project state or reset a primary App Certificate.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-agora)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Agora homepage](https://www.agora.io)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI commands, action schema inspection steps, JSON request payloads, and JSON connector responses.]

## Skill Version(s):

1.0.2 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
