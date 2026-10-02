## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and authorized security testers use this skill to drive a Dockerized browser for anti-bot compatibility checks, regression testing, and defensive research on systems they own or have written permission to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Headless-detection-resistant browser automation can be misused against unauthorized targets.

Mitigation: Install only for authorized QA or defensive testing and use it only with sites the user owns or has written permission to test.

Risk: If AUTH_TOKEN is unset or the service is exposed beyond localhost, reachable users can control the browser session.

Mitigation: Bind the API and noVNC ports to localhost, set a strong AUTH_TOKEN, and keep any remote access behind an authenticating proxy.

Risk: Browser inspection, screenshots, script execution, and persistent profiles can expose page data, cookies, and live sessions.

Mitigation: Scope data capture to the authorized test, use isolated test accounts, treat profile volumes as secrets, and remove or rotate session data after testing.

Risk: Dialogs are auto-accepted by default and URL loaders execute automatically on matching pages.

Mitigation: Disable or scope dialog auto-accept before stateful actions and mount only loader YAML files that have been written or audited for the test.

Risk: Mutable container tags or broad container privileges can change the reviewed runtime or increase host exposure.

Mitigation: Pin the Docker image by digest, review compose or loader files before use, avoid privileged mode and Docker socket mounts, and restrict network egress to the test target.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [Script mode control flow reference](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, YAML, and shell command examples; browser actions may return JSON, page text, HTML, screenshots, recordings, cookies, logs, and script outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and curl; uses STEALTHY_AUTO_BROWSE_URL as the primary endpoint and AUTH_TOKEN for authenticated deployments.]

## Skill Version(s):

2.6.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
