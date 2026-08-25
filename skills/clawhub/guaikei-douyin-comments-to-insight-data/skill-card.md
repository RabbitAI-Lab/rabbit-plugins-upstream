## Description:

This skill retrieves public Douyin search results, creator posts, video comments, and trending topics as structured insight data for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, marketers, and developers use this skill to gather structured Douyin public data for content ideation, competitor monitoring, comment sentiment review, and trend tracking. It is not intended for publishing, editing, downloading, or private-data access workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route Douyin research requests to the external guaikei.com service.

Mitigation: Use it only when the user explicitly wants Douyin public-data collection, and avoid confidential, regulated, or sensitive research terms.

Risk: Large result sets can be saved locally under logs and may include comments, user identifiers, account URLs, or business research terms.

Mitigation: Protect, review, or delete generated log files when they contain personal identifiers, sensitive topics, or business-confidential analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-comments-to-insight-data)
- [User documentation](readme.md)
- [CLI options](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei token and service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with Node.js shell commands; command stdout is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command results may be saved under logs.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
