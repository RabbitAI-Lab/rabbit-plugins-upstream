## Description:

Provides Docker-based, headless-detection-resistant browser automation for authorized QA, compatibility testing, and defensive security research on sites the user owns or is explicitly authorized to test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and authorized security testers use the Docker-hosted browser for anti-bot compatibility, regression testing, and defensive research on systems they own or have written permission to test. It is not intended for unauthorized access or scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended container setup grants the broad SYS_ADMIN capability.

Mitigation: Review the grant and avoid it unless necessary; otherwise use a dedicated disposable VM and pin a reviewed image digest.

Risk: An unauthenticated browser API or broadly exposed browser ports can allow others to control the browser and access its data.

Mitigation: Keep browser ports bound to localhost or otherwise restricted, authenticate the API, and explicitly pass AUTH_TOKEN to browser containers in cluster mode.

Risk: Automatic dialog acceptance or unreviewed page loaders can cause unintended actions during tests.

Mitigation: Audit loaders, disable automatic dialog acceptance before state-changing tests, and use isolated test accounts.

## Reference(s):

- [Setup and configuration](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Text, Screenshots, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTTP API requests, JSON payloads, shell commands, and browser-returned text or screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the authorized target and requested browser action.]

## Skill Version(s):

3.2.0 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
