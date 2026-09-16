## Description:

LinkFox helps agents operate a connected LinkFox account through OOMOL's oo CLI to read, create, and update ecommerce intelligence and compliance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce operators use this skill to run LinkFox searches, reports, marketplace analytics, IP risk checks, and connected Amazon Ads or store workflows through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Download the installer separately, verify its source and integrity, and review it before execution.

Risk: Some actions can affect connected accounts or account-scoped data, including Amazon, ads, store, order, billing, and write-capable workflows.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect before running write-capable or sensitive account actions.

## Reference(s):

- [LinkFox homepage](https://www.linkfox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-linkfox)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON data with execution metadata when actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
