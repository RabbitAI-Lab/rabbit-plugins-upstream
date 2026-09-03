## Description:

Inject current time and idle detection into every LLM turn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mfang0126](https://clawhub.ai/user/mfang0126)

### License/Terms of Use:

MIT

## Use Case:

Developers and Hermes Agent users use this skill to give agents compact current-time and idle-duration context for scheduling, reminders, time-sensitive decisions, and re-anchoring after user inactivity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Every Hermes model call receives a small time and idle-duration context block.

Mitigation: Install only when time and idle awareness are desired for Hermes conversations.

Risk: The installer writes under ~/.hermes/plugins and may enable the plugin automatically.

Mitigation: Review the installer before running it when cautious about scripts that modify local Hermes plugin state.

Risk: Python 3.9+ is effectively required by the implementation and doctor script, despite one artifact mentioning Python 3.8+.

Mitigation: Run the bundled doctor script and confirm the Python version before relying on the plugin.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mfang0126/skills/hermes-time-awareness)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and compact text context examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a small per-turn time and idle-duration context block for Hermes LLM calls.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
