## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research. Camoufox + OS-level input + persistent fingerprints. Use only with sites you own or have written authorization to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and authorized security testers use the skill to check their own sites or approved targets against anti-bot controls, browser compatibility issues, and detection libraries. It supports controlled testing that needs realistic browser interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended container setup may grant broad privileges, including SYS_ADMIN.

Mitigation: Review required capabilities; prefer a tested setup without SYS_ADMIN, or isolate the workload in a dedicated VM if it is required.

Risk: An exposed unauthenticated API or viewer can give others control of the browser and access to its sessions.

Mitigation: Bind services to localhost, set AUTH_TOKEN for non-localhost deployments, and do not expose the noVNC viewer publicly.

Risk: Browser automation can capture sensitive page data or trigger state changes on real accounts.

Mitigation: Use only owned or explicitly authorized sites, limit capture to the test scope, and use disposable test accounts. Disable dialog auto-accept before actions that could change state.

Risk: Mounted loaders and CAPTCHA extensions can act on visited pages or access page data.

Mitigation: Audit loaders and extensions before enabling them, and protect persistent profiles and their session data.

## Reference(s):

- [Project homepage](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [Setup and security guidance](references/setup.md)
- [API reference: humanized input](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script mode control flow](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [API calls, Text, Screenshots, Shell commands, Configuration, Guidance]

**Output Format:** [JSON browser requests and results, YAML scripts, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browser actions and captured content depend on the authorized test task.]

## Skill Version(s):

3.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
