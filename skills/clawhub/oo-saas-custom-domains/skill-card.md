## Description:

Enables agents to manage SaaS Custom Domains accounts, upstreams, custom domains, DNS verification, and cache purges through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect SaaS Custom Domains action schemas and run account, upstream, custom-domain, DNS verification, and cache-purge actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes mutable remote installer commands that execute directly in a shell.

Mitigation: Install the oo CLI through a trusted, reviewable, pinned, or verified method before using the skill.

Risk: Write and destructive connector actions can create, delete, or purge SaaS Custom Domains resources.

Mitigation: Confirm the exact payload, target resource, and intended effect with the user before running any write or destructive action.

## Reference(s):

- [SaaS Custom Domains homepage](https://saascustomdomains.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-saas-custom-domains)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
