## Description:

Provides detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to test browser interactions and anti-bot behavior on sites they own or have written authorization to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detection-resistant automation could be used outside authorized test scope.

Mitigation: Use only on sites you own or have written permission to test; respect the agreed scope.

Risk: An exposed browser service or viewer could give others control of a test session.

Mitigation: Bind ports to localhost, set AUTH_TOKEN, and keep noVNC private or disabled.

Risk: Persistent browser profiles may retain live sessions and sensitive data.

Mitigation: Use isolated test accounts, avoid customer data, and protect and remove profile volumes after testing.

Risk: Mounted page loaders can automatically act on matching sites.

Mitigation: Mount only loader YAML you have written or audited.

Risk: Unreviewed container image updates may change the behavior of the browser service.

Mitigation: Review the image and pin it by digest before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup and security guidance](references/setup.md)
- [Project homepage (declared in skill metadata)](https://github.com/psyb0t/docker-stealthy-auto-browse)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and curl; use only with authorized test targets.]

## Skill Version(s):

3.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
