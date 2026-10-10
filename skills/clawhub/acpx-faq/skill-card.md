## Description:

Run coding agents (codex, claude, agy) through the acpx ACP CLI - one-shot dispatch into named sessions you can watch live. Use before launching or prompting a subagent, or when a command fails, a session is missing, or a prompt is lost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and operators use this skill to dispatch coding agents through acpx, manage named sessions, and troubleshoot failed or missing turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery advice can route blocked prompts around safety checks.

Mitigation: Do not automate classifier-bypass advice; require explicit user approval before retrying previously blocked content.

Risk: Broadly approved child agents may modify the selected workspace.

Mitigation: Use isolated worktrees, clean prompts, and minimal credentials; review proposed commands and changes before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tenequm/skills/acpx-faq)
- [Skill homepage (release metadata)](https://github.com/tenequm/skills/tree/main/skills/acpx-faq)
- [acpx CLI](https://github.com/openclaw/acpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent dispatch, session management, and troubleshooting guidance.]

## Skill Version(s):

0.9.0 (source: ClawHub release metadata, skill frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
