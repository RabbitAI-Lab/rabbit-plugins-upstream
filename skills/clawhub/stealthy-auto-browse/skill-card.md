## Description:

Provides browser automation in Docker for authorized QA, compatibility testing, and defensive security research where headless-browser detection interferes with testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA or security teams use this skill to automate browser tests on sites they own or have written permission to test, including anti-bot compatibility and regression checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detection-resistant automation can be misused against sites outside the approved test scope.

Mitigation: Use only on systems you own or have written permission to test; restrict data capture to the authorized task.

Risk: An exposed API or VNC viewer can grant browser and session control, especially without authentication.

Mitigation: Bind API and VNC ports to localhost, set AUTH_TOKEN, and do not publish the viewer unless needed.

Risk: Persistent browser profiles can retain live session cookies and other sensitive data.

Mitigation: Use isolated test accounts, protect profile volumes as secrets, and remove them after testing.

Risk: URL-matched loaders execute automatically and default dialog acceptance can approve unintended actions.

Mitigation: Audit loader YAML before mounting and reject unexpected dialogs before state-changing steps.

Risk: Container access through SYS_ADMIN weakens isolation, and mutable image tags can change what runs.

Mitigation: Pin the reviewed image by digest and apply the documented container hardening and restricted egress.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup guide](artifact/references/setup.md)
- [Humanized input reference](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script control-flow reference](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [Text, JSON, Images, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and JSON browser results; screenshots may be returned as images or base64 data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browser results may include page content and session data; scope captures to authorized tests.]

## Skill Version(s):

3.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
