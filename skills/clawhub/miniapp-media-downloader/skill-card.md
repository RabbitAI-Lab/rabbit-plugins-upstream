## Description: <br>
Resolve and download media from 视频号、抖音、小红书 through a configured resolver, plus local B站 downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harven-droid](https://clawhub.ai/user/harven-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure, call, debug, and maintain media resolver workflows for supported miniapp platforms and local Bilibili downloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted links or full share text are sent to the configured resolver service. <br>
Mitigation: Submit only the minimal URL needed for resolution when possible, and avoid including private share text. <br>
Risk: Distribution keys and service credentials can grant resolver access. <br>
Mitigation: Treat distribution keys, cookies, service credentials, and admin passwords as secrets; do not print or commit them. <br>
Risk: Remote resolver behavior depends on a configured external service and private platform credentials for some platforms. <br>
Mitigation: Install only when this resolver workflow is intended, verify the configured service endpoint and key source, and keep public documentation limited to the approved contact and configuration flow. <br>


## Reference(s): <br>
- [Miniapp Media Downloader on ClawHub](https://clawhub.ai/harven-droid/skills/miniapp-media-downloader) <br>
- [Multi-platform resolver service notes](artifact/references/dayuMiniPragram.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce resolver requests, troubleshooting steps, local downloader guidance, and code or configuration changes.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
