## Description:

A skill for Huawei Cloud CCE assessment that collects metrics and configurations from containerized application environments and generates a comprehensive report on alignment with cloud-native best practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and cloud operations teams use this skill to assess Huawei Cloud CCE-based container environments, score cloud-native readiness, and generate prioritized improvement recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Huawei Cloud access keys and can collect sensitive cluster and application data.

Mitigation: Run it with least-privilege, temporary credentials in an isolated environment and treat generated data and artifacts as sensitive.

Risk: The skill may suggest host-changing commands such as sudo operations, remote installer execution, pip installs, and file removal.

Mitigation: Review each command before execution and run only the host changes that are explicitly intended for the assessment environment.

Risk: Generated assessment findings may overstate some security-check results or include checks asserted without direct evidence.

Mitigation: Review the report critically and confirm high-impact recommendations against the collected evidence before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cce-env-assessment)
- [KooCLI installation guide](references/koocli-installation-guide.md)
- [Cloud-native checklist workbook](references/cloud-native-checklist.xlsx)
- [Python requirements](references/requirements.txt)
- [Cloud-native assessment collection template](templates/cloud-native-assessment-template.md)
- [Cloud-native report template](templates/report_template.md)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html)
- [Huawei Cloud CCE EOS bulletin](https://support.huaweicloud.com/intl/zh-cn/bulletin-cce/cce_bulletin_0033.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Step-by-step guidance plus Markdown collection notes, an Excel scoring workbook, SVG charts, and an HTML assessment report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written under the skill's data/ and artifacts/ directories during execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
