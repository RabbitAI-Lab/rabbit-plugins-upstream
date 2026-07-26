## Description: <br>
Build and deploy OpenClaw as Docker images or portable packages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zfanmy](https://clawhub.ai/user/zfanmy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to package, transfer, and run OpenClaw deployments in clean or full configurations across servers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The full package workflow can include private OpenClaw configuration, tokens, chat history, and workspace data. <br>
Mitigation: Use the clean package unless a full migration is intentional; inspect and remove sensitive data before creating or sharing a full package. <br>
Risk: Portable archives can expose sensitive deployment data if copied or stored without controls. <br>
Mitigation: Protect archives in transit and at rest, and share them only with intended operators. <br>
Risk: Build output can overwrite or collect data from an unintended location if paths are misconfigured. <br>
Mitigation: Verify OUTPUT_DIR points only to disposable build output before running packaging scripts. <br>
Risk: The included Node.js installer downloads and runs an external NVM installation script. <br>
Mitigation: Review or replace the NVM install script before execution in managed environments. <br>


## Reference(s): <br>
- [OpenClaw Deploy on ClawHub](https://clawhub.ai/zfanmy/skills/openclaw-deploy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or adapt deployment commands for Docker images and portable OpenClaw packages.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
