## Description:

OpenClaw Memory Distill helps agents turn conversation context into structured workspace memory files with semantic tiers, deduplication, sensitive-information skipping, and report-only scheduled runs unless unattended writing is explicitly enabled.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

External developers and OpenClaw users use this skill to distill long or recurring agent conversations into a root MEMORY.md file, daily memory logs, and a distillation configuration. It is intended for explicit memory-distillation requests and scheduled report generation, with file writes gated by confirmation or autoWrite configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plaintext memory files can retain sensitive or private conversation details.

Mitigation: Review proposed memory entries before confirming writes, skip secrets and private third-party information, and rely on the configured sensitive-pattern checks.

Risk: Scheduled unattended writes can update workspace memory without a live confirmation step.

Mitigation: Keep autoWrite disabled unless unattended updates are intended; when enabled, restrict writes to the documented memory paths and archive before overwriting MEMORY.md.

Risk: Stale or duplicated memory can mislead future agent sessions.

Mitigation: Use the skill's deduplication and periodic maintenance flow, and review generated daily logs before promoting information into long-term memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-memory-distill)
- [GitHub documentation](https://github.com/dtsola/xiaoyaoclaw-memory-distill)
- [XiaoyaoClaw guide](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [Related workspace initializer](https://github.com/dtsola/xiaoyaoclaw-workspace-initializer)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports plus workspace Markdown and JSON memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes are limited to declared workspace memory paths; scheduled runs report only unless autoWrite is enabled.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
