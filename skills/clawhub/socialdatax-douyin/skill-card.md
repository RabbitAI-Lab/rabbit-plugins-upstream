## Description:

Provides a Douyin data assistant for hot searches, content search and details, share links, comment and reply analysis, creator profiles, creator works, and creator short-drama or collection data via SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, researchers, and developers use this skill to ask an agent for Douyin content research, hot-search lookup, post details, comment and reply analysis, creator lookup, creator posts, and creator series data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the current npm release of socialdatax-skills with access to SOCIALDATAX_API_KEY.

Mitigation: Prefer a pinned, reviewed package version or run it in a constrained execution environment that exposes only the needed API key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)
- [SocialDataX API Access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm or npx, and SOCIALDATAX_API_KEY; runtime data access is described as read-only.]

## Skill Version(s):

0.1.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
