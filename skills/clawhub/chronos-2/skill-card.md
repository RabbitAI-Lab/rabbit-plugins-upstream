## Description:

Gives AI coding agents temporal awareness via a hook-backed ledger and decision rules for recency, retry windows, memory staleness, deploy cooldowns, idle detection, and time-related questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Chronos to give AI coding agents concrete time-awareness rules, hook-backed session timing, and a local tool-use ledger so agents can make better decisions about retries, stale information, progress reporting, idle loops, and date or time questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent hooks run on routine session, prompt, tool-use, and stop events.

Mitigation: Prefer project-scoped installation where available and review generated hook commands before enabling them.

Risk: Local tool-use timing metadata is stored under ~/.chronos by default.

Mitigation: Keep installer backups, configure retention to match local policy, and remove local ledgers when they are no longer needed.

Risk: The Windows PowerShell bypass variant may conflict with strict script-execution policy.

Mitigation: Avoid the bypass variant in restricted environments and use the standard hook configuration where policy permits.

## Reference(s):

- [Chronos ClawHub Skill Page](https://clawhub.ai/othmanadi/skills/chronos-2)
- [Server-resolved GitHub Repository](https://github.com/OthmanAdi/chronos)
- [Project Homepage](https://aware-bloom-szmt.here.now)
- [Your LLM Agents are Temporally Blind](https://arxiv.org/abs/2510.23853)
- [chronos-skill npm Package](https://www.npmjs.com/package/chronos-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, hook configuration, and JSONL ledger data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local hook configuration and timing ledgers under the user's configured Chronos directory.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact files declare 1.0.0 in SKILL.md, package.json, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
