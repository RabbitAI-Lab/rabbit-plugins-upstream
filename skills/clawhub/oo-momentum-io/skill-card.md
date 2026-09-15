## Description:

Momentum.io helps agents search and read Momentum.io meetings, users, signal prompts, signal definitions, and signal execution history through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers with OOMOL-connected Momentum.io accounts use this skill to inspect meeting records, organization users, signal prompts, definitions, and execution history without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could be unsafe if executed without verification.

Mitigation: Review installer instructions, prefer an official signed or package-manager installation path, and verify downloaded installers before execution.

Risk: Using connector actions outside the documented read-only lookup posture or with an unconfirmed payload could produce unintended Momentum.io access or effects.

Mitigation: Use the skill for read-only Momentum.io lookup tasks, fetch the live action schema before each action, and confirm the exact action and payload before any non-read operation.

## Reference(s):

- [Momentum.io homepage](https://www.momentum.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
