## Description:

Enables agents to inspect Retently action schemas and run Retently account, customer, feedback, template, campaign, and customer upsert operations through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read Retently account, customer, feedback, template, and campaign data and, after confirmation, bulk create or update Retently customers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unreviewed code during setup.

Mitigation: Install the oo CLI through a verified, pinned, or package-manager-based method before using the skill.

Risk: Retently customer and feedback data may be processed through OOMOL.

Mitigation: Confirm organizational approval for this data path before running connector actions.

Risk: Bulk customer upsert actions can change Retently records.

Mitigation: Review the live action schema and confirm the exact payload and expected effect with the user before write operations.

## Reference(s):

- [Retently homepage](https://www.retently.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Retently connection](https://console.oomol.com/app-connections?provider=retently)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Retently connector responses as JSON through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
