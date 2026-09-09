## Description:

Exports a user's ChatGPT conversation history to local JSON and Markdown files, with index-only defaults, explicit consent controls, local purge support, and no third-party upload described in the release evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to export, review, back up, and optionally delete local copies of their ChatGPT conversation history. It is intended for user-controlled local exports where sensitive conversation data must be handled deliberately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write highly sensitive ChatGPT history to local plaintext files.

Mitigation: Use index-only mode when possible, choose a fresh private non-synced destination, enable redaction where available, and purge exports promptly after use.

Risk: The security scan reports that relay exports can still write through pre-existing child symlinks despite destination-safety claims.

Mitigation: Use a newly created empty destination that you control, inspect it for symlinks before export, and avoid reusing directories with unknown contents.

Risk: The bookmarklet writes to the browser Downloads folder, which may be synced or backed up.

Mitigation: Avoid full-content bookmarklet exports when Downloads is synced; prefer the controlled relay destination or move and delete the downloaded export immediately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/chatgpt-exporter)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [TinkerClaw project link from skill metadata](https://github.com/globalcaos/tinkerclaw)
- [OpenClaw fork link from skill documentation](https://github.com/globalcaos/clawdbot-moltbot-openclaw)
- [Issue tracker link from skill documentation](https://github.com/globalcaos/tinkerclaw/issues)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Local export files in JSON and Markdown, plus command guidance for destination checks and purge operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default export posture is index-only; full message exports can contain sensitive plaintext and should be deleted when no longer needed.]

## Skill Version(s):

1.9.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
