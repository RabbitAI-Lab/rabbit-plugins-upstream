## Description:

Contentstack Content Delivery helps agents search and read published Contentstack content types, entries, and assets through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to retrieve Contentstack schemas, published entries, assets, and content-type lists through an authenticated OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute a remote installer script before the oo CLI is installed.

Mitigation: Install the oo CLI through a verifiable package manager or official versioned installer with checksum or signature verification, and avoid elevated privileges unless the installer has been independently verified.

Risk: Connector actions depend on an authenticated OOMOL-connected Contentstack account.

Mitigation: Run authentication or connection setup only after an action fails with a matching auth or connection error, then retry the read-only action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-contentstack-content-delivery)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Contentstack](https://www.contentstack.com/)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; available actions are read-only get and list operations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
