## Description:

Analyzes Douyin comments and replies to summarize audience feedback, sentiment themes, objections, pain points, FAQs, and discussion topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and creators use this skill to review comments and replies on selected Douyin posts, identify audience feedback themes, and summarize sentiment, objections, pain points, and FAQs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Comment collection can incur service charges.

Mitigation: Use page or item limits for selected posts and check the account's billing status before expanding collection.

Risk: Direct CLI requests use an API key.

Mitigation: Keep the key in supported secret storage or an untracked local settings file, and keep it out of chat and logs.

Risk: The behavior of the external CLI package is not independently verified in the supplied security evidence.

Mitigation: Review and pin a package version, and provide it only the credentials it needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)
- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON comment data with concise summaries of observed themes and sentiment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports page or item limits and pagination; multi-page results include page and item counts.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
