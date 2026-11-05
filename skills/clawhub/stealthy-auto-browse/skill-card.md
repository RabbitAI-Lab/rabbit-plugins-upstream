## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and security testers use the skill to check anti-bot and browser compatibility behavior in controlled environments. Use it only on systems they own or have written authorization to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended setup may require SYS_ADMIN, a broad system privilege.

Mitigation: Review the requirement, prefer a configuration without it, or use a dedicated disposable VM if it is necessary.

Risk: An unauthenticated browser API or viewer exposed beyond localhost could allow full browser control.

Mitigation: Enable authentication and keep the viewer local or behind an authenticating proxy.

Risk: Browser dialogs and automatically loaded page scripts can change site state during a test.

Mitigation: Use isolated test accounts, audit loaders before mounting them, and disable automatic dialog acceptance before state-changing tests.

## Reference(s):

- [Setup and configuration](references/setup.md)
- [Project repository and documentation](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [API reference: humanized input](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script mode control flow](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, HTML, Images]

**Output Format:** [JSON API requests and responses; extracted page text or HTML; screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The returned content depends on the requested browser action; capture only what the authorized test needs.]

## Skill Version(s):

3.3.1 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
