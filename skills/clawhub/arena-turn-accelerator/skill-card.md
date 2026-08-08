## Description:

Fixes agent-chat lag, stale answers after reconnect, late-conversation degradation, needless CAPTCHA false positives, sycophantic capitulation on true claims, and true claims delivered in a self-pitying or ill-timed voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to reduce turn latency, reject stale in-flight responses, monitor long-conversation degradation, triage verification false positives, and keep agent responses anchored to evidence under pushback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can shape agent behavior around truth-holding, tone, and creative invention, which may affect sensitive or high-stakes interactions.

Mitigation: Treat behavioral outputs as reviewable guidance rather than automatic authority, especially in sensitive contexts.

Risk: The skill may store local state under ~/.arena_turn, including prompt previews or derived local results.

Mitigation: Inspect local state and logs, protect any supplied inputs they contain, and run with least-privilege filesystem access.

Risk: The self-test can delete ~/.arena_turn state.

Mitigation: Run scripts/selftest.sh only with an isolated HOME or after backing up any needed ~/.arena_turn state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-turn-accelerator)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and local script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce JSON or status output from local Python utilities; some utilities may write local state under ~/.arena_turn.]

## Skill Version(s):

1.4.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
