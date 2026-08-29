## Description:

Ingests live edge-device audio into per-device streaming memory so agents can recall what a device heard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to connect edge-device audio streams to BlueColumn-backed ingestion and per-device recall workflows. It supports audio chunk submission, idempotent retries, streamed query responses, and session-summary retrieval for long-horizon context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambient or bystander audio may be captured or processed without adequate consent, retention, deletion, or redaction controls.

Mitigation: Install only for authorized devices and environments, and confirm consent obligations, retention/deletion behavior, access controls, and redaction needs before use.

Risk: Audio is sent to BlueColumn/Groq-backed processing, which may be unsuitable for sensitive environments without prior approval.

Mitigation: Review data handling requirements and limit use to approved audio sources, API keys, and processing environments.

Risk: Per-device audio recall can expose sensitive historical observations from a device namespace.

Mitigation: Restrict API keys and namespace access to approved users and devices, and review recalled content before relying on it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/streaming-audio-memory)
- [BlueColumn Streaming Audio API Base URL](https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SSE event expectations for streamed recall responses.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
