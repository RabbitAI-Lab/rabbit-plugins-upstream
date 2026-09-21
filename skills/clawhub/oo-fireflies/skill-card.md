## Description:

Fireflies (fireflies.ai). Use this skill for ANY Fireflies request - reading, creating, updating, and deleting data. Whenever a task involves Fireflies, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Fireflies through an OOMOL-connected account for meeting transcripts, users, channels, groups, bites, AI app outputs, and AskFred threads. It supports read operations as well as confirmed write and destructive Fireflies actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include one-line remote shell installer commands for the oo CLI.

Mitigation: Install only after trusting OOMOL's CLI distribution path, and prefer a verified or manual install method before running installer scripts.

Risk: The skill can perform state-changing or destructive Fireflies actions such as transcript deletion, role changes, privacy changes, and meeting updates.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Fireflies Skill](https://clawhub.ai/oomol/skills/oo-fireflies)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Fireflies Homepage](https://www.fireflies.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect action schemas and run Fireflies connector actions; command responses are JSON with data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
