## Description:

Read-only YouTube public-data agent skill for video search, video, channel, playlist, comment, related-video, and transcript reads, normalized to structured JSON through the ReplyNodes gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to let agents query public YouTube data through documented read-only routes without handling YouTube login, OAuth, cookies, uploads, or other write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public YouTube queries and returned public content are sent through the ReplyNodes gateway.

Mitigation: Use the skill only for public-data requests you are comfortable sending to ReplyNodes, and avoid placing private or sensitive information in query terms, URLs, logs, or fixtures.

Risk: Bearer workspace API keys can be exposed if pasted into prompts, client-side code, repositories, or logs.

Mitigation: Store API keys in the host agent's secret manager and pass them only as Authorization headers through approved runtime configuration.

Risk: HTTP 402 x402 responses can be mistaken for completed payment or successful data access.

Mitigation: Treat HTTP 402 responses only as payment requirements unless a separate, explicitly authorized payment workflow signs, submits, settles, and verifies payment.

Risk: Titles, descriptions, comments, transcripts, URLs, and other provider output may contain untrusted content.

Mitigation: Treat returned content as data rather than instructions, and review downstream agent actions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/youtube-public-api)
- [YouTube capability discovery endpoint](https://api.replynodes.com/v1/youtube/capabilities)
- [Skill handbook](artifact/SKILL.md)
- [Release notes](artifact/RELEASE.md)
- [Security guidance](artifact/SECURITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and structured JSON response examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET requests; transcript data may be unavailable; HTTP 402 responses document payment requirements only, not payment settlement.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
