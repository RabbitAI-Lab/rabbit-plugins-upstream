## Description:

Buttondown (buttondown.com). Use this skill for ANY Buttondown request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Buttondown account data through an OOMOL-connected account, including subscribers, tags, newsletters, and account lookup. It supports read, write, and destructive Buttondown operations with confirmation guidance for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could execute arbitrary code if followed without verification.

Mitigation: Install the oo CLI through a trusted, verifiable process and do not allow an agent to run remote installer commands automatically.

Risk: Write and destructive Buttondown actions can change or delete subscribers and tags.

Mitigation: Confirm the exact payload, effect, and target with the user before running write actions, and require explicit approval before destructive actions.

Risk: Using the skill routes Buttondown account operations through OOMOL-connected infrastructure.

Mitigation: Connect Buttondown only when the user is authorized and comfortable using OOMOL for those account operations.

## Reference(s):

- [Buttondown homepage](https://buttondown.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return JSON results that include data and an execution id.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
