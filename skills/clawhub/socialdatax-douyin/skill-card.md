## Description:

Search Douyin trends and content, inspect videos and comments, and look up creator profiles, posts, and series with SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Douyin trends, videos, comments, and creators can use this skill to retrieve read-only platform data through SocialDataX. It supports searches, content details and share links, comment and reply analysis, creator profiles, creator posts, and series.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions invoke an unpinned npm package, which can change between uses.

Mitigation: Pin and review the package version before use.

Risk: Search terms and URLs may be sent to SocialDataX for data lookup.

Mitigation: Avoid sensitive search terms and URLs, and review the provider's data handling before use.

Risk: The security scan was partial, so its evidence is incomplete.

Mitigation: Review and scan the skill before deployment.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Pretty-printed JSON results with textual summaries when presented by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookup results; list queries may be paginated.]

## Skill Version(s):

0.1.24 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
