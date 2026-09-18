## Description:

This skill helps agents search and read Shopify REST Admin (Legacy) data through the OOMOL Shopify connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Shopify shop, blog, article, page, author, and tag data through an OOMOL-connected account. The skill is limited to the listed read-only count, get, and list actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup uses remote shell installer commands for the oo CLI.

Mitigation: Install the oo CLI through a verified, versioned, or checksum-validated method before using this skill.

Risk: The skill depends on OOMOL's Shopify connector and connected-account credentials.

Mitigation: Use only the listed read-only actions and review live schemas before sending payloads.

## Reference(s):

- [Shopify](https://www.shopify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shopify)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI commands to inspect schemas and run read-only Shopify connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
