## Description:

Launch and drive coding agents (codex, claude, agy) through the Herdr CLI reliably.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when launching, prompting, monitoring, or recovering Herdr-controlled coding subagents. It provides operational recipes for Codex, Claude Code, and agy sessions, with emphasis on avoiding lost prompts and diagnosing misleading agent states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes commands that can start or control subagents, close panes, stop or update the Herdr server, and configure child-agent permissiveness.

Mitigation: Review each command before execution and use the skill only when the agent is expected to operate Herdr-controlled subagents.

Risk: Auto-approval flags and prompt-driving recipes may delegate actions to child agents with less human intervention.

Mitigation: Apply auto-approval only in environments where that level of delegation is intended, and verify agent state through Herdr reads before sending or resending prompts.

## Reference(s):

- [Herdr documentation](https://herdr.dev)
- [herdr-faq homepage](https://github.com/tenequm/skills/tree/main/skills/herdr-faq)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/herdr-faq)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance for operating Herdr-controlled subagents.]

## Skill Version(s):

0.1.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
