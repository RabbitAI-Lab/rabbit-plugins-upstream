## Description:

Searches public Douyin content by keyword, retrieves creator posts and video comments, and checks trending lists for short-video monitoring, competitor analysis, and reputation tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect and summarize public Douyin search results, creator posts, comments, and trending-list data for content planning, competitive analysis, reputation monitoring, and public-opinion tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collected Douyin searches, monitored accounts, comments, and generated logs may reveal sensitive business interests or personal data.

Mitigation: Run the skill only in trusted workspaces, limit collection to data needed for the task, protect generated logs, and delete stored datasets when they are no longer required.

Risk: Token-error behavior may display provider contact or promotional information despite the documentation's neutral-error claim.

Mitigation: Review stderr and user-facing error handling before deployment, and avoid exposing raw runtime errors directly to end users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-recon)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [User documentation](readme.md)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command stdout is intended to be parseable JSON; runtime logs and prompts are sent separately, and collected datasets may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
