## Description:

This skill lets an agent read, create, update, and delete Dokploy resources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Dokploy projects, servers, environments, applications, compose services, domains, deployments, logs, and database services through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer infrastructure and includes actions that create, update, stop, delete, deploy, rebuild, reload, kill, or cancel Dokploy resources.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any state-changing or destructive action.

Risk: The documented first-time setup includes remote installer pipe commands for the oo CLI.

Mitigation: Prefer a pinned, verifiable oo CLI release or trusted package manager before running the skill.

## Reference(s):

- [ClawHub Dokploy Skill](https://clawhub.ai/oomol/skills/oo-dokploy)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Dokploy Homepage](https://dokploy.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
