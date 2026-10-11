## Description:

Guides detection-resistant browser automation for authorized QA, compatibility testing, and defensive security research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to test their own sites or targets they have written permission to assess, especially when standard headless automation is incorrectly blocked by bot detection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detection-resistant automation could be used against sites without permission.

Mitigation: Use only for sites you own or have written authorization to test; stay within the approved scope.

Risk: An exposed browser API or VNC port could grant unauthorized browser control.

Mitigation: Bind API and VNC to localhost and set AUTH_TOKEN for real use.

Risk: Container images or mounted loaders could execute unreviewed code.

Mitigation: Run only reviewed, digest-pinned images and mount only trusted loaders.

Risk: Persistent browser profiles can hold live sessions and sensitive account data.

Mitigation: Treat profile volumes as secrets and avoid real user or customer accounts.

Risk: Automatically accepted dialogs could approve unintended changes.

Mitigation: Disable automatic acceptance before actions that could trigger consequential dialogs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup and secure defaults](references/setup.md)
- [Humanized input documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script-mode control flow documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browser responses may contain page content, screenshots, and session data.]

## Skill Version(s):

3.0.2 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
