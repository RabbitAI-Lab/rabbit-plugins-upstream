## Description:

This skill helps agents research Zhihu hot lists, content, comments, creator profiles, and article lists through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Zhihu readers and researchers can use the skill to review hot lists, search and inspect content, analyze comments, and look up creator profiles and article lists. It retrieves this information through SocialDataX for read-only research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research inputs are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Avoid confidential search terms or share text, and check applicable credit usage before querying.

Risk: An exposed API key or unreviewed downloaded CLI release could put account access or local data at risk.

Mitigation: Keep SOCIALDATAX_API_KEY in the execution environment's secret store and out of chat and version control; use a reviewed fixed CLI version with limited access to local files and unrelated secrets.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-zhihu)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured Zhihu research data and concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; API requests may consume paid credits.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
