## Description:

CoderPad lets an agent read, create, and update CoderPad data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and recruiting teams use this skill to manage CoderPad interview pads, questions, organization details, usage statistics, and event histories through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts directly in a shell.

Mitigation: Use a safer verified installation method for the oo CLI before installing.

Risk: The create_pad action changes CoderPad state.

Mitigation: Confirm the exact create_pad payload and expected effect with the user before running it.

Risk: Read actions may expose CoderPad organization, user, interview, question, and event data through the connected OOMOL account.

Mitigation: Limit requests to the data needed for the task and avoid sharing retrieved CoderPad data beyond the intended user context.

## Reference(s):

- [CoderPad homepage](https://coderpad.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing CoderPad actions require explicit user confirmation; oo CLI action responses are JSON.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
