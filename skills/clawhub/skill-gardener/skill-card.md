## Description:

When a workflow is proven, corrected, recurring, or worth retaining: create, repair, deduplicate, and verify a lean local skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadowninex](https://clawhub.ai/user/shadowninex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to turn verified, recurring workflows into local OpenClaw skills, repair stale skills, avoid duplicates, and validate the resulting skill collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change persistent local agent behavior by creating or modifying skills.

Mitigation: Review diffs for created or patched SKILL.md files and scripts before deployment.

Risk: Newly added helper code or companion skills may expand agent behavior beyond the operator's intent.

Mitigation: Require explicit approval before running newly added helper code and verify companion skills before installation.

## Reference(s):

- [Self-Improving Agent](https://github.com/pskoett/self-improving-agent)
- [Self-Improving Agent on ClawHub](https://clawhub.ai/pskoett/skills/self-improving-agent)
- [Skill Vetter on ClawHub](https://clawhub.ai/spclaudehome/skills/skill-vetter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks and optional file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or patch local skill files and run validation commands when the agent has appropriate workspace access.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
