## Description:

Provides Xiaohongshu / XHS / RedNote note detail retrieval for data analysis, note metrics, content research, and content analysis using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to fetch structured Xiaohongshu / XHS / RedNote note details by note ID or note URL for content analysis and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SOCIALDATAX_API_KEY-backed requests to SocialDataX at runtime.

Mitigation: Install and use it only when the operator is comfortable providing that API key to SocialDataX.

Risk: Returned full XHS note URLs can include xsec_token query parameters and may be sensitive.

Mitigation: Share or store returned full note URLs only with intended recipients and treat them as potentially sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-detail)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON data returned by SocialDataX tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for detail requests; preserves full returned note URLs when present.]

## Skill Version(s):

0.1.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
