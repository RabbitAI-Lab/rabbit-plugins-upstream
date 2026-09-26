## Description:

Creates product short-video ads by turning selling points into a storyboard, generating shot clips, joining them, and adding subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and agent users use this skill to plan and generate 15-30 second product video ads from product selling points, reference images, storyboard prompts, and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and referenced images may be sent to the selected generation provider.

Mitigation: Use the documented dry-run first, choose the provider deliberately, and avoid sending sensitive or unauthorized content.

Risk: The skill uses provider credentials and writes generated media to local output paths.

Mitigation: Configure only the intended provider credentials, rotate keys when needed, and review output files before sharing or publishing them.

Risk: Sample brand and model descriptions may not match the user's lawful brand rights or advertising requirements.

Mitigation: Replace sample brand guidance with lawful, appropriate brand guidance and review generated ads before use.

## Reference(s):

- [Backend Calling Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON storyboard inputs, shell commands, MP4 video files, SRT subtitles, concat manifests, and optional JSON status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run planning before provider calls; generated clips and subtitles are written to the selected output directory.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
