## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to run authorized QA, anti-bot compatibility checks, and defensive testing against sites they own or have written permission to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples use the mutable Docker image tag `latest`, which may change between runs.

Mitigation: Review image changes before upgrading and pin a reviewed version or digest for repeatable deployments.

Risk: Without `AUTH_TOKEN`, anyone who can reach the browser API can control the browser.

Mitigation: Bind published ports to localhost and set `AUTH_TOKEN` before exposing the service beyond a local smoke test.

Risk: Browser dialogs accept automatically by default and can confirm destructive actions.

Mitigation: On stateful sites, disable acceptance with `handle_dialog` before actions that may raise a dialog.

Risk: Mounted page loaders run automatically on matching URLs and may change page state.

Mitigation: Review and audit every loader YAML file before mounting it.

## Reference(s):

- [Setup guide](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [API: Humanized Input](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script Mode Control Flow](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)
- [Cluster Mode](https://psyb0t.github.io/docker-stealthy-auto-browse/cluster-mode/)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON API requests and Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser text, HTML, structured page data, or screenshots returned by authorized test actions.]

## Skill Version(s):

3.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
