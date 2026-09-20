## Description:

Helps agents work with Guandata BI by routing standard querying, dashboard, ETL, dataset, workflow, and metric tasks to the official Guandata CLI suite while adding field-tested guidance for ETL governance, SmartETL rewrites, custom charts, HTML dashboards, v7 publishing, SuperApp compatibility, and AI-native data architecture decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Developers, BI operators, and analytics engineers use this skill to guide agents through Guandata BI operations, especially cases where standard CLI workflows need business context, ETL governance judgment, custom chart troubleshooting, or release compatibility checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact BI operations, including dashboard overwrite and deletion workflows.

Mitigation: Use it only in Guandata BI environments you administer, require explicit target lists, and keep backups before allowing writes.

Risk: Production dashboard or ETL changes may be difficult to reverse if an agent proceeds from stale assumptions or ambiguous targets.

Mitigation: Require dry-runs, diffs, or previews where available, and require separate confirmation for guanvis upload, DELETE, and force=true actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [Project homepage](https://github.com/maojiebc/majia-guanyuan)
- [Official CLI compatibility](references/official-cli-compatibility.md)
- [SmartETL full-chain rewrite methodology](references/part-b17-fullchain-rewrite.md)
- [Custom chart playbook](references/custom-chart-playbook.md)
- [HTML dashboard playbook](references/part-c-html-dashboard.md)
- [v7 page/card publish pipeline](references/v7-page-card-publish-pipeline.md)
- [SuperApp pipeline](references/part-e-superapp-pipeline.md)
- [Security policy](SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON/configuration snippets, code examples, and BI workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use official Guandata CLI commands and to require confirmation before high-impact writes.]

## Skill Version(s):

3.2.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
