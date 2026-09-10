## Description:

Guides behavior-correction feedback by analyzing an agent mistake, improving the relevant prompt or workflow guard to reduce recurrence, and resuming the interrupted work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill when a fix-style feedback message identifies an agent behavior mistake. It guides root-cause analysis, prevention changes, completion of the interrupted work, and wrap-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently change future agent behavior through global memory, rule files, settings, and hooks.

Mitigation: Install only when a behavior-correction workflow is intended; prefer local or project-scoped use for sensitive workspaces.

Risk: Rule, settings, or hook changes can affect future sessions beyond the immediate correction.

Mitigation: Review every proposed persistent diff and require explicit approval before changes under ~/.claude, ~/.gemini, or ~/.agents.

Risk: Global hooks on shared or sensitive agent profiles can broaden the impact of a mistaken workflow guard.

Mitigation: Avoid global hooks on sensitive or shared profiles unless the hook behavior and scope have been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix)
- [SKILL.md](SKILL.md)
- [Step 2: Prompt Improvement](step2-improvement.md)
- [Step 3: Resume Original Work](step3-resume.md)
- [Step 4: Wrap-up](step4-wrapup.md)
- [Behavior Discipline](behavior-discipline.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional code blocks, shell commands, configuration changes, and task updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent agent-behavior changes when the workflow routes updates to memory, rules, settings, or hooks.]

## Skill Version(s):

0.6.1 (source: ClawHub release metadata, released 2026-09-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
