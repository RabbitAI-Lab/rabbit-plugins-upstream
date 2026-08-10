## Description:

SocialDataX Weibo Search helps agents analyze Weibo hot-search lists and posts for keyword discovery, content research, competitor analysis, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research teams use this skill to query SocialDataX-backed Weibo hot-search and post data, then summarize observed rankings, post metadata, interaction signals, and traceable URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API-authenticated Weibo research queries are sent to SocialDataX.

Mitigation: Use this skill only for queries acceptable to send to SocialDataX, keep SOCIALDATAX_API_KEY in the environment, and avoid placing secrets in prompts or files.

Risk: The examples run a Node/npm CLI package and use the latest package version.

Mitigation: Run commands in a trusted environment, review command arguments before execution, and pin the package version if your deployment policy requires reproducible tooling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Markdown, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Weibo research workflow that requires SOCIALDATAX_API_KEY and Node/npm for CLI use.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
