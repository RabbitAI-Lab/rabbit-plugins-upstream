## Description:

PhantomBuster (phantombuster.com). Use this skill for ANY PhantomBuster request -- reading, creating, and updating data. Whenever a task involves PhantomBuster, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PhantomBuster through an OOMOL-connected account, including reading agent, container, organization, and agent-list data. It can also launch and stop PhantomBuster agents when the user confirms the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags an unsafe remote installer command for the OOMOL CLI.

Mitigation: Use an already trusted CLI installation when possible, and independently verify the OOMOL installer source before running installer pipelines.

Risk: The skill can launch or stop PhantomBuster agents, which may change service state.

Mitigation: Confirm the target, payload, and expected effect with the user before launching or stopping agents.

Risk: The security summary notes that a state-changing action is under-labeled.

Mitigation: Treat launch and stop operations as state-changing even when labels are incomplete, and require explicit user confirmation before execution.

## Reference(s):

- [PhantomBuster homepage](https://phantombuster.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-phantombuster)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include PhantomBuster connector data returned as JSON.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
