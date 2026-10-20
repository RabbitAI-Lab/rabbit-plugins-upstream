## Description:

Turns a used-car condition sheet into a listing still, a spoken walkaround, and, after separate approval, one short walkaround clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Used-car dealers use this skill to plan a listing still and spoken script from a supplied condition sheet, then request one paid still, speech track, and walkaround clip with separate approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device authorization grants broader Beatra account access than the used-car workflow requires, and a shared token remains on the device.

Mitigation: Review the authorization scope before approving, protect the local credential, and use the bundled disconnect procedure when the connection is no longer needed.

Risk: Bundled helpers install package updates automatically by default and manage shared Beatra state during uninstall.

Mitigation: Review update behavior before installation, disable automatic updates if undesired, and check what other Beatra skills share the connection before uninstalling.

Risk: Generated listing media may misstate condition facts, while image, speech, and video generation consume credits.

Mitigation: Check printed and spoken claims against the supplied condition sheet and require a fresh approval with current pricing before each paid stage.

## Reference(s):

- [Used Car Walkaround on ClawHub](https://clawhub.ai/beatra-ai/skills/used-car-walkaround)
- [Used-car walkaround workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a listing plan, speakable script, approval cards, and delivery details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid Beatra operations may produce a listing still, speech audio, and a short video clip.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
