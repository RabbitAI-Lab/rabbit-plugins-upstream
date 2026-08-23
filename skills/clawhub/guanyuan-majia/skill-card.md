## Description:

A Guandata BI agent skill that routes standard BI work to the official Guandata CLI family and provides battle-tested guidance for ETL governance, custom chart debugging, v7 page publishing, SuperApp workflows, AI-native ADS design, and restaurant BI formulas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Developers, BI operators, and analytics teams use this skill to work with Guandata BI environments through agent-assisted analysis, ETL governance, dashboard customization, publish workflow troubleshooting, and implementation guidance around official Guandata tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers high-impact BI write and delete workflows, including ETL rewrites, descriptor patches, form writes, and force-delete guidance.

Mitigation: Treat these as privileged operations: verify target IDs, target environment, backups or source files, and downstream references before approving execution.

Risk: Agent-assisted BI administration can affect production dashboards, datasets, ETL jobs, and business metrics if used in the wrong Guandata environment.

Mitigation: Install and use the skill only in Guandata BI environments where the operator is authorized to let an agent assist with BI administration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [Publisher Profile](https://clawhub.ai/user/maojiebc)
- [Project Homepage](https://github.com/maojiebc/majia-guanyuan)
- [README.en.md](README.en.md)
- [Security Policy](SECURITY.md)
- [Attributions](ATTRIBUTIONS.md)
- [ETL Full-Chain Rewrite Methodology](references/part-b17-fullchain-rewrite.md)
- [Custom Chart Playbook](references/custom-chart-playbook.md)
- [HTML Dashboard Playbook](references/part-c-html-dashboard.md)
- [V7 Page/Card Publish Pipeline](references/v7-page-card-publish-pipeline.md)
- [SuperApp Pipeline](references/part-e-superapp-pipeline.md)
- [AI-Native ADS Design](references/ai-native-ads-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, code snippets, and procedural checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to official Guandata CLI tools and to local reference playbooks for detailed procedures.]

## Skill Version(s):

3.1.9 (source: SKILL.md frontmatter, package.json, manifest.json, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
