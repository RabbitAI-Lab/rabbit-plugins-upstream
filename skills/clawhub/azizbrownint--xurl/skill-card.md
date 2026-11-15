## Description:

xurl CLI for authenticated X posts, replies, reads/search, DMs, media upload, followers, auth status, or raw v2 API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate the xurl CLI for authenticated X API workflows, including reading posts, posting or replying, direct messages, media upload, follower actions, authentication checks, and raw v2 API requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform public or account-changing X actions, including posts, deletes, DMs, follow, block, mute, media upload, and auth app removal.

Mitigation: Require explicit user confirmation before executing account-changing commands and review the target account, endpoint, method, and payload.

Risk: Raw authenticated API requests can reach endpoints beyond the documented shortcuts.

Mitigation: Prefer read-only commands and require confirmation for raw non-GET requests before execution.

Risk: Credential exposure is possible if secrets are inspected, pasted into chat, passed inline, or exposed through verbose output.

Mitigation: Do not read or display ~/.xurl, do not ask users to paste tokens, do not run auth commands with inline secrets, and avoid verbose mode in agent sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/xurl)
- [Publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API Calls]

**Output Format:** [Markdown with inline bash code blocks; xurl command results are JSON on stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may exit non-zero on API, authentication, network, rate-limit, or media-processing errors.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
