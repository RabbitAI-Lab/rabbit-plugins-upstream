## Description: <br>
OnePilot CLI connects local agents to OnePilot for event recommendations, consent-based memory, application help, and organizer-only workbench support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[y09749204-gif](https://clawhub.ai/user/y09749204-gif) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and local-agent developers use OnePilot CLI to bind a OnePilot account, get personalized OPC and AI startup event recommendations, manage consent-based memory and feedback, draft application answers, and perform organizer workflows when authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Binding stores a local OnePilot agent token and uses it for account-scoped actions. <br>
Mitigation: Install only when comfortable binding a OnePilot account, keep the token private, and do not print, paste, commit, or share the local token file. <br>
Risk: The skill can send selected preferences, availability, application details, feedback, and organizer data to OnePilot. <br>
Mitigation: Send only purpose-limited data after user consent, and keep profile, memory, feedback, issue, and application metadata concise. <br>
Risk: Organizer workflows can involve attendee registration data and other personal information. <br>
Mitigation: Use organizer-only commands only with the bound account's organizer permissions and require explicit confirmation before viewing or exporting registration data. <br>
Risk: QR download behavior can retrieve image content from OnePilot-provided URLs. <br>
Mitigation: Use the QR download command only for trusted OnePilot-provided image URLs. <br>


## Reference(s): <br>
- [OnePilot Website](https://onepilot.zeabur.app) <br>
- [ClawHub Skill Page](https://clawhub.ai/y09749204-gif/skills/onepilot-cli) <br>
- [Platform Adapter Notes](references/adapters.md) <br>
- [Activity Intent Few-shots](references/activity-intent-few-shots.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OnePilot internal URLs, concise recommendation explanations, application-answer drafts, and local command examples.] <br>

## Skill Version(s): <br>
0.1.23 (source: VERSION, package.json, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
