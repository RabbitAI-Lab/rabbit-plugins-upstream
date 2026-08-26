## Description:

Qase (qase.io). Use this skill for ANY Qase request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA teams use this skill to operate Qase projects, test cases, and test runs through an OOMOL-connected account. It supports read workflows and user-confirmed write actions for creating cases, creating runs, and completing active runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can modify Qase projects, test cases, or test runs.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: First-time setup commands can affect CLI authentication or account connections.

Mitigation: Run setup steps only after the matching command, authentication, or connection failure occurs.

Risk: Connector input and output schemas can differ from static examples.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [ClawHub Qase Skill](https://clawhub.ai/oomol/skills/oo-qase)
- [Qase Homepage](https://qase.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
