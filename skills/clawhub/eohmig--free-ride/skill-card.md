## Description:

Manages free AI models for OpenClaw by ranking options, configuring fallbacks, and updating its model configuration; Groq, Gemini, and Cerebras support is opt-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use FreeRide to choose free models, configure fallback options for rate limits, and recover service when a model is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because it may replace a user-selected free model when ownership state is missing or unreadable; the scan is partial.

Mitigation: Review the current primary model and FreeRide ownership state before enabling automatic changes; confirm proposed changes manually if state is unavailable.

Risk: The optional background watcher persistently checks model availability and can rotate configuration, while the skill uses file, network, and shell access.

Mitigation: Review those accesses before installation and enable the watcher only if automatic recovery is wanted; a one-shot check is available.

## Reference(s):

- [FreeRide ClawHub release](https://clawhub.ai/eohmig/skills/free-ride)
- [FreeRide project homepage](https://github.com/Shaivpidadi/FreeRide)
- [OpenRouter API keys](https://openrouter.ai/keys)
- [OpenClaw](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Status text]

**Output Format:** [Updated OpenClaw JSON configuration and command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update model and fallback settings in OpenClaw configuration and save a backup before writing.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
