## Description:

Plans and creates short AI videos from text, supplied images, multimodal references, or existing footage, with review and targeted iteration of the resulting clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and other external users can plan, generate, edit, or extend short video clips for ads, product stories, social content, and cinematic concepts, then review delivered results before requesting another paid stage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad, persistent account token can expose account access if the device or credential file is compromised.

Mitigation: Install only if you trust Beatra; keep the token in the documented private credential file, limit local access, and disconnect when access is no longer needed.

Risk: The installed skill silently updates itself by default, outside a separate store approval.

Mitigation: Review the update policy and disable automatic updates with the documented update command when store-mediated review is required.

Risk: Uploaded media, installation registration telemetry, and paid video requests may affect privacy and account credits.

Mitigation: Share only approved media, evaluate the registration behavior against privacy needs, and confirm the live estimate and available balance before each paid video request.

## Reference(s):

- [Beatra AI Video Studio](https://beatra.ai/skills/beatra-ai-video-studio)
- [Intent and routing](artifact/references/intent-and-routing.md)
- [Video recipes](artifact/references/video-recipes.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Links, Guidance]

**Output Format:** [Markdown with generated media links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivered clips are reviewed before recommending a targeted edit, extension, or new render.]

## Skill Version(s):

1.3.1 (source: server-resolved release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
