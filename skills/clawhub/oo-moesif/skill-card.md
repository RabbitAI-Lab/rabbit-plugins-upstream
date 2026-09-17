## Description:

Moesif (moesif.com). Use this skill for ANY Moesif request - searching and reading data. Whenever a task involves Moesif, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Moesif apps, workspaces, workspace templates, and individual workspaces through an OOMOL-connected account. It is intended for read-oriented Moesif discovery workflows where the agent first checks the connector schema and then runs the selected action with a matching JSON payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Moesif metadata and connector responses are routed through OOMOL.

Mitigation: Install and use the skill only when that routing is acceptable for the workspace and data involved.

Risk: The first-time setup section includes remote installer commands.

Mitigation: Review and verify the CLI installation method before running installer commands, and do not allow an agent to run them automatically.

Risk: The release security verdict is suspicious despite the listed connector actions being read-oriented.

Mitigation: Limit routine use to the listed get and list actions unless the user explicitly approves a broader action and payload.

## Reference(s):

- [Moesif homepage](https://www.moesif.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Moesif skill page](https://clawhub.ai/oomol/skills/oo-moesif)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
