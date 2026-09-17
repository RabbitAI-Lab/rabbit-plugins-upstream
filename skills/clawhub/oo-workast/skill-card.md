## Description:

Workast (workast.com) skill for reading, creating, and updating Workast data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External Workast users and teams use this skill to inspect action schemas, read Workast user, space, and task details, and create, update, or complete tasks through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts.

Mitigation: Verify the official installer source and local effects before running installer commands, or install the oo CLI through a trusted reviewed path.

Risk: Write actions can change Workast task state.

Mitigation: Confirm the exact payload and intended effect before create, update, or complete task actions.

Risk: Connected Workast access is mediated by OOMOL.

Mitigation: Use only a Workast account you intend OOMOL to access and review connection scopes before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-workast)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Workast homepage](https://www.workast.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Workast action results returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
