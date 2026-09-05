## Description:

Gives AI coding agents temporal awareness through a hook-backed ledger and decision rules for recency, retry windows, memory staleness, deploy cooldowns, idle detection, and date or time questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Chronos to give coding agents concrete time-awareness rules, local tool-use history, retry cooldown checks, staleness checks, and idle-loop safeguards during normal agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent local hooks that run on session, prompt, tool, and stop events and write timing metadata to a local ledger.

Mitigation: Use project-scoped installation for sensitive projects when available, review generated Claude and Codex configuration changes, and set CHRONOS_HOME and retention values deliberately.

Risk: Hook or installer changes can affect agent runtime behavior across supported platforms.

Mitigation: Keep installer source pinned or reviewed before use, and prefer dry-run or config-diff review paths where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/chronos)
- [Publisher profile](https://clawhub.ai/user/othmanadi)
- [Project homepage](https://aware-bloom-szmt.here.now)
- [Chronos repository](https://github.com/OthmanAdi/chronos)
- [Your LLM Agents are Temporally Blind](https://arxiv.org/abs/2510.23853)
- [chronos-skill npm package](https://www.npmjs.com/package/chronos-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands, JSONL examples, and platform configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install local hooks that write session and tool timing metadata to a local ledger.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
