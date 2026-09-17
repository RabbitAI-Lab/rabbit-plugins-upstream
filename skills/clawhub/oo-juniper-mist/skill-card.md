## Description:

The Juniper Mist skill helps agents search and read Juniper Mist account, organization, site, and device data through an OOMOL-connected connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Juniper Mist account, organization, site, and device data through an OOMOL-connected Juniper Mist connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only from verified OOMOL documentation or a signed/package-managed source, and do not run installer commands during routine read-only connector use.

Risk: Connector actions run against the user's Juniper Mist connection context.

Mitigation: Inspect the live action schema before each connector run and confirm any write or destructive payload with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-juniper-mist)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Juniper Mist AI](https://www.juniper.net/us/en/products/networking/mist-ai.html)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
