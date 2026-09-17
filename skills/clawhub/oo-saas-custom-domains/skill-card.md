## Description:

SaaS Custom Domains helps agents read, create, update, and delete SaaS Custom Domains data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage SaaS Custom Domains accounts, upstreams, custom domains, DNS verification, and cache purges through OOMOL's `oo` CLI connector. It supports read workflows directly and requires confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Prefer installing the `oo` CLI through a verifiable release, package manager, checksum, or signature process before using the skill.

Risk: Create, delete, and purge actions can change or remove SaaS Custom Domains resources.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-saas-custom-domains)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SaaS Custom Domains Homepage](https://saascustomdomains.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
