## Description:

Searches public Kuaishou videos, creator posts, and video comments, returning structured data for user feedback and consumer insight analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use this skill to find public videos, review creator activity, and summarize comment themes such as needs, concerns, and feedback. The results support content research, competitor analysis, product improvement, and customer service preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and Kuaishou links are sent to guaikei.com to retrieve data.

Mitigation: Use only queries and links appropriate to send to the service; do not submit confidential information.

Risk: The security assessment reports that 20 of 32 components were fully inspected, 12 were partially inspected, and a third-party data disclosure gap was identified.

Mitigation: Review the provider's data handling and the partially inspected components before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-comment-consumer-insights)
- [GuaiKei service and token access](https://www.guaikei.com)
- [Command options](artifact/references/options.md)
- [Output envelope schema](artifact/assets/output_envelope.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON results for video searches, creator posts, or comments, with text summaries derived from the returned data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public data only. Monthly token limits are 30 search results, 50 posts, and 60 comments; available counts depend on the token plan.]

## Skill Version(s):

1.1.2 (source: ClawHub release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
