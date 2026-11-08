## Description:

openInvest helps agents review multi-asset portfolios and market data, record investment activity, and prepare a four-role committee analysis for selected assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longsizhuo](https://clawhub.ai/user/longsizhuo)

### License/Terms of Use:

MIT-0

## Use Case:

External users use the skill to review multi-asset portfolios and market data, record investment activity, and request committee analysis for selected assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review classifies this release as suspicious, citing live brokerage trading beyond the stated scope and privacy and supply-chain concerns; the review is incomplete.

Mitigation: Treat as review-required before installation. Consider whether live brokerage capabilities are needed, confirm that any financial information sent to external models is disclosed and approved, and account for the partial scan coverage.

## Reference(s):

- [openInvest on ClawHub](https://clawhub.ai/longsizhuo/skills/openinvest)
- [Project wiki](https://github.com/longsizhuo/openInvest/tree/main/docs/wiki)
- [Tool and subcommand reference](references/tools.md)
- [Committee protocol](references/committee-protocol.md)
- [Coordinator and Direct paths](references/two-paths.md)
- [Adding tracked assets](references/adding-assets.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Portfolio and market analysis or committee verdicts in Markdown; structured JSON for Direct-path committee results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available market data, configured services, and the selected model provider.]

## Skill Version(s):

0.34.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
