## Description:

Dokploy (dokploy.com). Use this skill for Dokploy requests, including reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Dokploy projects, servers, environments, applications, compose services, domains, deployments, and service logs through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes unverified network-fetched installer commands for the oo CLI.

Mitigation: Review the installer path before use, prefer a verified package or documented release with checksum or signature validation, and avoid running installer commands automatically.

Risk: Write and destructive Dokploy actions can change service state, interrupt deployments, or remove routing, environments, or deployment history.

Mitigation: Inspect the live action schema, confirm the exact target, payload, and expected effect with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dokploy)
- [Dokploy Homepage](https://dokploy.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Dokploy connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
