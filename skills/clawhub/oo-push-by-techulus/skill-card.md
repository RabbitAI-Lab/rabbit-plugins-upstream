## Description: <br>
Push by Techulus helps an agent send notifications through Push by Techulus using an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to send Push by Techulus notifications to all account-targeted devices or to a specific device group. It is useful when an agent needs to perform notification delivery without handling raw Push by Techulus API tokens directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notification sends are external side effects and may reach all devices targeted by the account or team API key. <br>
Mitigation: Confirm the exact message body, target group or all-device scope, and account/team API key context before running a send action. <br>
Risk: A missing, expired, or incorrectly scoped OOMOL connection can prevent actions from running. <br>
Mitigation: Use the documented first-time setup and connection recovery steps only after an auth or connection error occurs. <br>


## Reference(s): <br>
- [Push by Techulus homepage](https://push.techulus.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-push-by-techulus) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces action guidance and oo CLI commands; action responses may include JSON data and an execution identifier.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
