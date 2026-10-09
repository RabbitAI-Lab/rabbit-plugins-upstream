## Description:

Helps create short vertical Douyin product ads with an AI presenter, spoken pitch, and product-focused visuals from a product photo and merchant-approved details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use this skill to turn a product photo and approved claims into a short creator-style Douyin ad. The agent prepares a presenter frame and narration, obtains approval for paid stages, and delivers a video link with media and billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable shared Beatra credential can authorize media generation and spending.

Mitigation: Approve paid stages deliberately, monitor charges, and revoke the Beatra device in the Beatra Console when finished.

Risk: Product images and prompts are sent to Beatra.

Mitigation: Only submit material you are authorized and comfortable sharing with Beatra.

Risk: Installed package files update silently by default.

Mitigation: Disable automatic updates with the documented update --auto off command if you need to review changes first.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/douyin-ugc-ad-creator)
- [Publisher skill page](https://beatra.ai/skills/douyin-ugc-ad-creator)
- [Douyin UGC ad workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the approved script and creator direction, generated media links, actual media details, and charged credits.]

## Skill Version(s):

0.2.2 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
