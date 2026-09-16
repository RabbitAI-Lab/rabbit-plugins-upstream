## Description:

Recruitee (recruitee.com). Use this skill for Recruitee requests involving reading, creating, and updating data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and recruiting teams use this skill to have an agent operate Recruitee through an OOMOL-connected account. It supports reading offers, listing offers, searching candidates, and creating candidates when the user confirms the write payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes running a remote installer directly in a shell.

Mitigation: Review the setup commands first, and prefer a verified, version-pinned oo CLI install or inspect the installer before execution.

Risk: The create_candidate action changes Recruitee data.

Mitigation: Confirm the exact payload and intended effect with the user before running the write action.

## Reference(s):

- [Recruitee homepage](https://recruitee.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recruitee)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
