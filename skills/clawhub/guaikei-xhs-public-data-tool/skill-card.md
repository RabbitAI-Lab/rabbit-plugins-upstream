## Description:

Routes Xiaohongshu keywords and public links to CLI commands that retrieve search results, note details, creator posts, or comments as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, marketers, and analysts use this skill to collect public Xiaohongshu data for content research, competitive monitoring, KOL screening, and comment analysis. It requires an API token and should be used only for public data workflows authorized by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Xiaohongshu keywords or links, including URL query parameters, are sent to guaikei.com with the configured API token.

Mitigation: Use the skill only when the user is comfortable with that data transfer, and avoid submitting sensitive or unauthorized links.

Risk: Returned comments, profile data, and other results may be retained in local JSON logs.

Mitigation: Treat generated logs as retained business data, review them before sharing, and delete them when retention is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-public-data-tool)
- [Guaikei website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI execution returns structured JSON and can save JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; sends Xiaohongshu keywords or links to guaikei.com and may retain returned data in a local logs directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
