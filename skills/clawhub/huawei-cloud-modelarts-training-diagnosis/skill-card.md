## Description: <br>
Huawei Cloud ModelArts training job fault diagnosis skill that uses hcloud CLI to call ModelArts training job log and event APIs, analyze failures, timeouts, abnormal or stuck jobs, locate customer training code issues, and provide diagnosis conclusions with fix suggestions and confidence levels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to diagnose Huawei Cloud ModelArts training job failures, timeouts, abnormal states, and stuck runs from job status, logs, events, and stage data. It helps produce evidence-based root-cause summaries, confidence levels, and manual remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on hcloud credentials and can expose ModelArts training job metadata and diagnostic logs to the agent. <br>
Mitigation: Use least-privilege read-only Huawei Cloud credentials and avoid pasting or displaying AK/SK values. <br>
Risk: Training logs and temporary OBS log URLs may contain sensitive data. <br>
Mitigation: Redact logs and temporary URLs before sharing, and include only key error or traceback excerpts in reports. <br>
Risk: Installer and cleanup guidance includes non-interactive script execution and removal of local hcloud configuration. <br>
Mitigation: Verify installer downloads independently and only remove ~/.hcloud/ after intentionally backing up or retiring local profiles and credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-modelarts-training-diagnosis) <br>
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [ModelArts Training Job Diagnosis API Catalog](references/api-catalog.md) <br>
- [Training Job Diagnosis Flow Details](references/diagnosis-flow.md) <br>
- [hcloud Command Templates](references/hcloud-command-templates.md) <br>
- [Confidence Level Judgment Rules + Output Contract](references/confidence-rules.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown diagnosis report with command snippets and structured confidence levels] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses evidence from read-only ModelArts status, event, stage, and log APIs; fix actions are guidance for user-confirmed manual execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
