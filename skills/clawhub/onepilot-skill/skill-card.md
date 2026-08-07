## Description: <br>
Connect local agents to OnePilot for event recommendations, consent-based memory and feedback, application form support, and organizer-only event management or registration export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[y09749204-gif](https://clawhub.ai/user/y09749204-gif) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to connect a local agent to OnePilot, request event and resource recommendations, manage consent-based memory and feedback, draft application answers, and use organizer workflows when their account has permission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill binds a OnePilot account and stores a local agent token under ~/.config/onepilot/agent.json. <br>
Mitigation: Install only when comfortable binding the account to the local agent, protect the token file on shared machines, and remove it when the binding is no longer needed. <br>
Risk: Approved workflows can send selected recommendation, memory, application, feedback, issue-report, or organizer data to OnePilot. <br>
Mitigation: Send only the minimum necessary data, require explicit user approval for memory, feedback, calendar writes, application submission, issue reporting, and organizer exports, and avoid uploading secrets or private messages. <br>
Risk: Custom QR download output paths or organizer registration exports can contain personal data. <br>
Mitigation: Use deliberate output paths, review export contents before sharing, and store or delete exported files according to the user's privacy needs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/y09749204-gif/skills/onepilot-skill) <br>
- [OnePilot website](https://onepilot.zeabur.app) <br>
- [Activity intent examples](references/activity-intent-few-shots.md) <br>
- [Platform adapters](references/adapters.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local CLI calls for account status, event recommendations, memory, feedback, application help, issue reports, and organizer workflows after the required user approval.] <br>

## Skill Version(s): <br>
0.1.24 (source: package.json, VERSION, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
