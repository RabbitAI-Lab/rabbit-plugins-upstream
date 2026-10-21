## Description:

Helps agents research Douyin hot searches, posts, comments, creators, and short-drama collections through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to retrieve and analyze Douyin trends, content, comments, and creator information through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs are sent to SocialDataX and consume the user's API credits.

Mitigation: Avoid sending sensitive share text and use sensible retrieval limits.

Risk: The external CLI and hosted backend are not included for inspection, and an unpinned latest CLI can change over time.

Mitigation: Prefer a reviewed, fixed CLI version and confirm the selected API calls before use.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Pretty-printed JSON lookup results and concise research guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Douyin research; results depend on SocialDataX service availability and API access.]

## Skill Version(s):

0.1.21 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
