## Description:

Provides headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research using Camoufox, OS-level input, and persistent fingerprints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and defensive security testers use this skill to drive authorized browser sessions against systems they own or have written permission to test, especially when standard headless automation is misclassified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detection-resistant automation can be misused against systems outside the user's authority.

Mitigation: Use the skill only on systems the user owns or has written authorization to test, and keep each run within the approved scope.

Risk: An unauthenticated API or VNC listener can expose full browser control, cookies, screenshots, and script execution.

Mitigation: Bind services to localhost, set a strong AUTH_TOKEN, send it as a Bearer token, and avoid exposing the VNC port beyond local debugging.

Risk: Page inspection, screenshots, storage, and cookies can capture sensitive content or persistent session data.

Mitigation: Collect only the data needed for the authorized test, use dedicated test accounts, and delete persistent profile data when testing ends.

Risk: Auto-accepted dialogs can approve destructive or irreversible actions on stateful sites.

Mitigation: Call handle_dialog with accept set to false before steps that may trigger confirmations, permission prompts, or beforeunload dialogs.

Risk: URL-triggered loaders run automatically and can modify page state.

Mitigation: Mount only loader YAML that has been written or audited by the user, and review loader behavior before enabling it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup](references/setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with JSON API examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is scoped to authorized browser automation and local service configuration.]

## Skill Version(s):

2.6.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
