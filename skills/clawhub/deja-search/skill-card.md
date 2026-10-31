## Description:

deja-search helps coding agents retrieve prior decisions and solutions from a user's AI coding sessions before they repeat work, debug an old issue, or make recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using AI coding agents can look up decisions, fixes, and preferences from earlier sessions before editing, debugging, recommending tools, or reporting work as complete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Past conversations from multiple coding tools can enter the current agent's context.

Mitigation: Exclude sensitive projects from searches.

Risk: Recalled commands and shared rules may not fit the current task.

Mitigation: Check recalled commands against the current task and select shared rules only when you want them applied across agents.

## Reference(s):

- [Memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text context from earlier coding sessions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Historical material is reference context; apply it according to the skill's instructions.]

## Skill Version(s):

0.23.3 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
