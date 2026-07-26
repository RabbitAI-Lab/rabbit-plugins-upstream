## Description: <br>
Automatically scans UUMit tasks, matches them against configured skills, submits applications, monitors status, and sends approval notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cx75227-ops](https://clawhub.ai/user/cx75227-ops) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to automate UUMit task discovery, skill matching, application submission, status monitoring, and approval notifications. It is intended for paid task workflows and requires careful control of API credentials, spending limits, and any automatic application or settlement behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic applications or USDT settlement could submit paid task actions or spend funds with too little user control. <br>
Mitigation: Use manual confirmation before applications or payments, set clear spending limits, and do not enable unattended auto-apply or automatic USDT settlement unless the operator understands how to stop it. <br>
Risk: A broad UUMit API key could expose more account access than the workflow requires. <br>
Mitigation: Use a limited-scope UUMit API key and keep a clear revocation path before installing or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cx75227-ops/skills/uumit-auto-bot) <br>
- [Publisher profile](https://clawhub.ai/user/cx75227-ops) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe task matches, application actions, monitoring status, notifications, and billing-related setup.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
