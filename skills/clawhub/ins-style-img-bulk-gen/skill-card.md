## Description:

Generate batches of Instagram-aesthetic photos (INS-style / Xiaohongshu / lifestyle flat-lay) by randomly composing prompts from an 80+ element library, then dispatching them in parallel to image generation skills and archiving to ~/Download/ins-image-{timestamp}/.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill to bulk-generate INS-style lifestyle image prompts and dispatch them to available image generation skills for scene-based visuals, cover art, and flat-lay photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic batch generation can create more outputs than intended when the user's creative request is ambiguous.

Mitigation: Review ambiguous requests before running; the skill defaults to five prompts when no count is specified.

Risk: Generated images are archived locally under ~/Download, which may create unwanted local files.

Mitigation: Use the skill only when local image archiving is desired and review the timestamped output folder after generation.

## Reference(s):

- [INS Style Elements Reference](references/ins-style-elements.md)
- [ClawHub Skill Page](https://clawhub.ai/mebusw/skills/ins-style-img-bulk-gen)
- [Server-Resolved Source Repository](https://github.com/mebusw/ins-style-img-bulk-gen)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Natural-language image prompts plus locally archived generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to five prompts when no count is specified and archives generated images under ~/Download/ins-image-{timestamp}/.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
