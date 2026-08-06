## Description:

Helps agents use SocialDataX to research public Kuaishou/Kwai content, videos, comments, replies, creator profiles, and creator posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other external users use this skill to fetch and review public Kuaishou/Kwai social-media data through SocialDataX for content research, comment analysis, and creator research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends query parameters and SOCIALDATAX_API_KEY to the SocialDataX service when fetching Kuaishou data.

Mitigation: Use only an intended SocialDataX account key and review SocialDataX account, billing, and data-use terms before running data fetches.

Risk: Broad fetch options such as all comments or all user posts may increase data volume, cost, or exposure of returned public social-media data.

Mitigation: Start with narrow queries, avoid repeated retries on insufficient-balance errors, and broaden collection only when the user has confirmed scope and account readiness.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and SocialDataX API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data retrieval; requires node, npm, and SOCIALDATAX_API_KEY.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
