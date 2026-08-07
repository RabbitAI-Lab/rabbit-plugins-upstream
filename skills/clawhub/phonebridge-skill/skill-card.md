## Description:

Phonebridge helps users get step-by-step guidance for enabling developer mode and USB debugging on common phone brands, exporting selected app data, backing up WeChat chats, and using ADB screen capture workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[woozakii](https://clawhub.ai/user/woozakii)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to receive beginner-friendly phone connection, USB debugging, app export, chat backup, and ADB capture guidance for their own devices and accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports sensitive phone-data workflows.

Mitigation: Confirm the user is working on their own device and account before following export, backup, or ADB guidance.

Risk: Exported chats and phone data can be sensitive.

Mitigation: Remind users to store exported data securely and avoid letting an agent read ~/PhoneMirror/ unless explicitly requested.

Risk: USB debugging can increase device exposure if left enabled.

Mitigation: Tell users to turn off USB debugging after completing the intended workflow.

Risk: The linked site currently includes third-party page tracking despite conflicting privacy claims.

Mitigation: Make users aware of the tracking concern before relying on the linked site.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/woozakii/skills/phonebridge-skill)
- [Server-resolved GitHub provenance](https://github.com/Woozakii/phonebridge/tree/main/phonebridge-skill)
- [Phonebridge tutorial site](https://b1f884fbf01f443d9e99f3d71dad32c6.gz4.agentos-app.net)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with step-by-step paths, backup reminders, FAQ-style troubleshooting, and occasional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's phone brand or requested data-export workflow.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
