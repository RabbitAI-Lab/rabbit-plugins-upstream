## Description:

Captures smart-home automation conflicts, sensor drift, device connectivity failures, integration regressions, safety gaps, and energy optimization opportunities for continuous domotics improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and smart-home operators use this skill to capture domotics issues, learnings, and feature requests, then promote recurring patterns into safer automation playbooks, compatibility notes, rule libraries, or safety standards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks can persist across sessions and broad Bash output detection may trigger reminders from common smart-home terms.

Mitigation: Review hook setup before enabling it, keep hooks project-scoped, and enable Bash output detection only when reminder triggering on command output is desired.

Risk: Learning files may accidentally capture sensitive smart-home details such as lock codes, alarm codes, credentials, or private household schedules.

Mitigation: Keep secrets and private schedules out of logs; record only the minimum operational context needed to diagnose the issue.

Risk: Domotics recommendations can affect high-impact routines involving locks, alarms, gas or water shutoff, and heaters if later implemented without review.

Mitigation: Use human confirmation, conservative fallback states, and notify-only behavior for high-impact routines; keep this skill reminder-only and separate from actuator execution.

## Reference(s):

- [Domotics Entry Examples](artifact/references/examples.md)
- [Domotics Hook Setup Guide](artifact/references/hooks-setup.md)
- [OpenClaw Integration (Domotics)](artifact/references/openclaw-integration.md)
- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-house)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminder-only workflow; does not directly control physical devices.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
