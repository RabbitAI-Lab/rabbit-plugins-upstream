## Description:

Helps procurement teams search tender notices, assess bids, discover opportunities, and research companies using procurement data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and sales teams use this skill to find Chinese tender opportunities, evaluate whether to bid, monitor prospective projects, and review customers, suppliers, and competitors through procurement records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shareable reports can retain signed links that grant access to linked content.

Mitigation: Treat reports and URLs containing sk as access-bearing; share only with intended recipients.

Risk: The skill can store an API key locally and leave generated reports on disk.

Mitigation: Prefer a managed ZLBX_API_KEY environment variable; clear ~/.zlbx/config.json and ~/zlbx-*-files report folders when no longer needed.

Risk: Using the skill sends procurement queries to zhiliaobiaoxun.com services.

Mitigation: Review the external API access and local report generation before installing or using the skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [Tender search guide](artifact/references/tender-search/overview.md)
- [Bid decision guide](artifact/references/bid-decision/overview.md)
- [Opportunity radar guide](artifact/references/opportunity-radar/overview.md)
- [Company intelligence guide](artifact/references/company-intel/overview.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML reports]

**Output Format:** [Conversational text and Markdown analyses; optional locally generated HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the ZLBX_API_KEY credential and metered procurement APIs; some shareable reports contain access-bearing signed links.]

## Skill Version(s):

1.1.3 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
