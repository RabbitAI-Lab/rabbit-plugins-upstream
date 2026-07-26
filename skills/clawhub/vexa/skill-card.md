## Description: <br>
Send bots to Zoom, Google Meet, and Microsoft Teams meetings, then retrieve live transcripts, recordings, and reports from Vexa Cloud or a self-hosted Vexa instance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dmitriyg228](https://clawhub.ai/user/dmitriyg228) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and meeting operators use this skill to start and manage Vexa meeting bots, read transcripts and recordings, configure webhook-based report creation, and write local meeting reports. It supports Vexa Cloud and self-hosted Vexa endpoints for Google Meet, Microsoft Teams, and Zoom workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting transcripts, recordings, share links, and generated reports may contain sensitive participant or workplace information. <br>
Mitigation: Use the skill only with participant consent and policy approval; avoid transcript share links unless intended, and prefer --no-share for meeting bundles. <br>
Risk: Optional webhook automation can convert meeting-finished events into agent instructions that write persistent reports and entity memory. <br>
Mitigation: Keep webhook automation disabled unless needed, and review generated reports plus memory/entities changes before relying on them. <br>
Risk: API keys grant access to Vexa meeting data and bot controls. <br>
Mitigation: Set VEXA_API_KEY through the environment or local secrets files, never through chat, and keep the secrets directory excluded from publishing. <br>
Risk: Meeting and recording deletion commands can remove or anonymize stored meeting data. <br>
Mitigation: Run destructive delete commands only after confirming the exact meeting or recording identity and using the required --confirm DELETE guard. <br>


## Reference(s): <br>
- [ClawHub Skill Vexa page](https://clawhub.ai/dmitriyg228/skills/vexa) <br>
- [Vexa onboarding flow](artifact/references/onboarding-flow.md) <br>
- [Vexa API reference notes](artifact/references/user-api-guide-notes.md) <br>
- [Vexa webhook setup](artifact/references/webhook-setup.md) <br>
- [Vexa API keys dashboard](https://vexa.ai/dashboard/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown, Files, Configuration] <br>
**Output Format:** [Chat guidance with shell commands and JSON CLI responses; generated meeting reports are Markdown files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write meeting reports under memory/meetings/ and local Vexa state or endpoint files under the skill secrets directory.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
