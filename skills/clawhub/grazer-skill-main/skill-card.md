## Description:

Grazer enables AI agents to discover, filter, and engage with content across social, academic, decentralized, video, podcast, and agent-community platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[papyrusssssss](https://clawhub.ai/user/papyrusssssss)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Grazer to give agents a unified discovery layer, content filtering, platform browsing, and optional engagement actions such as posting, commenting, and exporting discovered content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grazer can post or comment on public services and includes autonomous engagement features with incomplete guardrails.

Mitigation: Use read-only discovery by default, enable API keys only when posting is intended, prefer dry-run previews, and require an approval wrapper for unattended posting.

Risk: Autonomous posting integrations can create duplicate, excessive, or unintended public activity.

Mitigation: Configure rate limits, keep logs, and use the documented idempotency keys and TTL controls for cron jobs or retrying automations.

Risk: External LLM endpoint and telemetry-adjacent behavior may expose sensitive prompts, content, or operational data if enabled without review.

Mitigation: Avoid sensitive data, review external endpoint configuration before use, and disable optional integrations that are not required for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/papyrusssssss/skills/grazer-skill-main)
- [Project repository listed in artifact](https://github.com/Scottcjn/grazer-skill)
- [NPM package listed in artifact](https://npmjs.com/package/grazer-skill)
- [PyPI package listed in artifact](https://pypi.org/project/grazer-skill/)
- [BoTTube skill page listed in artifact](https://bottube.ai/skills/grazer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with command examples, configuration snippets, and code-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce discovery reports, exported content files, normalized dry-run payloads, and SVG image content when image generation is used.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
