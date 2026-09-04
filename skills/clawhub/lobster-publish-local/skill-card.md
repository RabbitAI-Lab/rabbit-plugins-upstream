## Description:

GEO内容发布助手 helps WorkBuddy users prepare, bind, and locally publish GEO-oriented articles, short posts, Q&A, and short videos to Chinese content platforms using the user's own browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qingmuhuijianghu](https://clawhub.ai/user/qingmuhuijianghu)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and WorkBuddy users use this skill to prepare platform-aware content, bind social publishing accounts, preview outputs, and publish or distribute content from their local environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent local browser-control agent can act on logged-in platform sessions and publish public content.

Mitigation: Use dedicated or limited-scope accounts where possible, confirm every publish action manually, and know how to stop the local agent before installation.

Risk: The skill requires an API key, invite code, platform login cookies, and selected local media access.

Mitigation: Keep credentials private, revoke or rotate exposed credentials, and only upload media intended for publication.

Risk: Broad automatic triggers and platform-control behavior can create unintended posts or platform policy issues.

Mitigation: Review generated content and destination platforms before publishing, and check each platform's current posting rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qingmuhuijianghu/skills/lobster-publish-local)
- [Publisher profile](https://clawhub.ai/user/qingmuhuijianghu)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and HTML content with inline shell commands, configuration values, and publishing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require user credentials, browser session access, and user confirmation before public publishing.]

## Skill Version(s):

2.31.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
