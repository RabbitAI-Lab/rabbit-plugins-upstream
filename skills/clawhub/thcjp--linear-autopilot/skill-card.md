## Description: <br>
Automates Linear task processing with Discord notifications and git synchronization for agent-driven task workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent builders, and small teams use this skill to connect Linear tasks with Discord notifications, agent task execution, Linear status updates, and optional git synchronization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to connect Linear and Discord credentials for automation workflows. <br>
Mitigation: Use least-privilege Linear and Discord tokens, avoid plaintext secrets where possible, and restrict Discord task channels. <br>
Risk: Unattended task processing can update Linear, send Discord messages, and push git changes with limited safeguards. <br>
Mitigation: Require explicit bot mentions unless unattended processing is intended, disable autoPush until tested, and review changes before enabling git push automation. <br>
Risk: Referenced scripts or local commands may affect project state when executed. <br>
Mitigation: Review referenced scripts before running them and test the workflow in a controlled repository before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/linear-autopilot) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in Linear API calls, Discord messages, local file changes, git commits, and git pushes when the configured workflow is executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
