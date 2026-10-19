## Description:

Provides Docker-based browser automation for authorized QA, compatibility testing, and defensive security research against anti-bot systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized testers use this skill to operate a browser against their own sites or explicitly approved targets for anti-bot QA, compatibility checks, and defensive testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation can be misused against sites without permission.

Mitigation: Use only for authorized QA or defensive testing on owned sites or targets with written permission.

Risk: A mutable third-party Docker image and elevated container capability warrant careful review.

Mitigation: Pin and review the image or compose file before running it; limit container privileges and network access.

Risk: An exposed API or noVNC viewer can give others control of a live browser session.

Mitigation: Bind both services to localhost, set AUTH_TOKEN beyond smoke tests, and do not publish the viewer unless needed.

Risk: Persistent profiles and untrusted page loaders can expose sessions or trigger unintended actions.

Mitigation: Use test accounts, protect and remove profile data after testing, and mount only reviewed loaders.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup and security guidance](references/setup.md)
- [Project documentation](https://github.com/psyb0t/docker-stealthy-auto-browse)
- [Browser API reference](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)

## Skill Output:

**Output Type(s):** [Text, JSON, Images, Shell commands, Configuration guidance]

**Output Format:** [Markdown instructions and JSON browser responses, with optional screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May capture page content, screenshots, and recordings from authorized test sessions.]

## Skill Version(s):

3.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
