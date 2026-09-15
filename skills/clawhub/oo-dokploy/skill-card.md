## Description:

Dokploy (dokploy.com). Use this skill for Dokploy requests that read, create, update, or delete data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and operate Dokploy projects, servers, environments, applications, compose services, domains, deployments, logs, git providers, and database services through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Dokploy actions can interrupt deployments, stop services, or alter routing and environment configuration.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions.

Risk: Destructive Dokploy actions can remove deployment history, domains, or environments.

Mitigation: Require explicit approval for destructive actions and verify identifiers against a read-only lookup first.

Risk: Remote installer commands for the OOMOL oo CLI can execute external code.

Mitigation: Run installer commands only after independently trusting and verifying the installer source.

Risk: Broad Dokploy/OOMOL credentials could allow disruptive deployment operations.

Mitigation: Use least-privilege Dokploy and OOMOL credentials appropriate to the requested task.

## Reference(s):

- [Dokploy homepage](https://dokploy.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Dokploy skill on ClawHub](https://clawhub.ai/oomol/skills/oo-dokploy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
