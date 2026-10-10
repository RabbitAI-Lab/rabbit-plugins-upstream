## Description:

Helps advisors turn supplied quarterly report highlights and authorized stills into short, separately narrated talking clips, one per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors and fund marketers use this skill to plan and produce individual talking clips from their own quarterly report highlights and authorized images, without adding unsupported financial claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Device Token gives the bundled client broad account access.

Mitigation: Install only if that access is acceptable; keep the token private and use the skill for trusted Beatra workflows.

Risk: The bundled client can update installed package files automatically without separate approval.

Mitigation: Review the automatic-update policy and disable automatic updates using the documented command if required.

Risk: Voice cloning and generated media can incur charges or use someone's likeness without permission.

Mitigation: Confirm voice and image rights, review live prices, and obtain approval before each paid stage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/fund-report-talking)
- [Publisher skill page](https://beatra.ai/skills/fund-report-talking)
- [Quarterly report talking-clip workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Labeled clip plan and delivery summary with links to generated audio and video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One 2–15-second talking clip per authorized still; final media is returned by the connected service.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
