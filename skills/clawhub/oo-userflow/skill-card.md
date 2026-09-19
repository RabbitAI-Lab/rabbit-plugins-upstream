## Description:

Enables agents to inspect Userflow connector schemas and run Userflow actions through OOMOL's oo CLI for users, groups, and events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Teams that use Userflow can ask an agent to read users and groups, list users with filters and pagination, track events, and create, update, or delete Userflow records through an OOMOL-connected account. The skill is intended for agents that need to inspect live action schemas before constructing Userflow requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installation and prefer a verified package, signed release, or inspected download.

Risk: Write and destructive Userflow actions can create, update, or delete users and groups.

Mitigation: Require explicit approval for the exact target, payload, and expected effect before running write or delete actions.

## Reference(s):

- [Userflow homepage](https://userflow.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Userflow skill page](https://clawhub.ai/oomol/skills/oo-userflow)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI with a connected Userflow account.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
