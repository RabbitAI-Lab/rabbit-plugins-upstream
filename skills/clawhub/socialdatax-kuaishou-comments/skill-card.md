## Description:

Helps analyze Kuaishou video comments and replies for audience feedback, sentiment themes, questions, and pain points using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content analysts, marketers, and developers use this skill to retrieve Kuaishou comments and replies and summarize audience themes, objections, and frequently asked questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm package at runtime introduces supply-chain risk.

Mitigation: Trust the publisher and package before installation; pin an exact reviewed package version or use a locked installation path.

Risk: Unbounded comment pagination can consume more API credits than intended.

Mitigation: Set page or item limits and review the remaining budget before fetching additional pages.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-comments)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands]

**Output Format:** [JSON comment data or Markdown analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pagination can return partial results; report coverage and preserve collected comments.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
