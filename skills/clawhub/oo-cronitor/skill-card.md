## Description:

Cronitor (cronitor.io). Use this skill for ANY Cronitor request - reading, creating, updating, and deleting data. Whenever a task involves Cronitor, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect, list, retrieve, create, update, and delete Cronitor monitors through an OOMOL-connected account without handling raw Cronitor API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute downloaded code if followed.

Mitigation: Review installer sources before running them and prefer verified package-manager or trusted installation instructions for the oo CLI.

Risk: The skill can create, update, or delete Cronitor monitors.

Mitigation: Confirm exact payloads and effects before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Cronitor homepage](https://cronitor.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cronitor Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-cronitor)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before requests and returns oo CLI JSON responses for connector runs.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
