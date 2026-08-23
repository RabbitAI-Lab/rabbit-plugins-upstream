## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and defensive security testers use this skill to drive a Dockerized browser for authorized anti-bot QA, compatibility testing, and controlled security research where standard headless browsers produce false-positive blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser automation surface can control navigation, input, cookies, screenshots, and script execution.

Mitigation: Use only on systems you own or have written authorization to test, keep API and VNC access bound to localhost, and set AUTH_TOKEN for any non-trivial run.

Risk: Page text, HTML, DOM structure, screenshots, recordings, network logs, console logs, cookies, and storage can capture sensitive information.

Mitigation: Limit collection to the authorized test scope, use test accounts, avoid persisting real session data, and remove profile data after testing.

Risk: Dialogs are auto-accepted by default and could approve state-changing actions.

Mitigation: Disable or scope dialog auto-accept before stateful flows and review scripts before running them against accounts or data.

Risk: URL-triggered loader YAML executes automatically on matching pages and can modify page state.

Mitigation: Mount only loader files you wrote or audited, and review loader steps before deployment.

Risk: Container images, exposed ports, VNC, and mounted volumes can expand operational exposure.

Mitigation: Pin reviewed image digests, bind ports to 127.0.0.1, avoid privileged Docker settings and docker socket mounts, and restrict writable volumes to the needed test paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe browser actions, MCP tool usage, Docker configuration, screenshots, recordings, script-mode JSON outputs, and operational safeguards.]

## Skill Version(s):

2.6.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
