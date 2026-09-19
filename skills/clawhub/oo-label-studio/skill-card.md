## Description:

Label Studio support for reading, creating, and updating Label Studio data through the OOMOL Label Studio connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Label Studio account, project, and task data and to create projects or individual tasks through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands that can execute code on the user's machine.

Mitigation: Review the setup path before installing and prefer a pinned, verified oo CLI release or trusted package manager.

Risk: Write actions can modify Label Studio projects or tasks.

Mitigation: Confirm the exact payload and expected effect with the user before running create or other write actions.

## Reference(s):

- [Label Studio homepage](https://labelstud.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Label Studio skill page](https://clawhub.ai/oomol/skills/oo-label-studio)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses when Label Studio actions are executed.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
