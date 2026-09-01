## Description:

post2all helps OpenClaw agents create, validate, draft, schedule, publish, update, cancel, and manage platform-specific social posts across connected post2all accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[post2all](https://clawhub.ai/user/post2all)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare review-first social publishing workflows through post2all, including platform-specific drafts, media handoff, scheduling, and approved publication across connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create public social publishing side effects when used with connected accounts.

Mitigation: Keep draft-first behavior as the default, and require explicit approval of destinations, content, media, and timing before scheduling or publishing.

Risk: API keys or account credentials could be exposed through prompts, logs, screenshots, or committed files.

Mitigation: Use local CLI configuration or the hosted OAuth MCP flow, and do not print, repeat, log, or commit post2all API keys.

Risk: Destructive actions such as cancellation, record deletion, or live social deletion can affect existing posts.

Mitigation: Inspect the post and exact affected account or target before destructive actions, confirm the user's intent, and distinguish deleting a post2all record from deleting live social content.

Risk: Platform rules, account options, privacy values, media support, and destination-specific settings can change.

Mitigation: Refresh current account capabilities and publishing options before validation, scheduling, publishing, or platform-specific configuration.

Risk: Blind retries after failed publishing mutations can create duplicates or obscure partial changes.

Mitigation: Inspect the returned error and post state before retrying, reuse or update existing posts when appropriate, and pause on rate limits or permission restrictions.

## Reference(s):

- [post2all setup for OpenClaw](references/setup.md)
- [Publishing boundaries and safety](references/safety.md)
- [post2all OpenClaw workflows](references/workflows.md)
- [post2all OpenClaw setup](https://www.post2all.com/openclaw)
- [post2all MCP documentation](https://www.post2all.com/docs/mcp)
- [post2all API reference](https://www.post2all.com/docs/api-reference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Real account actions depend on connected post2all accounts, credentials, platform capabilities, workspace permissions, and user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
