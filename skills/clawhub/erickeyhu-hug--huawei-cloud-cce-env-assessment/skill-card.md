## Description: <br>
A skill for Huawei Cloud Container Engine assessment that collects metrics and configurations from containerized application environments and generates a comprehensive cloud-native assessment report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to assess Huawei Cloud CCE application environments against cloud-native best practices, produce scoring artifacts, and identify remediation priorities. <br>

### Deployment Geography for Use: <br>
Global, subject to Huawei Cloud CCE regional availability. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Huawei Cloud AK/SK credentials and read CCE, Kubernetes, logging, security, and related resource information. <br>
Mitigation: Use temporary least-privilege credentials scoped to assessment-only access, and revoke or rotate them after the run. <br>
Risk: The workflow includes host commands, dependency installation, remote KooCLI installation guidance, and sudo fallback guidance. <br>
Mitigation: Review commands before execution, prefer preinstalled trusted tools, avoid automatic sudo or remote install scripts, and run in a controlled environment. <br>
Risk: The skill may clone or inspect a user-provided source repository for Dockerfile assessment. <br>
Mitigation: Confirm the repository URL before use and provide only repositories intended for assessment. <br>
Risk: Generated reports and workbooks may contain sensitive cluster, workload, image, security, and remediation details. <br>
Mitigation: Store generated artifacts in trusted locations and redact sensitive details before sharing outside approved channels. <br>


## Reference(s): <br>
- [Huawei Cloud KooCLI Installation Guide](references/koocli-installation-guide.md) <br>
- [Huawei Cloud KooCLI Latest Documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [Python Requirements](references/requirements.txt) <br>
- [Cloud-Native Assessment Collection Template](templates/cloud-native-assessment-template.md) <br>
- [Cloud-Native Report Template](templates/report_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Stepwise text/status updates, Markdown collection notes, an Excel scoring workbook, SVG charts, and an HTML assessment report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated files are written under the skill's data/ and artifacts/ directories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
