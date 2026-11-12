## Description:

A three-tier pipeline for testing installable Huawei Cloud skills from individual checks through multi-skill flows and consolidated reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use the skill to check Huawei Cloud skill installation, derive and run functional tests, assess multi-skill flows, and review consolidated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command execution, installation ownership, approval records, and cleanup reporting have unresolved safety issues; existing installations or cloud resources could be affected.

Mitigation: Avoid production use until these issues are corrected. For evaluation, use a disposable environment, a separate skill-install directory, and restricted test credentials; independently verify cloud resources and every cleanup command.

Risk: A report may claim checks passed without verification.

Mitigation: Independently confirm test outcomes before relying on a report or using it to approve a skill.

Risk: The downloaded quality telemetry utility and its data collection were not inspected.

Mitigation: Disable telemetry with SKILL_QUALITY_REPORT=0 while evaluating the skill.

## Reference(s):

- [Huawei Cloud KooCLI setup](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)
- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-skill-tester)

## Skill Output:

**Output Type(s):** [JSON reports, Markdown reports, Shell commands, Testing guidance]

**Output Format:** [Structured JSON phase results and a consolidated Markdown report, produced through shell scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include per-phase outcomes and may include cloud resource lifecycle and cleanup details.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
