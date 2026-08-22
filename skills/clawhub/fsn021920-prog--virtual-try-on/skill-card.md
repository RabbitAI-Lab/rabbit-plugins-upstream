## Description:

Creates a realistic try-on image by fitting tops, pants, or dresses to a person photo with face preserved and seamless garment blending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fsn021920-prog](https://clawhub.ai/user/fsn021920-prog)

### License/Terms of Use:

CC BY-SA 4.0

## Use Case:

External users and creators use this skill to turn a person photo and a clothing photo into a prompt workflow for a realistic AI-generated try-on image, limited to tops, pants, and dresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Photos may include likenesses or garments the user does not have permission to use.

Mitigation: Use only photos the user owns or has permission to use, avoid third-party likenesses without consent, and stop when rights are unclear.

Risk: Synthetic try-on outputs may be mistaken for real photographs or endorsements.

Mitigation: Label outputs as AI-generated and do not present them as real photos, real photoshoots, advertisements, or endorsements.

Risk: Supplying photos to a configured image generator may expose sensitive personal images to that generator.

Mitigation: Install and run the skill only when the configured image generator's privacy and data-handling practices are acceptable for the supplied photos.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fsn021920-prog/skills/virtual-try-on)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prompt guidance with optional image-generation prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a person photo and a clothing photo; if no image generator is available, the skill stops after writing the prompt.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
