## Description: <br>
Generate, fetch, poll, and clear disposable email addresses using the Vortex API for temporary inboxes during signup or testing flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[techwithanirudh](https://clawhub.ai/user/techwithanirudh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to create disposable inboxes, wait for incoming messages, fetch mailbox contents, and clear temporary mailboxes during low-risk signup or testing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Temporary mailbox contents are handled by a third-party hosted service. <br>
Mitigation: Use the skill only for low-risk signup or testing workflows, not for sensitive personal, financial, production, account-recovery, or secret-bearing email. <br>
Risk: Clearing a mailbox deletes the messages for the specified temporary address. <br>
Mitigation: Double-check the target email address before running the clear action. <br>


## Reference(s): <br>
- [temp-mail ClawHub page](https://clawhub.ai/techwithanirudh/skills/temp-mail) <br>
- [Vortex homepage](https://vortex.skyfall.dev) <br>
- [Vortex API base URL](https://vtx-api.skyfall.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with command examples and text or JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI can create a mailbox address, fetch messages, poll until messages arrive, or clear a mailbox.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
