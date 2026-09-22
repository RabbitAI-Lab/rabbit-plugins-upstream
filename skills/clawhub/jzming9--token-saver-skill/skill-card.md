## Description:

Smart token cost optimization for OpenClaw that reduces AI token consumption through context compression, semantic caching, and adaptive optimization while preserving response quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jzming9](https://clawhub.ai/user/jzming9)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to monitor token usage, compress long conversation context, manage token-saving modes, and review savings reports during extended AI sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may transform and cache conversation content, including sensitive context.

Mitigation: Avoid using it with secrets or confidential conversations unless cache scope, retention, and clearing behavior are acceptable.

Risk: The core optimizer dependency is not present or pinned in the artifact.

Mitigation: Use a pinned installer and review a locked @token-saver/core version before deploying in sensitive workspaces.

Risk: Server security evidence marks the release as suspicious because cache retention and installation provenance are unclear.

Mitigation: Review the skill before installation in sensitive workspaces and prefer deployment only after provenance and dependency controls are confirmed.

## Reference(s):

- [Token Saver Skill on ClawHub](https://clawhub.ai/jzming9/skills/token-saver-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with slash commands, status reports, configuration examples, and optimization guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize or transform conversation context and report estimated token savings.]

## Skill Version(s):

1.0.2 (source: server release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
