## Description:

Helps agents research Bilibili videos, articles, comments, reactions, and creators, with optional video downloads on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search and analyze Bilibili content, discussions, reactions, and creator activity through SocialDataX. They can save a video locally when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested commands run the latest, unpinned socialdatax-skills package while the user's API key is available.

Mitigation: Review and pin a trusted package version before execution, and protect SOCIALDATAX_API_KEY.

Risk: The optional video download writes files to a local directory.

Mitigation: Download only when explicitly requested, and restrict output to an intended directory.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [B站数据助手 SocialDataX on ClawHub](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Text or Markdown guidance and CLI responses; optional downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Data access requires a SocialDataX API key; local video downloads require an explicit request.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
