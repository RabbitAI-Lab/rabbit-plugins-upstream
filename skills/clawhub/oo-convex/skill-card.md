## Description:

Convex (convex.dev). Use this skill for ANY Convex request, including reading, creating, updating, and deleting data through the OOMOL `oo` CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Convex action schemas and manage Convex projects, deployments, regions, domains, deploy keys, and runtime function execution through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports unsafe installer commands in first-time setup guidance.

Mitigation: Review the installer source independently before running remote shell or PowerShell install pipelines, and prefer a trusted package or preinstalled `oo` CLI where available.

Risk: The security summary reports that some high-impact Convex operations are under-scoped.

Mitigation: Require explicit user confirmation for mutation, action, function, write, and delete operations, including the exact target deployment, project, function, and payload.

## Reference(s):

- [Convex homepage](https://www.convex.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Convex connection](https://console.oomol.com/app-connections?provider=convex)
- [Skill page](https://clawhub.ai/oomol/skills/oo-convex)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute `oo connector schema` and `oo connector run` commands when used by an agent with the allowed `oo` CLI tool.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
