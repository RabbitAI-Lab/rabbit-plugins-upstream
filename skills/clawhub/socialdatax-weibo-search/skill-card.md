## Description:

Supports Weibo hot-search and post research for keyword discovery, content and competitor analysis, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social media researchers use the skill to review Weibo hot searches and search posts by keyword. It helps summarize observed ranking and content signals, with post details for traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and requests may consume account credits.

Mitigation: Use appropriate search terms and monitor credit usage.

Risk: An exposed API key could be used by others.

Mitigation: Keep the key in supported secret storage and out of chat and version control.

Risk: The supplied skill instructions do not establish the behavior of the downloaded npm package.

Mitigation: Prefer a reviewed, pinned CLI version and provide only the credentials it needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown research summaries with supporting post details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; summaries distinguish observed evidence from interpretation.]

## Skill Version(s):

0.1.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
