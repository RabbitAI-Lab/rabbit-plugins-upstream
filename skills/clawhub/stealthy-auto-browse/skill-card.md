## Description:

Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and defensive security testers use this skill to automate authorized browser testing against sites they own or have written permission to assess, especially when standard headless browsers create false-positive bot-detection failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser-control API can be misused if exposed beyond an authorized local testing environment.

Mitigation: Bind the service to localhost, set AUTH_TOKEN, and use it only for sites owned by the operator or covered by written authorization.

Risk: Screenshots, DOM extraction, cookies, storage, and persistent profiles can capture sensitive session or page data.

Mitigation: Use dedicated test accounts, collect only the data needed for the authorized test, and delete persistent profile data when testing is complete.

Risk: The VNC viewer and mounted loaders can expand control or execution risk if exposed or unaudited.

Mitigation: Avoid exposing VNC, mount only reviewed loader files, and keep Docker images pinned to reviewed digests.

## Reference(s):

- [Setup](references/setup.md)
- [Skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, code]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces browser-control instructions and examples for an agent; screenshots and recordings may be produced by the external browser service when configured.]

## Skill Version(s):

2.6.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
