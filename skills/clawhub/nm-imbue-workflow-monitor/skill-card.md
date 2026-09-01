## Description:

Detects workflow failures and inefficient patterns then files GitHub issues

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to monitor workflow executions, classify failures and inefficiencies, and prepare structured issue reports for repository follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow diagnostics can capture command output, paths, session context, stack traces, environment notes, tokens, or proprietary snippets and may place them into GitHub or GitLab issues.

Mitigation: Keep automatic issue creation disabled unless the repository is trusted and private, and review or redact captured evidence before creating issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-workflow-monitor)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)
- [Detection patterns](artifact/modules/detection-patterns.md)
- [Efficiency metrics](artifact/modules/efficiency-metrics.md)
- [Issue templates](artifact/modules/issue-templates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown reports with issue templates, command examples, and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow evidence excerpts, efficiency scores, labels, and suggested fixes.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
