## Description:

OpenHands lets agents read, create, update, and monitor OpenHands Cloud conversations through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect OpenHands action schemas, list or retrieve conversations, start repository tasks, and send follow-up messages through an OOMOL-connected OpenHands account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts immediately.

Mitigation: Review the installer path before installing, and prefer a verified package manager or installer with a published checksum or signature.

Risk: Connected OOMOL and OpenHands credentials may allow actions against the linked account.

Mitigation: Connect only an account with acceptable permissions for this connector and confirm write-action payloads before execution.

Risk: Write actions such as starting conversations or sending messages can change OpenHands state.

Mitigation: Confirm the target conversation or repository task, payload, and expected effect with the user before running those actions.

## Reference(s):

- [OpenHands homepage](https://www.all-hands.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-open-hands)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require confirmation of the payload and expected effect.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
