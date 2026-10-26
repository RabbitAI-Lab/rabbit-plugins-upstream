## Description:

Supports Kuaishou work research and keyword, content, competitor, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts use it to search Kuaishou short-form works by keyword and review visible content, author, and engagement details for content, competitor, and trend research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and may reveal confidential research details.

Mitigation: Avoid including confidential details in search terms.

Risk: API key exposure or unbounded searches can create credential or credit-use concerns.

Mitigation: Protect SOCIALDATAX_API_KEY and set page or item limits to control credit use.

Risk: An unreviewed CLI release may change behavior.

Mitigation: Consider pinning a reviewed CLI version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Natural-language summaries and structured JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include content IDs, share URLs, author details, interaction counts, and publish times when available.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
