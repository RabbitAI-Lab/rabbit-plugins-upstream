## Description:

Supports Instagram research with content search, post details, comment analysis, creator profiles, and creator post lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and researchers can use this skill to find Instagram content, inspect posts and discussions, and review creator profiles and post lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research inputs are sent to SocialDataX and may include sensitive share text.

Mitigation: Send only necessary public URLs or identifiers; exclude confidential share text.

Risk: Unbounded pagination can consume API credits.

Mitigation: Set page or item limits appropriate to the research task.

Risk: Using the @latest CLI package can introduce unreviewed changes.

Mitigation: Prefer a reviewed, fixed CLI version.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Instagram research data, JSON data, Text summaries]

**Output Format:** [Pretty-printed JSON data with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; pagination can be limited by page or item count.]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
