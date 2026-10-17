## Description:

帮助用户检索招投标公告、评估投标机会、发掘采购商机，并调查企业的招投标记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and sales teams use this skill to search public tender data, assess whether to bid, identify upcoming opportunities, and review customers, suppliers, or competitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API-key setup or consent-based registration may expose account credentials or device information.

Mitigation: Obtain consent before registration, restrict access to the local API-key configuration, and never include the key in shared outputs.

Risk: Data queries may consume account credits.

Mitigation: Check the available balance and expected credit costs before extensive queries; avoid unnecessary retries.

Risk: Generated reports or chat messages may contain signed links that allow recipients to open pages without logging in.

Mitigation: Treat reports and signed links as sensitive; review recipients before sharing and remove access-granting links where unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/zlbx-ai-platform)
- [Tender search guide](artifact/references/tender-search/overview.md)
- [Bid decision guide](artifact/references/bid-decision/overview.md)
- [Opportunity radar guide](artifact/references/opportunity-radar/overview.md)
- [Company intelligence guide](artifact/references/company-intel/overview.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML reports]

**Output Format:** [Conversational answers and structured Markdown or HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include source links and credit usage.]

## Skill Version(s):

1.1.5 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
