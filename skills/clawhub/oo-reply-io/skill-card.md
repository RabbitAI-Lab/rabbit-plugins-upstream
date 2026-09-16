## Description:

Reply.io (reply.io). Use this skill for ANY Reply.io request -- reading, creating, and updating data. Whenever a task involves Reply.io, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Reply.io through an OOMOL-connected account, including contact management, sequence lookup, and controlled sequence state changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute shell content directly.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI through a trusted, reviewable, version-pinned method where possible.

Risk: Write actions can change Reply.io contacts or sequence state.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Reply.io homepage](https://reply.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-reply-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing Reply.io action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
