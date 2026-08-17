## Description:

Generate and edit images and videos with Grok Imagine through RunAPI. Use when the user asks an agent to create, edit, animate, or transform media with Grok Imagine. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate, edit, animate, or transform images and videos with Grok Imagine through RunAPI. It supports one-off CLI execution and SDK-based application or backend integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to RunAPI/Grok Imagine and may include sensitive or proprietary content.

Mitigation: Use only media intended for upload, review requests before submission, and prefer a dedicated API key where possible.

Risk: Using the skill may consume paid API credits.

Mitigation: Authenticate before execution, submit each paid task once, preserve task evidence, and avoid replacement submissions without user authorization.

Risk: A stale CLI or API contract can lead to invalid requests or incomplete deliverables.

Mitigation: Discover the current CLI and API contracts, stop on contract mismatches, and verify every requested media file is non-empty with the expected MIME type.

## Reference(s):

- [RunAPI Grok Imagine homepage](https://runapi.ai/models/grok-imagine)
- [Model overview, pricing, and rate limits](https://runapi.ai/models/grok-imagine.md)
- [Provider overview](https://runapi.ai/providers/xai.md)
- [Full model catalog](https://runapi.ai/models.md)
- [SDK integration](https://github.com/runapi-ai/grok-imagine-sdk)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-grok-imagine)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands, JSON request and response files, and optional SDK code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce request.json, task.json, result.json, downloaded image or video files, and SDK integration snippets.]

## Skill Version(s):

0.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
