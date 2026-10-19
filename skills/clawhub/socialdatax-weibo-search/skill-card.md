## Description:

Helps agents research Weibo hot searches and posts for keyword discovery, content analysis, competitor research, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this skill to examine Weibo hot searches and keyword-matched posts, summarize observed activity, and investigate content and competitor trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the latest npm package can execute code that has changed since review.

Mitigation: Review the package source and pin a vetted version before running it.

Risk: A compromised dependency could access the SocialDataX API key used for research.

Mitigation: Limit SOCIALDATAX_API_KEY access and balance to what the research task needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown research summaries and optional CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed results from interpretation and identifies incomplete paginated searches.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
