## Description:

ExportDou helps agents export public Douyin video comments and optional replies to CSV or Excel, inspect video metadata and comment counts, preview samples, and manage resumable asynchronous export tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenny-shaw](https://clawhub.ai/user/kenny-shaw)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill to collect public Douyin video comments for user feedback, public opinion, content planning, and market analysis. It supports controlled exports, previews, downloads, credit checks, and recovery of partial asynchronous tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses ExportDou as a third-party service for public Douyin comment exports, including account login, credit usage, and npm CLI execution through npx.

Mitigation: Confirm the user is comfortable with the third-party service, authenticate through the approved ExportDou flow, and check credits before large exports.

Risk: Credentials, signed download URLs, provider responses, or internal cursors could be exposed while troubleshooting or handling task output.

Mitigation: Keep stderr separate from structured stdout and do not reveal API keys, signed URLs, raw provider responses, or internal cursors.

Risk: Requests for private, deleted, login-gated, region-restricted, or access-controlled content may fail or exceed the intended public-data scope.

Mitigation: Use only user-supplied public Douyin links or share text, and ask for another public link when content is unavailable.

Risk: Large or reply-inclusive exports can consume credits or hit row and task limits.

Mitigation: Use explicit row limits for replies and large exports, avoid combining all-comments mode with replies, and resume eligible partial tasks instead of creating replacements.

## Reference(s):

- [ExportDou Website](https://exportdou.cn)
- [ExportDou API Docs](https://exportdou.cn/developers)
- [ExportDou CLI Guide](https://exportdou.cn/developers#agent)
- [Command Reference](references/commands.md)
- [Error Handling Reference](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces export task IDs, small normalized previews, and downloaded CSV or XLSX files when the user requests complete results.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
