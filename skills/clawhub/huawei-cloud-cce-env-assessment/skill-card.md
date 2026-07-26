## Description: <br>
Collects Huawei Cloud CCE metrics and configurations to generate cloud-native assessment scoring, reports, and improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud platform engineers and application operators use this skill to assess Huawei Cloud CCE container environments against cloud-native best practices, then generate scoring spreadsheets, charts, HTML reports, and prioritized remediation guidance. <br>

### Deployment Geography for Use: <br>
Global, for Huawei Cloud CCE environments in supported Huawei Cloud regions. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Huawei Cloud access keys and can query CCE and Kubernetes environment metadata. <br>
Mitigation: Use least-privilege, temporary credentials dedicated to assessment, and revoke or rotate them after use. <br>
Risk: The workflow may involve local installation steps, downloaded KooCLI installers, and sudo for permission problems. <br>
Mitigation: Review installer commands before execution, verify downloads from Huawei Cloud sources, and approve sudo only when it is intentionally required. <br>
Risk: The workflow clears prior data and artifacts before collecting fresh assessment outputs. <br>
Mitigation: Run it in a clean workspace or back up existing data and artifacts before starting the assessment. <br>
Risk: The collection script can clone the configured Dockerfile repository into the workspace. <br>
Mitigation: Provide only trusted repository URLs and review cloned Dockerfile content as untrusted input before relying on assessment results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cce-env-assessment) <br>
- [Huawei Cloud KooCLI Installation Guide](references/koocli-installation-guide.md) <br>
- [Python Dependency Requirements](references/requirements.txt) <br>
- [Cloud-Native Assessment Template](templates/cloud-native-assessment-template.md) <br>
- [Report Template](templates/report_template.md) <br>
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated Excel workbook, SVG charts, and HTML report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Assessment artifacts are written under the skill's artifacts directory; intermediate collection data is written under the data directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
