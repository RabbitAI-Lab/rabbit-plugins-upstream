## Description:

Assesses Huawei Cloud CCE environments by collecting configuration and metric data, scoring cloud-native readiness, and generating reports with improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and cloud operations teams use this skill to assess Huawei Cloud CCE container environments against cloud-native best practices and identify prioritized improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud credentials that can read CCE, AOM, LTS, and HSS resources.

Mitigation: Use least-privilege, temporary AK/SK credentials or an existing scoped profile, and revoke or rotate them after the assessment.

Risk: The workflow can run broad local and cloud collection actions.

Mitigation: Run it only in an approved assessment workspace and review each proposed step before confirming execution.

Risk: The workflow may delete prior contents under data/ and artifacts/ during environment checks.

Mitigation: Review and back up any needed files in those directories before starting or continuing the workflow.

Risk: Installer guidance includes sudo and non-interactive install or uninstall commands.

Mitigation: Install prerequisites manually where possible, and avoid running sudo or non-interactive installer/uninstall commands through the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-cce-env-assessment)
- [Huawei Cloud KooCLI Installation Guide](references/koocli-installation-guide.md)
- [Cloud Native Checklist](references/cloud-native-checklist.xlsx)
- [Python Requirements](references/requirements.txt)
- [Huawei Cloud KooCLI Release Notes](https://support.huaweicloud.com/wtsnew-hcli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated HTML, Excel, SVG, JSON, and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes intermediate collection data under data/ and final reports, charts, and scoring workbooks under artifacts/.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
