## Description:

This skill helps agents manage Tremendous data through the OOMOL oo CLI, including reading records, creating orders, generating reward links, and listing campaigns, funding sources, products, and rewards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent perform Tremendous account workflows through an OOMOL-connected account, including reward orders, reward links, campaigns, funding sources, products, rewards, and organization lookups. The skill expects live action schemas to be fetched before requests and requires confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can run a remote installer pipeline for the oo CLI.

Mitigation: Install or update the oo CLI only after independently verifying the installer source and integrity.

Risk: The skill routes Tremendous connector credentials and reward/order data through a third-party OOMOL-connected account.

Mitigation: Use the skill only when the publisher and connector are trusted for the relevant Tremendous credentials and business data.

Risk: State-changing Tremendous actions can create orders or generate reward links.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Tremendous homepage](https://www.tremendous.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tremendous)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI commands, action-schema guidance, JSON request payloads, and connector responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
