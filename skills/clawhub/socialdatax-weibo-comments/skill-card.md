## Description:

Analyzes Weibo post comments and replies to identify audience sentiment, recurring themes, objections, and pain points using SocialDataX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, marketers, and developers use this skill to retrieve Weibo comments and replies and summarize audience feedback, sentiment themes, and common questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the latest npm CLI grants mutable package code access to the SocialDataX API key.

Mitigation: Review and pin the package version or use a reviewed installed CLI; require approval before shell or network execution.

Risk: Unbounded comment pagination may consume more API credits than expected.

Mitigation: Set page or item limits before fetching large threads and confirm scope before using --all.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-comments)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown summaries; CLI data returned as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries should distinguish single-page from multi-page results and identify incomplete retrievals.]

## Skill Version(s):

0.1.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
