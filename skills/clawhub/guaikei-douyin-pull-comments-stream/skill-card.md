## Description:

Collects public Douyin search results, creator posts, video comments, and trending-list data through Node.js CLI commands and returns structured JSON for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content teams use this skill to research public Douyin content, monitor creator activity, inspect comment sentiment, and follow real-time trends. It is not intended for publishing, editing, downloading videos, or accessing private Douyin data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, video or account URLs, and the configured API token are sent to GuaiKei.

Mitigation: Install and run the skill only when this data sharing is acceptable for the intended workflow.

Risk: Collected Douyin results are saved locally under logs/ by default and may include sensitive topics, comments, or user data.

Mitigation: Review and periodically delete logs, especially after research involving sensitive topics or identifiable user data.

Risk: The skill can trigger on vague short-video research requests, which may collect Douyin data when the user did not explicitly name Douyin.

Mitigation: Use it for explicit Douyin research requests, or confirm intent before running the CLI for ambiguous requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-pull-comments-stream)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Usage Documentation](readme.md)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [GuaiKei Token and Support Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline bash commands; CLI stdout is structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes collected results to logs/ by default.]

## Skill Version(s):

1.0.0 (source: release metadata, SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
