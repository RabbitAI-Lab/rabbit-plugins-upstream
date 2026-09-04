## Description:

Operate the Message-in-a-Bottle (MIAB) LIFO callback stack, a local asynchronous callback broker that lets agents delegate work, yield, and resume when results return.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albzhu](https://clawhub.ai/user/albzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to register wake paths, create and forward callback bottles, return or resolve delegated work, inspect active callback state, and reap stale local callback envelopes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broker is designed for a single-user trust boundary and assumes local agents with access to CLAW_HOME are trusted.

Mitigation: Install only on a single-user machine with trusted local agents and keep CLAW_HOME private.

Risk: Callback task, result, and resume text is persisted locally and may be copied into dispatch messages.

Mitigation: Do not place secrets in callback task, result, summary, or resume fields; reference locations instead of secret values when needed.

Risk: The stale callback reaper can fail and purge pending callback envelopes when the global TTL is too short for the workload.

Mitigation: Measure the workload and run the reaper in dry-run mode before enabling purging.

## Reference(s):

- [ClawHub miab-broker listing](https://clawhub.ai/albzhu/skills/miab-broker)
- [SKILL.md](artifact/SKILL.md)
- [SECURITY.md](artifact/SECURITY.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local command guidance for callback lifecycle operations; no network output is declared by the artifact.]

## Skill Version(s):

2.0.0 (source: server release evidence, CHANGELOG.md, and claw-callback.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
