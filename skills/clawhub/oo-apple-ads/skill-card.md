## Description:

Use this skill for Apple Ads requests involving reading, creating, updating, and deleting campaign, ad group, ad, keyword, budget, asset, and reporting data through the OOMOL Apple Ads connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and advertising operators use this skill to inspect Apple Ads account data, run performance reports, and manage campaign structures, ads, keywords, budgets, recommendations, and related Apple Maps or App Store advertising records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and modify Apple Ads accounts, including campaigns, budgets, bids, ads, and related records.

Mitigation: Use only with Apple Ads accounts where this level of agent access is acceptable, and require explicit user confirmation before write, destructive, recommendation apply, or recommendation dismiss actions.

Risk: The setup instructions include curl-to-bash and irm-to-iex installer commands.

Mitigation: Install the oo CLI through a safer verified channel instead of running remote installer scripts blindly.

Risk: Some recommendation actions may cause financially meaningful advertising changes without being tagged as writes in the artifact.

Mitigation: Treat apply and dismiss recommendation actions as change operations and confirm the exact payload and expected effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-apple-ads)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Apple Ads](https://ads.apple.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Apple Ads Icon](https://static.oomol.com/logo/third-party/apple_ads.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution and returns connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
