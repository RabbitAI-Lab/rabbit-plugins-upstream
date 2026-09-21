## Description:

Convex (convex.dev). Use this skill for ANY Convex request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Convex projects, deployments, deploy keys, custom domains, and functions through an OOMOL-connected account. The skill guides agents to inspect live action schemas before building connector payloads and to request approval before state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Convex projects, deployments, deploy keys, and deployment settings.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before write actions.

Risk: Destructive actions can delete Convex resources or execute mutations, actions, and arbitrary functions against a deployment.

Mitigation: Require explicit user approval for the target resource and operation before any destructive action.

Risk: First-time setup may require installing or authenticating the oo CLI.

Mitigation: Review the installer path before running it and perform setup only after a command fails because the CLI, authentication, or Convex connection is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-convex)
- [Convex Homepage](https://www.convex.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Convex App Connection](https://console.oomol.com/app-connections?provider=convex)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and Convex connector; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
