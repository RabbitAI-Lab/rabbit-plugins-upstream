## Description:

Inventories and classifies installed OpenClaw skills, detects duplicates and missing dependencies, and exports reports in Markdown, JSON, or HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kuntao2011](https://clawhub.ai/user/kuntao2011)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and administrators can audit installed skills, review classifications and dependencies, and export inventories. Optional commands check for updates, change skill activation, or publish a report to Feishu or Notion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTML reports can execute malicious metadata from untrusted third-party skills.

Mitigation: Use Markdown or JSON reports when inventorying untrusted skills instead of opening the HTML report.

Risk: Update checks may contact git remotes recorded in local skill metadata.

Mitigation: Avoid --check-updates unless contacting those remotes is acceptable.

Risk: Publishing a report can send skill inventory details to Feishu or Notion.

Mitigation: Use --push only when sharing that inventory is intended and the destination credentials are appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kuntao2011/skills/skill-classifier)

## Skill Output:

**Output Type(s):** [Markdown, JSON, HTML]

**Output Format:** [Markdown, JSON, or standalone HTML inventory reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report labels and CLI output are in Chinese; optional Feishu and Notion publishing.]

## Skill Version(s):

1.2.2 (source: ClawHub release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
