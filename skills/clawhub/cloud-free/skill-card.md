## Description: <br>
Cloud Free helps users choose consumer cloud storage services by device mix and clarify common sync and storage-space misconceptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users ask an agent for consumer cloud storage service selection and explanations for storage quota, photo backup, and sync behavior questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for command execution capability, API-key setup, and an optional callback URL despite a simple advisory purpose. <br>
Mitigation: Install with least privilege and avoid granting execution, API keys, or callback URLs unless the publisher documents why they are required and what data is sent. <br>
Risk: Consumer cloud-storage recommendations may affect account, sync, or storage decisions. <br>
Mitigation: Confirm storage quotas, sync settings, and deletion behavior in the relevant provider account before making irreversible changes. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/cloud-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional JSON-formatted result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include service recommendations, misconception explanations, and configuration caveats; normal use does not require generated files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
