## Description:

Restyles a short source video into a chosen visual treatment while aiming to preserve its subject, action, composition, and camera intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to turn one short source clip into an anime, illustration, ink, clay, or other chosen style while reviewing how well the result preserves the original scene and motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants a shared local device token with broad media and wallet-related permissions.

Mitigation: Review the requested permissions and connect only if comfortable granting them to Beatra.

Risk: The package checks for and installs verified updates automatically without separate confirmation.

Mitigation: Disable automatic updates with the documented command if each package change should require an explicit decision.

Risk: Video generation uses paid credits.

Mitigation: Review the estimate and require the documented approval before submitting a paid request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/ai-video-restyler)
- [Workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Installation and authorization](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with video artifact links and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned task status, video links, and actual billed credits.]

## Skill Version(s):

0.1.8 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
