## Description:

Provides browser automation designed to resist headless detection for authorized QA, compatibility testing, and defensive security research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized testers use this skill to exercise their own sites or in-scope targets where standard headless browsers trigger false-positive blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detection-resistant automation could be used on targets without permission.

Mitigation: Use only on sites you own or have written authorization to test, within the agreed scope.

Risk: An exposed browser API or noVNC viewer could allow unauthorized control of active sessions.

Mitigation: Bind ports to 127.0.0.1, set a strong AUTH_TOKEN, and keep noVNC local or disabled.

Risk: Persistent profiles, shared cookies, and captured page data could disclose credentials or sensitive content.

Mitigation: Use dedicated test accounts, minimize captured data, and protect or remove profile and Redis-backed session data after testing.

Risk: Unreviewed container images, compose files, or page loaders could introduce unwanted behavior.

Mitigation: Pin container images by digest and review compose files and loader YAML before deployment.

## Reference(s):

- [Setup and secure deployment](references/setup.md)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Script mode documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [Text, JSON, Screenshots, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and shell commands; browser actions return JSON, page content, or screenshots.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Captured pages and session data may be sensitive; limit collection to authorized tests.]

## Skill Version(s):

2.7.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
