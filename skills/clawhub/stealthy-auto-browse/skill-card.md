## Description:

Provides headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research using Camoufox, OS-level input, and persistent fingerprints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and defensive security testers use this skill to automate browser sessions against sites they own or have written authorization to test, especially when validating anti-bot compatibility or investigating false-positive headless-browser blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a browser session against sites that may treat automation as sensitive.

Mitigation: Use it only for sites you own or have written authorization to test, and keep test scope explicit.

Risk: An exposed HTTP API or noVNC viewer can give another party browser control, including access to session data.

Mitigation: Bind ports to 127.0.0.1, set AUTH_TOKEN for non-local use, and avoid exposing noVNC unless it is locally confined.

Risk: Persistent profiles can retain cookies, credentials, and fingerprint state beyond a test run.

Mitigation: Use isolated test accounts, treat profile volumes as secrets, and remove profile data when testing concludes.

Risk: Dialogs are auto-accepted by default and could approve unintended state-changing actions.

Mitigation: Disable or scope dialog auto-accept before flows that might trigger confirm, permission, or beforeunload prompts.

Risk: Loader files execute automatically on matching URLs and can modify page state.

Mitigation: Mount only loader, profile, and media files that were written or audited for the authorized test.

Risk: Container execution, network access, and mounted volumes expand the operational impact of misuse or compromise.

Mitigation: Review or build the Docker image before use, pin reviewed image digests, restrict egress and mounts, and avoid privileged or unnecessary host access.

## Reference(s):

- [Setup](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [Script mode control flow reference](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API examples, YAML script examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide HTTP API, MCP, Docker, script-mode, screenshot, recording, and browser-session workflows for authorized targets.]

## Skill Version(s):

2.6.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
