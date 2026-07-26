## Description: <br>
Team Memory is a local Markdown-based long-term memory assistant for managers to record team observations, 1:1 notes, OKR and performance evidence, stakeholder feedback, follow-up tasks, dashboards, reports, migrations, local indexes, exports, and privacy-preserving team records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jichengkai](https://clawhub.ai/user/jichengkai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Managers and team leads use this skill to maintain local long-term records for team members, stakeholder feedback, follow-up tasks, performance evidence, 1:1 preparation, status reports, reviews, promotions, retrospectives, and upward communication. It is designed for sensitive personnel notes stored in a locked local Markdown data directory with generated machine indexes and exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intended to store sensitive team, performance, 1:1, and stakeholder feedback locally. <br>
Mitigation: Keep the data directory and exported archives out of public repositories and shared drives unless they are explicitly protected. <br>
Risk: Dashboard or report outputs may summarize sensitive personnel information for broader audiences. <br>
Mitigation: Review generated dashboards, reports, and exports before sharing them outside the intended management context. <br>
Risk: Imports, migrations, and task resolution workflows can change local records if applied without review. <br>
Mitigation: Use the provided dry-run and confirmation flows before applying imports, migrations, or task resolution changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jichengkai/skills/team-memory) <br>
- [Usage guide](references/usage.md) <br>
- [Record templates](references/record-templates.md) <br>
- [Scenario examples](references/scenario-examples.md) <br>
- [Team dashboard data architecture](references/team-dashboard.md) <br>
- [Markdown import guide](references/import-markdown.md) <br>
- [Upgrade and migration guide](references/upgrade.md) <br>
- [Troubleshooting guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, local file updates, SVG/Markdown/JSON dashboards, JSONL/SQLite indexes, exports, and configuration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill works from a locked local Markdown data directory and treats JSONL/SQLite indexes as rebuildable outputs rather than source data.] <br>

## Skill Version(s): <br>
2.6.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
