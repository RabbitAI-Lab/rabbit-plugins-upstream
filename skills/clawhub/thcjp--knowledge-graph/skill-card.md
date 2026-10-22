## Description:

Maintains a SkillHub knowledge graph by adding, deleting, or superseding atomic notes under life/areas/**.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to maintain a SkillHub knowledge graph for AI-agent workflows by updating atomic notes and reviewing the resulting changes. It is not intended for decisions that require 100% certainty or unreviewed changes to important knowledge stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, and command execution authority with broad instructions for knowledge-graph maintenance.

Mitigation: Run it with narrow workspace access, avoid broad command execution unless necessary, and review proposed file and command actions before allowing changes.

Risk: Knowledge graph content under life/areas/** may contain private or important data.

Mitigation: Use explicit instructions, keep backups, and review outputs for sensitive information before sharing or committing them.

Risk: Delete, replace, or API-key-using workflows can cause data loss or credential exposure if approved without review.

Mitigation: Require confirmation for delete, replace, and API-key workflows, and keep credentials in environment variables or the host agent's secret store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-graph)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown, JSON-like status output, and agent-proposed file or command actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read, write, and execute commands when the host agent grants those capabilities.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
