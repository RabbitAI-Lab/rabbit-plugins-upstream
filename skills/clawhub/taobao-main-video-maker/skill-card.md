## Description:

Creates a short, product-focused Taobao or Tmall listing video from an inspectable product photo and seller-provided details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and ecommerce teams use this skill to plan and create short, silent product showcase videos for Taobao and Tmall listings from product photos and confirmed selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device authorization can be reused across Beatra skills.

Mitigation: Authorize only if shared credential access is acceptable, and keep the device token private.

Risk: Paid media generation can spend wallet credits.

Mitigation: Review the live price estimate and confirm each paid stage before submission.

Risk: Automatic package updates may install without separate approval.

Mitigation: Disable automatic updates when explicit update approval is required.

Risk: The bundled client has generic remote tool access.

Mitigation: Review requested Beatra operations and use the documented product-video workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/taobao-main-video-maker)
- [Beatra skill homepage](https://beatra.ai/skills/taobao-main-video-maker)
- [Taobao main product video workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Video artifacts, Shell commands]

**Output Format:** [Markdown guidance with video artifact details and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires separate approval for each paid stage.]

## Skill Version(s):

0.1.9 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
