## Description:

Healthchecks.io (healthchecks.io). Use this skill for ANY Healthchecks.io request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Healthchecks.io checks, notification metadata, pings, and status history through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could run arbitrary code if the installer source or transport is compromised.

Mitigation: Review the setup path before installing and prefer a verified, versioned oo CLI package or independently check installer contents and integrity before execution.

Risk: The skill can create, update, pause, resume, and delete Healthchecks.io checks.

Mitigation: Confirm write and delete payloads, targets, and intended effects before allowing the skill to act.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-healthchecks-io)
- [Healthchecks.io homepage](https://healthchecks.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Healthchecks.io actions through the oo CLI after inspecting the live action schema.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
