## Description: <br>
Connects local agents to OnePilot for event recommendations, optional mailbox-code and calendar availability help, consent-based memory and feedback, application form support, and organizer-only event management or registration export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[y09749204-gif](https://clawhub.ai/user/y09749204-gif) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use OnePilot CLI to let local agents bind to a OnePilot account, recommend OPC and AI startup events, manage consent-based memory and feedback, assist with application forms, and support organizer-only workflows when the bound account has permission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a local OnePilot account token after binding. <br>
Mitigation: Keep the token file private, do not paste or commit it, and re-bind if the token is revoked or exposed. <br>
Risk: The skill can send preferences, availability summaries, application answers, feedback, issue reports, and organizer data to OnePilot when used. <br>
Mitigation: Bind only if OnePilot is trusted, review application answers before submission, and send feedback or issue reports only after user approval. <br>
Risk: Organizer registration export can expose sensitive attendee data. <br>
Mitigation: Use organizer export only from authorized accounts and handle exported registration data as sensitive. <br>


## Reference(s): <br>
- [OnePilot Website](https://onepilot.zeabur.app) <br>
- [Platform Adapter Notes](references/adapters.md) <br>
- [Activity Intent Few-shots](references/activity-intent-few-shots.md) <br>
- [ClawHub Skill Listing](https://clawhub.ai/y09749204-gif/skills/onepilot-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured CLI or JSON outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local files for application QR codes; account-bound commands can send user-approved data to OnePilot.] <br>

## Skill Version(s): <br>
0.1.23 (source: evidence release, VERSION, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
