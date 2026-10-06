## Description:

Turns a product photo and merchant-provided details into a short vertical product video with spoken narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Online merchants and marketing teams use the skill to turn a product photo and verified selling points into a narrated video for listings, launches, and social posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable Beatra device credential grants broad access to media, artifacts, tasks, and wallet-related functions, especially on a shared machine.

Mitigation: Review Beatra account and device access before connecting; disconnect or remove the credential when no longer needed.

Risk: Product photos and related assets are uploaded to Beatra's service.

Mitigation: Upload only assets you are authorized and comfortable sharing with Beatra.

Risk: The bundled client silently updates itself by default.

Mitigation: Disable automatic updates with the documented `update --auto off` command if changes require prior review.

Risk: Image, speech, and video generation can consume paid credits.

Mitigation: Review estimates and approve preparation and final video separately before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/product-video-studio)
- [Product Video Studio homepage](https://beatra.ai/skills/product-video-studio)
- [Video creation workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with a generated-video link and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the returned video, duration, model, and net charged credits when available.]

## Skill Version(s):

0.1.9 (source: server-resolved release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
