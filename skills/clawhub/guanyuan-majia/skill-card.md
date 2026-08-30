## Description:

观远 BI · 马甲实战版 is an Agent Skill for Guandata BI operators and developers that routes standard BI work to the official Guandata CLI family and provides playbooks for ETL governance, custom dashboard and chart work, SuperApp development, and AI-native ADS design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Developers, BI administrators, and data teams use this skill when working inside Guandata BI environments to plan and troubleshoot ETL governance, dashboard publishing, custom chart injection, SuperApp workflows, metric operations, and BI-specific data architecture decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact BI write and delete workflows.

Mitigation: Review destructive commands before use and require explicit resource IDs, names, and backup or rebuild confidence before approving deletes.

Risk: Incorrect BI guidance could change dashboards, ETL jobs, datasets, or metrics in a user's Guandata environment.

Mitigation: Use the skill in administered Guandata BI environments, prefer preview or dry-run steps where available, and verify target resources before applying changes.

## Reference(s):

- [Project homepage from metadata.clawdis](https://github.com/maojiebc/majia-guanyuan)
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [README.en.md](README.en.md)
- [ETL governance and write playbook](references/part-b17-fullchain-rewrite.md)
- [Custom chart playbook](references/custom-chart-playbook.md)
- [HTML dashboard playbook](references/part-c-html-dashboard.md)
- [SuperApp pipeline playbook](references/part-e-superapp-pipeline.md)
- [AI-native ADS design methodology](references/ai-native-ads-design.md)
- [Restaurant BI formula library](https://github.com/maojiebc/majia-huiyuan/tree/main/公式库)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration examples, and BI workflow checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed before execution when they affect BI assets, especially write and delete workflows.]

## Skill Version(s):

3.1.10 (source: SKILL.md frontmatter, package.json, CHANGELOG, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
