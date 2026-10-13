## Description:

Animates a supplied still image into a short video with directed subject motion and camera movement, then guides review for visual drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn a supplied product photo, portrait, illustration, or artwork into a short video for social, promotional, or storyboard use while checking that important visual details remain recognizable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra device token can authorize other media and account capabilities beyond this image-to-video workflow.

Mitigation: Review the full account permissions before connecting, protect the local credential, and disconnect the device when no longer needed.

Risk: Generation can spend credits, and estimated charges may differ from final usage.

Mitigation: Review the live estimate and confirm sufficient balance before submission; check the completed task's net charged credits.

Risk: The package can update itself silently by default, replacing installed code.

Mitigation: Disable automatic updates with the documented update command if you need to review changes before replacement.

Risk: The client sends limited installation and environment metadata to Beatra.

Mitigation: Review the installation registration details before connecting if this reporting is sensitive.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/image-to-motion)
- [Beatra skill homepage](https://beatra.ai/skills/image-to-motion)
- [Image-to-video workflow](artifact/references/workflow.md)
- [Installation and authorization](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Video artifact links, Guidance]

**Output Format:** [Markdown with links to generated video artifacts and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires an accessible source image and user confirmation before paid submission; final charges and visual fidelity require review.]

## Skill Version(s):

0.2.2 (source: server-resolved ClawHub release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
