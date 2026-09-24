## Description:

Type with your voice using Yaps on desktop. Get set up, fix a problem, or recover a recent dictation. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to operate Yaps desktop dictation from an agent session, check setup readiness, troubleshoot voice typing, and recover recent dictation text when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a broad local Yaps CLI wrapper beyond simple voice typing.

Mitigation: Use it only for explicit Yaps dictation, transcription, setup, or recovery tasks, and review commands that touch history, media files, output paths, jobs, or batch processing.

Risk: Local CLI operations may interact with account state, desktop permissions, and local files.

Mitigation: Do not approve Keychain prompts, do not use the CLI to bypass denied Yaps or MCP access, and confirm microphone, accessibility, download, and file-output actions before proceeding.

## Reference(s):

- [Runtime guide](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce transcript text, subtitle files, meeting metadata, setup diagnostics, and local Yaps CLI command guidance.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
