## Description:

Use when the operator asks for model or reasoning-effort routing using a GPT-only or OpenClaw subscription palette, including a standing request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[theangrypit](https://clawhub.ai/user/theangrypit)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and developers use this skill to choose model and reasoning-effort recommendations for work across GPT-only or OpenClaw subscription choices, while respecting the active selection and the capabilities of the current host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes an unpinned global installer command, and scanner guidance says remote content was not verified.

Mitigation: Before running the command, inspect and verify the installer package and remote content, and review whether a global installation is appropriate.

Risk: The optional profile installer can change persistent agent profiles and supports replacing differing files when explicitly requested.

Mitigation: Review the target directory and existing profiles before installation; use replacement only when that change is intended.

## Reference(s):

- [GPT-only edition guidance](references/gpt-only.md)
- [OpenClaw subscription edition guidance](references/openclaw-subscriptions.md)
- [GPT-6.2 model and role review](references/gpt62-20261117.md)
- [T3 runtime mapping](references/t3-runtime.md)
- [Pstack role presets](references/pstack-role-presets.json)
- [Benchmark refresh and limitations](references/benchmarks-20261106.md)
- [ClawHub skill release](https://clawhub.ai/theangrypit/skills/model-capability-router)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Agent profiles]

**Output Format:** [Markdown guidance with inline shell commands and TOML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations do not prove or change the active host model or configuration.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
