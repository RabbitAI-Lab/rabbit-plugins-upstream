## Description:

Kit (kit.com). Use this skill for ANY Kit request - reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Kit connector schemas, list or retrieve Kit data, and create or update Kit subscribers through an authenticated OOMOL account. It is intended for Kit account operations where write actions require confirming the exact payload and effect first.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the agent to run unverified remote installer scripts for the oo CLI.

Mitigation: Review the skill before installation and prefer a verified, pinned, or package-manager-based oo CLI installation method.

Risk: Kit write actions can create or update subscriber data.

Mitigation: Confirm the exact subscriber payload and intended effect with the user before allowing write commands to run.

## Reference(s):

- [Kit homepage](https://kit.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the oo CLI and may return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
