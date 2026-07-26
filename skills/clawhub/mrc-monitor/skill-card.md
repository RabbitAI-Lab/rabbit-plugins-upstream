## Description: <br>
Real-time token monitoring for the MRC canteen order system that checks Firebase Firestore order status and notifies the current channel when monitored tokens are ready. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wysh3](https://clawhub.ai/user/wysh3) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to monitor one or more MRC canteen order tokens, receive an immediate monitoring confirmation, and get a channel notification when orders are ready. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The monitor polls an MRC Firebase order database every 15 seconds and sends notifications to the current channel. <br>
Mitigation: Install only when this behavior is desired and use explicit monitoring commands such as 'mrc 73' or 'token 97'. <br>
Risk: Local logs may contain token numbers and channel identifiers. <br>
Mitigation: Treat generated logs as local operational data and remove them when they are no longer needed. <br>
Risk: Messages with unrelated numbers could be interpreted as canteen tokens if the agent applies the skill too broadly. <br>
Mitigation: Use explicit canteen-token commands and avoid invoking monitoring for unrelated numeric messages. <br>


## Reference(s): <br>
- [Mrc Monitor ClawHub listing](https://clawhub.ai/wysh3/skills/mrc-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/wysh3) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and short status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Starts a background polling process and posts readiness updates to the selected channel.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
