## Description:

Search Douyin public videos, creator profiles, posts, comments, and trending lists, and return structured JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and data teams can search public Douyin videos and creators, inspect posts and comments, and track trending topics. They can use the structured results for topic research, competitor monitoring, and sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied links or IDs are sent to a third-party service when the skill is used.

Mitigation: Submit only public links or IDs you are comfortable sharing with that service.

Risk: The security analysis was partial and notes undeclared capabilities, so its benign verdict is not a guarantee of safety.

Mitigation: Review the requested search and post-detail features and the skill behavior before installation.

## Reference(s):

- [Usage and environment FAQ](artifact/references/faq.md)
- [Command options](artifact/references/options.md)
- [Output contract](artifact/references/contract.md)
- [Error handling guidance](artifact/references/errors.md)
- [Demand mining guidance](artifact/references/demand-mining.md)
- [Customer acquisition guidance](artifact/references/customer-acquisition.md)
- [Service and token setup](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON result envelopes containing public Douyin content and engagement data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, profile, post, detail, comment, and trending results; query results are also saved under logs/ except trending results.]

## Skill Version(s):

1.5.0 (source: server-resolved release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
