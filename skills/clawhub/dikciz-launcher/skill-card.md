## Description:

Install and operate Dikciz Launcher on an owner-selected Android device through its MCP, HTTP, or WebSocket controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External users and Android device operators use the skill to install and control Dikciz Launcher on an owner-selected phone, including launcher settings, device data, sensors, hardware, files, and requested automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote controls and privileged shell commands can affect the selected phone or its data.

Mitigation: Use narrowly scoped access tokens and only the Android permissions needed for the requested task; review privileged commands and verify effects.

Risk: Capture and assistant features can expose phone data to configured providers, and active captures or event subscriptions may continue after a task.

Mitigation: Review data recipients, share only the needed data, stop capture sessions, and remove unneeded event subscriptions when finished.

Risk: The bundled documentation review does not establish the safety of a separately supplied controller or installed Android app.

Mitigation: Review the controller and APK before use.

## Reference(s):

- [Setup and connection](references/setup.md)
- [Capabilities](references/capabilities.md)
- [Hardware and speech operations](references/hardware-and-speech.md)
- [Files, notifications, and durable jobs](references/operations.md)
- [Dikciz Launcher documentation index](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/index.md)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Dikciz Launcher release page](https://clawhub.ai/psyb0t/skills/dikciz-launcher)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls, Files and operation results]

**Output Format:** [Markdown guidance, shell commands, configuration examples, and structured operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available actions and results depend on the connected Android build and its granted permissions.]

## Skill Version(s):

0.30.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
