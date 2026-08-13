## Description:

RelayAPI lets agents post to 22 social and messaging platforms through a unified API while managing accounts, workspaces, media, scheduling, analytics, inbox activity, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zanhk](https://clawhub.ai/user/zanhk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and social media teams use this skill to have an agent prepare RelayAPI requests for publishing, scheduling, account management, analytics, inbox moderation, media uploads, and webhook setup across connected platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable broad changes to connected social-media accounts, including publishing, deletion, account connection, moderation, workspace changes, direct messages, replies, and webhook creation.

Mitigation: Require explicit user confirmation before any publishing, bulk posting, local file upload, account connection or disconnection, content deletion or unpublishing, workspace or queue change, DM or reply, or webhook creation.

Risk: The skill depends on a RelayAPI API key that can authorize actions against connected accounts.

Mitigation: Use a limited API key where possible, store RELAYAPI_API_KEY in OpenClaw secrets, and do not ask users to paste the key into chat.

Risk: Immediate publishing is asynchronous and may result in partial or failed delivery across target platforms.

Mitigation: Check post status after creation or use webhooks to confirm final delivery state before treating a publish request as complete.

## Reference(s):

- [RelayAPI Homepage](https://relayapi.dev)
- [RelayAPI API Docs](https://api.relayapi.dev/docs)
- [RelayAPI OpenAPI Spec](https://api.relayapi.dev/openapi.json)
- [RelayAPI ClawHub Skill Listing](https://clawhub.ai/zanhk/skills/relayapi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API call guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RELAYAPI_API_KEY and curl; API responses are returned by RelayAPI.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
