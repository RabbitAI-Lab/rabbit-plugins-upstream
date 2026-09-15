## Description:

Lingxing enables agents to operate the Lingxing connector through an OOMOL-connected account for reading, creating, and updating Lingxing business data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to inspect Lingxing action schemas and run Lingxing connector actions for products, listings, sellers, marketplaces, inventory, shipments, currencies, profitability data, advertising reports, keyword metrics, rankings, and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include unverified remote installer scripts that could execute arbitrary code.

Mitigation: Use a verified, pinned, or package-manager installation method for the oo CLI instead of running curl|bash or irm|iex blindly.

Risk: The connector can access Lingxing business data through an OOMOL-connected account.

Mitigation: Install and use the skill only when the OOMOL connector path is trusted and the account grants appropriate Lingxing data access.

Risk: Write-tagged actions can change Lingxing state.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect before executing any write-tagged action.

## Reference(s):

- [Lingxing ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lingxing)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Lingxing homepage](https://www.lingxing.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when the documented oo CLI commands are run.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
