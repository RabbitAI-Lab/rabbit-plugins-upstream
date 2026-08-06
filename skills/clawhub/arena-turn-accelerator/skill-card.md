## Description:

Arena Turn Accelerator helps agents reduce turn latency, discard stale responses, monitor long-context degradation, triage human-verification false positives, and apply evidence-based anti-sycophancy response checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to preflight web-agent turns, compact prompts, fence request lifecycles, monitor context health, triage repeat CAPTCHA triggers, and shape responses that hold evidence-backed claims without hostile delivery. It is intended for local agent-side and client-side workflow assistance, not server-side performance fixes or CAPTCHA bypass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist prompt previews and conversation metadata under ~/.arena_turn.

Mitigation: Use it only where local prompt and conversation metadata storage is acceptable, and periodically review or clear that directory.

Risk: The self-test can delete ~/.arena_turn state.

Mitigation: Run scripts/selftest.sh only in an isolated profile or after backing up any state you need to keep.

Risk: The response-shaping modules are opinionated and may add firm anti-sycophancy guidance or unsolicited creative extensions.

Mitigation: Review quarry, register, and spine behavior before enabling the skill in workflows where strict response style or minimal intervention is required.

Risk: The verification triage workflow could be misunderstood as a CAPTCHA bypass.

Mitigation: Use it only to diagnose and reduce false-positive human-verification triggers; do not use it to evade or spoof verification systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/arena-turn-accelerator)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [plugin.json](artifact/plugin.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus text, JSON, and local-state outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local state under ~/.arena_turn; self-tests may delete that local state.]

## Skill Version(s):

1.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
