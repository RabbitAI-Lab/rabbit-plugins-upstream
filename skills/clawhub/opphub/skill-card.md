## Description: <br>
OppHub connects an OppHub account to OpenClaw so users can log in, add company knowledge, search business opportunities, and receive push updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mtty-ai](https://clawhub.ai/user/mtty-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OpenClaw and OppHub users use this skill to operate OppHub from chat or scheduled OpenClaw workflows: authenticate, configure push channels, submit company knowledge, and review matching opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ClawHub security review says the skill normalizes broad token, cron, local-memory, file-upload, and production-operations access that is not clearly scoped for users. <br>
Mitigation: Review before installing, use it only in workspaces where OppHub may receive company profiles, contract-derived data, and search-derived content, and require the publisher to document exactly what leaves the device. <br>
Risk: Discovery against private memory or wiki sources may expose context the user did not intend to share with OppHub. <br>
Mitigation: Avoid running discovery against private memory or wiki sources unless the user explicitly wants that context used. <br>
Risk: Bundled production docs, token diagnostics, uploads, and cron actions may create operational or privacy risk if they are not reviewed. <br>
Mitigation: Remove bundled production docs or secrets, redact token diagnostics, and add explicit confirmations for uploads and cron actions before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mtty-ai/skills/opphub) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/mtty-ai) <br>
- [Project homepage from clawdis metadata](https://github.com/mtty-ai/opphub-skill) <br>
- [OppHub API base URL](https://api.opphub.ruiplus.cn) <br>
- [OppHub registration page](https://api.opphub.ruiplus.cn/register) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text responses with JSON command results and shell command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate OppHub OAuth device-flow setup, OpenClaw plugin checks, channel configuration, knowledge submission, search, matching, and scheduled workflow guidance.] <br>

## Skill Version(s): <br>
5.0.0 (source: server release, SKILL.md frontmatter, package.json, CHANGELOG released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
