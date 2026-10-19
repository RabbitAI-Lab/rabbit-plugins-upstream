## Description:

Helps agents search Xiaohongshu notes through SocialDataX for topic discovery, content research, competitor analysis, and trend research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and content teams use this skill to search Xiaohongshu notes and summarize content themes, audience reactions, competitor positioning, and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runtime npm package can change between uses and has access to the user's SocialDataX API key.

Mitigation: Use a trusted, reviewed pinned package version or a vetted preinstalled CLI before sharing the API key.

Risk: Page limits or interrupted searches can leave research results incomplete.

Mitigation: Identify partial results and page limits; resume from the returned pagination token using the remaining limits.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown research summaries with source links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings reflect retrieved pages, not complete platform coverage.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
