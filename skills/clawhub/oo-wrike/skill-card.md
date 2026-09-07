## Description:

Wrike helps an agent read Wrike data and create folders or tasks through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate on Wrike contacts, folders, projects, and tasks through the oo CLI connector, including read actions and confirmed create actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses a user's Wrike account through OOMOL.

Mitigation: Install it only when Wrike access through OOMOL is intended, and use trusted oo CLI setup sources.

Risk: Create actions can change folders and tasks in the Wrike workspace.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Incorrect connector input can cause failed or unintended operations.

Mitigation: Fetch the live connector schema before constructing each action payload.

## Reference(s):

- [Wrike ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-wrike)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Wrike homepage](https://www.wrike.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
