## Description:

Resource Flow (Hub Planner) helps agents read, create, and update Hub Planner projects and resources through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Resource Flow (Hub Planner) projects and resources from an agent-connected OOMOL account. It supports read operations and guarded creation of projects and resources after checking the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute unreviewed code during first-time setup.

Mitigation: Review the installer source before use, prefer a pinned verified release or trusted package manager, and do not let an agent run the remote installer automatically.

Risk: Project and resource creation actions change Hub Planner state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Resource Flow (Hub Planner) homepage](https://www.milientsoftware.com/hub-planner)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hub-planner)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands and JSON payloads for Hub Planner connector actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
