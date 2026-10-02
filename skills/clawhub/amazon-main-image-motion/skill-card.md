## Description:

Turns one approved white-background product image into a short motion clip for a listing's main video slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers use this skill to plan and generate one short product-motion clip from an already approved white-background main image, with a review and credit-cost confirmation before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared, full-scope Beatra device token grants broad account authority.

Mitigation: Connect only if comfortable granting that authority; keep the device token private.

Risk: The bundled client can replace package-owned files automatically without a separate confirmation.

Mitigation: Review the package before installing and consider disabling automatic updates using the documented control.

Risk: Video generation consumes credits and additional takes can incur additional charges.

Mitigation: Review the production card and live credit cost, then explicitly approve each paid generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/amazon-main-image-motion)
- [Beatra skill homepage](https://beatra.ai/skills/amazon-main-image-motion)
- [Main image motion workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Video]

**Output Format:** [Markdown shot plan and review with a link to the generated video clip]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per approved image; reports actual duration, dimensions, and net credits charged.]

## Skill Version(s):

0.1.8 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
